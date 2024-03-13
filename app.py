"""
Created on Sun Apr 17 14:14:23 2021

@project: DSE_6000_SEM

@author: Venkata babu Alapati
"""


#Importing Required libs and modules
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import visualization
from visualization import fig1,fig2,fig3,fig4,fig5,fig6,fig7,fig8,fig9,fig10,fig11,fig12,fig13,fig14,fig15

#External web interface intilization
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#Intialzing dash app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#call deployment server 
server = app.server

#Getting the COID_19 image
COVID_IMG = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fbigredmarkets.com%2Fwp-content%2Fuploads%2F2020%2F03%2FCovid-19.png&f=1&nofb=1"

#calling functions to plot from visuvalization module
fig1=fig1()
fig2=fig2()
fig3=fig3()
fig4=fig4()
fig5=fig5()
fig6=fig6()
fig7=fig7()
fig8=fig8()
fig8.update_layout({"bargap": 0.02})
fig9=fig9()
fig10=fig10()
fig11=fig11()
fig12=fig12()
fig12.update_traces(textposition='inside', textinfo='percent+label')
#fig12.update_traces(marker_line_color="white")
fig13=fig13()
fig14=fig14()
fig15=fig15()
#fig16=fig16()

#Creating App layout
app.layout = html.Div(children=[
    # All elements from the top of the page 
    #calling html methods for slider, headings and subheadings in webinterface
    html.Div([
        html.Marquee("National participation is high in the survey more than urban and rural ; Ethiopia is the nation with maximum number of survey responders; High income group is the one least Partipated in the survey "),
        html.H1(children='DSE 6000 SEMESTER PROJECT'),
        html.H1(children='Venkata babu Alapati'),
        html.Img(src = COVID_IMG, height = "30px"),
        html.Div(children='COVID_19 SURVEY DATA  ANALYSIS'),
        html.Div(children='''Exploration of covid survey data from 2020 to 2021. Analysis focused on waves, GDP , income group , total samples collected,and  urban rural participation'''),
#html interface to call back and plot fig1
        html.Div(children='''Plot1: Diffrent group of People Responded to the survey.'''),
        dcc.Graph(
            id='graph1',
            figure=fig1
        ),  
        html.Div(children='''
            Low response from Rural People and high response from nationals 
        '''),
    ]),



#html interface to call back and plot fig2
    html.Div([
        #html.H1(children='ANALYSIS on Month and GDP'),

        html.Div(children='''
            Plot2: Analysis on months over GDP.
        '''),

        dcc.Graph(
            id='graph2',
            figure=fig2
        ),
        html.Div(children='''
            We can see that GDP 7-9 is most common among all months.
        '''),


    ]),
#html interface to call back and plot fig3
     html.Div([
        #html.H1(children='Countries GDP over waves'),

        html.Div(children='''
            Plot3: Countries participation in survey over waves .
        '''),

        dcc.Graph(
            id='graph3',
            figure=fig3
        ),
        html.Div(children='''
            We can that Countries with high GDP participated less in survey among waves .
        '''),

    ]),
#html interface to call back and plot fig4
     html.Div([
        #html.H1(children='Hello Dash'),

        html.Div(children='''
            Plot4: Income groups relation to the participation in survey 
        '''),

        dcc.Graph(
            id='graph4',
            figure=fig4
        ),
        html.Div(children='''
            We can observe that high Income group are the ones least participated in the survey 
        '''),

    ]),
#html interface to call back and plot fig5
     html.Div([
        #html.H1(children='Income wise Participation'),

        html.Div(children='''
           Plot5: Countries not in survey over months
        '''),

        dcc.Graph(
            id='graph5',
            figure=fig5
        ),
        html.Div(children='''
            we can see that many countries not taken part of survey for all months
        '''),
    ]),
#html interface to call back and plot fig6
     html.Div([
        #html.H1(children='Sample Count Among countires'),

        html.Div(children='''
             Plot6: Mean of sample count of countires
        '''),

        dcc.Graph(
            id='graph6',
            figure=fig6
        ),  
        html.Div(children='''
            we can see that from many countires fall below the mean of sample count
        '''),
    ]),
#html interface to call back and plot fig7
     html.Div([
        #html.H1(children='Mean sample Count Among countires'),

        html.Div(children='''
            Plot7: Density of countries participation over waves
        '''),

        dcc.Graph(
            id='graph7',
            figure=fig7
        ),  
        html.Div(children='''
            we can see that almost all countries participated in wave1 survey
        '''),
    ]),
#html interface to call back and plot fig8
     html.Div([

        html.Div(children='''
            Plot8: Histogram of GDP
        '''),

        dcc.Graph(
            id='graph8',
            figure=fig8
        ),
        html.Div(children='''
            We can find it from the observation that it symetric and fallows normal distribution
        '''),  
    ]),
#html interface to call back and plot fig9
     html.Div([

        html.Div(children='''
            Plot9: Region wise sample count with labels
        '''),

        dcc.Graph(
            id='graph9',
            figure=fig9
        ),
        html.Div(children='''
            Region wise sample count with respect to waves
        '''),
    ]),
#html interface to call back and plot fig10
    html.Div([
    
        html.Div(children='''
           Plot10: How Regions related to survey
        '''),

        dcc.Graph(
            id='graph10',
            figure=fig10
        ),
        html.Div(children='''
            Region wise understanding of the survey data with visuvalization
        '''),  
    ]),
#html interface to call back and plot fig11
     html.Div([

        html.Div(children='''
            Plot11: Animated plot GDP over waves
        '''),

        dcc.Graph(
            id='graph11',
            figure=fig11
        ), 
        html.Div(children='''
            By click one can select or deselct the Countries, that will change the volume with respect to selected countires for GDP over waves, slides from left to right and vice versa
        '''), 
    ]),
#html interface to call back and plot fig12
     html.Div([

        html.Div(children='''
           Plot12: Finding countries percentage with Animated pie chart
        '''),

        dcc.Graph(
            id='graph12',
            figure=fig12
        ), 
        html.Div(children='''
            By click one can select or deselct the Countries, that will change the percentage with respect to the selected countires 
        '''), 
    ]),
#html interface to call back and plot fig13
     html.Div([

        html.Div(children='''
           Plot13: Top 10 countries based on Survey sample count
        '''),

        dcc.Graph(
            id='graph13',
            figure=fig13
        ),
        html.Div(children='''
            By click one can select or deselct among the top 10 Countries, that will change the volume of the country with respect to the selected countries
        '''),
  
    ]),
#html interface to call back and plot fig14
     html.Div([

        html.Div(children='''
           Plot14: comparison of Histogram GDP alone  versus GDP over months histogram
        '''),

        dcc.Graph(
            id='graph14',
            figure=fig14
        ),  
        html.Div(children='''
            We can observe that Histogram of GDP alone is not symmetric as GDP over months 
        '''),
    ]),
#html interface to call back and plot fig15
     html.Div([

        html.Div(children='''
          Plot15: Finding correlation in the among numeric columns in the given dataset 
        '''),

        dcc.Graph(
            id='graph15',
            figure=fig15
        ), 
        html.Div(children='''
            We can see that all numeric data in the given data set is weekly correlated
        '''), 
    ]), 
#html interface to call conclusion
html.Div([
        html.H1(children='Conclusion:'),

        html.Div(children='''
            -Want to explore the  different patterns presented in the dataset and their interrelationships using plots'''),
        html.Div(children='''
            -Numeric data is weekly correlated, Numeric feature GDP is symmetic and it fallows a normal distribution
 '''),
        html.Div(children='''
            -Observerd countries participation with respect to waves
            '''),
        html.Div(children='''
            -Explored region,country wise Survey count related to income group, gdp '''),
        html.Div(children='''
            -Expiremented with income groups participation in survey,which is interesting'''),
        
    ]),
     html.Div([
        html.H1(children='Learnings:'),

        html.Div(children='''
            -Explored different libraries ,functions, editors  and API interfaces'''),
        html.Div(children='''
            -Used Modularized approach while writing the scripts'''),
        html.Div(children='''
            -Deployed the app on both platforms GCP and Horeku'''),
        html.Div(children='''
            -Learned html interfaces apart and dash APIs'''),

    ]),
     
])
#Calling Main function
if __name__ == '__main__':
    app.run_server(debug=True)
