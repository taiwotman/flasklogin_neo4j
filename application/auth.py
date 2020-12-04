"""Routes for user authentication."""
from flask import redirect, render_template, flash, Blueprint, request, url_for,session
from flask_login import login_required, logout_user, current_user, login_user
from flask import current_app as app
from werkzeug.security import generate_password_hash
from .assets import compile_auth_assets
from .forms import LoginForm, SignupForm
from .models import db, User
from .import login_manager
from datetime import datetime
import re

# Blueprint Configuration
auth_bp = Blueprint('auth_bp', __name__,
                    template_folder='templates',
                    static_folder='static')
compile_auth_assets(app)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login_page():
    """User login page."""
    # Bypass Login screen if user is logged in
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.dashboard'))
    login_form = LoginForm(request.form)
    # POST: Create user and redirect them to the app
    if request.method == 'POST':
        # Get Form Fields
        email = request.form.get('email')
        password = request.form.get('password')
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if not (re.search(regex, email)):
            flash("Invalid e-mail")
        elif login_form.validate():

            user = User(name=None,
                        email=email,
                        password=generate_password_hash(password, method='sha256'),
                        website=None)
                 # Validate Login Attempt
            if user.check_password(password=password):
                        login_user(user)
                        user.set_lastlogin()
                        next = request.args.get('next')
                        return redirect(next or url_for('main_bp.dashboard'))
            else:
              flash('Invalid username/password combination')
        return redirect(url_for('auth_bp.login_page'))
    # GET: Serve Log-in page
    return render_template('login.html',
                           form=LoginForm(),
                           title='Log in | Sentiment Analytics Dashboard',
                           template='login-page',
                           body="Log in with your User account.")


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup_page():
    """User sign-up page."""
    signup_form = SignupForm(request.form)
    # POST: Sign user in
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm = request.form.get('confirm')
        website = request.form.get('website')
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

        regex_website = re.compile(
        r'^(?:http)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' 
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        if len(name) < 1:
            flash('Your username must be at least one character.')
        elif not (re.search(regex, email)):
                    flash('Invalid e-mail')
        elif len(password) < 5:
            flash('Your password must be at least 5 characters.')
        elif password != confirm:
            flash('Password do not match.')
        elif website and (not re.search(regex_website, website)):
            flash('Invalid website url')
        elif signup_form.validate():
            # Get Form Fields

            user = User(name=name,
                            email=email,
                            password=generate_password_hash(password, method='sha256'),
                            website=website)

            existing_user = user.find()

            if existing_user is None:
                db.graph.push(user)
                login_user(user)
                return redirect(url_for('main_bp.dashboard'))
            flash('A user already exists with that email address.')
            return redirect(url_for('auth_bp.signup_page'))
    # GET: Serve Sign-up page
    return render_template('/signup.html',
                           title='Create an Account | Sentiment Analytics Dashboard.',
                           form=SignupForm(),
                           template='signup-page',
                           body="Sign up for a user account.")


@auth_bp.route("/logout")
@login_required
def logout_page():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth_bp.login_page'))


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        query = 'match (n:User) where ID(n)={userid} return n'
        user = db.graph.run(query, parameters={'userid': user_id}).evaluate()
        user2 = User(user['name'], user['email'], user['password'], user['website'])
        return user2
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.')
    return redirect(url_for('auth_bp.login_page'))
