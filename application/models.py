"""Database models."""
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from py2neo import Node, NodeMatcher
from py2neo.ogm import GraphObject, Property
from datetime import datetime

class User(UserMixin, GraphObject):
    """Model for user accounts."""
    name = Property()
    email = Property()
    password = Property()
    website = Property()
    created_on = Property()
    last_login = Property()
    
    matcher = NodeMatcher(db.graph)
    
    def __init__(self,  name, email, password,website):

        self.name = name
        self.email = email
        self.password = password
        self.website = website
        self.created_on = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.last_login = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def find(self):
        # user = db.graph.find_one('User', 'email', self.email)  # ! deprecated
        user = matcher.match("User", email = self.email).first()
        return user

    def get_id(self):
        query = 'match (n:User) where n.email={email} return ID(n)'

        #user = db.graph.find_one('User', 'email', self.email) # ! find_one deprecated
        #id = db.graph.run(query, parameters={'email': user['email']}).evaluate()  # ! deprecated
        user = matcher.match("User", email = self.email).first()
        id = db.graph.run(query, email = user['email']).evaluate()
 
        return id

    def set_lastlogin(self):
        query = " MATCH (p:User) SET p.last_login = {last_login}"
        db.graph.run(query, last_login = self.last_login)

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
        if not self.find():
            user = 
            ('User', name=self.name, email=self.email, password=self.password, website=self.website, created_on=self.created_on, last_login=self.last_login)
            db.graph.create(user)
            return True
        else:
            return False

    def check_password(self, password):
        """Check hashed password."""
        user = self.find()
        if user:
            return check_password_hash(user['password'], password)
        else:
            return False



    def __repr__(self):
        return '<User {}>'.format(self.email)
