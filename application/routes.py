"""
Author: Taiwo O. Adetiloye
Date: Dec 27, 2019 
"""

"""Routes for logged-in application."""
from bokeh.plotting import figure
from bokeh.embed import components
from math import pi
import pandas as pd
from bokeh.palettes import Category20c
from bokeh.transform import cumsum

from flask import Blueprint, render_template, request
from flask_login import current_user
from flask import current_app as app
from .assets import compile_auth_assets
from flask_login import login_required
from .models import db
import numpy as np
from flask_paginate import Pagination, get_page_args

# Blueprint Configuration
main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')
compile_auth_assets(app)


@main_bp.route('/', methods=['GET', 'POST'])
@login_required
def dashboard():
    """Serve logged in Dashboard."""
 
    facilities = [''] #Enter list items
    selected_facility = request.form.get('facility')

    facilities2 = ['']  #Enter list items

    if (not selected_facility) or selected_facility == 'Select facility':
        return render_template('dashboard.html',
                               title='Sentiment Analytics Dashboard.',
                               template='dashboard-template',
                               current_user=current_user,
                               facilities=facilities,
                               Facilities='Facilities',
                               display='none',
                               selected_facility='24',
                               body="You are now logged in!")
    elif (selected_facility in facilities2):

        query_count_patient = 'MATCH (n:Patient)-[r:SURVEY_ON]->(f:Facility) WHERE f.facility_code={facility_code}  return count(n)'
        count_patient = db.graph.run(query_count_patient, parameters={'facility_code': selected_facility}).evaluate()

        query_gross = 'MATCH (n:Patient)-[r:SURVEY_ON]->(f:Facility)  return count(ID(n))'


        count_gross = db.graph.run(query_gross).evaluate()



        #------------------------------------------Bar plot

        def make_bar_plot():
            label = [selected_facility, 'All facilities']
            y = [count_patient, count_gross]
            plot = figure(x_range=label, y_range=(0, count_gross), plot_width=500, plot_height=300,
                          title="Patient Survey(facility) and Total Survey(all facilities)")
            plot.xaxis.major_label_orientation = np.pi / 4
            plot.vbar(label, top=y, width=0.5, color="#CAB2D6")

            script, div = components(plot)

            return script, div

        plots = []
        plots.append(make_bar_plot())

        #------------------------------------------End Bar plot


        #------------------------------------------Grid table


        query_response_negative = "match (p:Patient)-[r:SURVEY_ON]->(f:Facility)  where f.facility_code={facility_code} and p.sentiment='Negative' return  ID(p), p.response, p.date,p.service_type_code ORDER BY p.date DESC"
        query_response_positive = "match (p:Patient)-[r:SURVEY_ON]->(f:Facility)  where f.facility_code={facility_code} and p.sentiment='Positive' return ID(p), p.response, p.date,p.service_type_code ORDER BY p.date DESC"
        query_response_neutral = "match (p:Patient)-[r:SURVEY_ON]->(f:Facility)  where f.facility_code={facility_code} and p.sentiment='Neutral' return ID(p), p.response,p.date ,p.service_type_code ORDER BY p.date DESC"

        query_response_negative2 = "match (p:Patient)-[r:SURVEY_ON]->(f:Facility)  where f.facility_code={facility_code} and p.sentiment='Negative' return count(p)"
        query_response_positive2 = "match (p:Patient)-[r:SURVEY_ON]->(f:Facility)  where f.facility_code={facility_code} and p.sentiment='Positive' return count(p)"
        query_response_neutral2 = "match (p:Patient)-[r:SURVEY_ON]->(f:Facility)  where f.facility_code={facility_code} and p.sentiment='Neutral' return count(p)"

        count_negative = db.graph.run(query_response_negative2, parameters={'facility_code': selected_facility}).evaluate()
        count_positive = db.graph.run(query_response_positive2, parameters={'facility_code': selected_facility}).evaluate()
        count_neutral = db.graph.run(query_response_neutral2, parameters={'facility_code': selected_facility}).evaluate()
        total_sentiment = count_negative + count_positive + count_neutral

        def sentiment(query_response):
            comment_id= []
            comment_list = []
            date = []
            comment_svt_code = []


            comments_db = db.graph.run(query_response, parameters={'facility_code': selected_facility}).data()

            for comment in comments_db:
                comment_id.append(comment['ID(p)'])
                comment_list.append(comment['p.response'])
                date.append(comment['p.date'])
                comment_svt_code.append(comment['p.service_type_code'])

            return (list(dict.fromkeys(comment_id)),comment_list,date,comment_svt_code) #' list(dict.fromkeys(comment_service_type_code))   # Remove duplicates

        sentiment_pos = zip(sentiment(query_response_positive)[1],sentiment(query_response_positive)[2], sentiment(query_response_positive)[3])
        sentiment_neg = zip(sentiment(query_response_negative)[1],sentiment(query_response_negative)[2], sentiment(query_response_negative)[3])
        sentiment_neu = zip(sentiment(query_response_neutral)[1], sentiment(query_response_neutral)[2],sentiment(query_response_neutral)[3])

        # ------------------------------------------Grid table Ends


        #------------------------------------------Pie Chart plot
        def make_pie_plot():
            x = {
                'Positive':  count_positive/total_sentiment,
                'Neutral': count_neutral/total_sentiment,
                'Negative': count_negative/total_sentiment
            }
            data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'sentiments'})
            data['angle'] = data['value'] / data['value'].sum() * 2 * pi
            data['color'] = Category20c[len(x)]

            p = figure(plot_height=250,plot_width=300, title="Patient Sentiment Pie Chart", toolbar_location=None,
                       tools="hover", tooltips="@sentiments: @value{0.00%}", x_range=(-0.5, 1.0),
                       background_fill_color='#CAB2D6',
                       border_fill_color='#CAB2D6',)

            p.wedge(x=0, y=1, radius=0.4,
                    start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
                    line_color="white", fill_color='color', legend_field='sentiments', source=data)

            p.axis.axis_label = None
            p.axis.visible = False
            p.grid.grid_line_color = None

            script, div = components(p)

            return script, div

        plots_pie = []
        plots_pie.append(make_pie_plot())


        #------------------------------------------Pie Chart End plot



        return render_template('dashboard.html',
                               title='Sentiment Analytics Dashboard.',
                               template='dashboard-template',
                               current_user=current_user,
                               selected_facility=selected_facility,
                               facilities=facilities,
                               Facilities='Facility',
                               count_patient=total_sentiment,
                               count_gross=count_gross,
                               percentage=  str(round((total_sentiment * 100 / count_gross), 2)) + '%', #percentage
                               plots=plots,
                               plots_pie=plots_pie,
                               display='block',
                               positive=sentiment_pos,
                               negative=sentiment_neg,
                               neutral=sentiment_neu,
                               body="You are now logged in!")
