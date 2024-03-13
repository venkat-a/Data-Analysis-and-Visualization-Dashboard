"""
Created on Sun Apr 17 14:14:23 2021

@project: DSE_6000_SEM

@author: Venkata babu Alapati
"""

#Importing required libs and modules
import pandas as pd
import plotly.express as px
import clean_data
from clean_data import urban_rural,income_group,fcs,top10_countries1,country_fcs,country_wave\
                       ,country_wave_month,country_wave_gdp,monthly_covid_df,gdp_month \
                       ,df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df17,df18,df19,df20,df21,df22,df23,df24

#Intializing required Dataframes from data_clean module
df1=df1()
df2=df2()
df3=df3()
df4=df4()
df5=df5()
df6=df6()
df7=df7()
df8=df8()
df9=df9()
df10=df10()
df11=df11()
df12=df12()
#top10_countries=top10_countries1()
#country_wave=country_wave()
df13=df13()
df14=df14()
df15=df15()
df17=df17()
df18=df18()
df19=df19()
df20=df20()
df21=df21()
df22=df22()
df23=df23()
df24=df24()


#pie chart
urban_rural=urban_rural()
#bar or pie chart
income_group=income_group()
#hist
fcs=fcs()
#buble chart
top10_countries= top10_countries1()
#scater
country_fcs= country_fcs()
#skater
country_wave=country_wave()
#skater
country_wave_month=country_wave_month()
#
country_wave_gdp= country_wave_gdp()
#correlation
gdp_month=gdp_month()
#
monthly_covid_df= monthly_covid_df()


#Defining various plot functions

# Function definition for bar plot
def fig1():
    return px.bar(df4, x="type_of_people", y="responded", color="type_of_people", barmode="group",title = "Participation")
    
# Function definition for scatter plot
def fig2():
    return px.scatter(gdp_month,x="ln_GDP_pc",y="month",color="month",width=750, height=500, title = "ANALYSIS on Month and GDP")
    
# Function definition for line plot
def fig3():
    return px.line(country_wave_gdp,x="wave",y="ln_GDP_pc",color = "country",labels = {"wave" : "wave", "ln_GDP_pc" : "GDP",
           "country" : "Country name"},title = "Country GDP wrt Waves")
# Function definition for bar slide plot
def fig4():
    return px.bar(df5,x="income_group",y="participated_survey",color="income_group",barmode="group",
        title="Income wise Participation ")
# Function definition for strip plot
def fig5():
    return px.strip(df14,
               x="country",
               y="sample_counts",
               color="month",
               category_orders = {"country" : ["Sudan", "Zimbabwe", "Haiti","Ethiopia","Nigeria"]},
               title = " Sample Count Among countries ")
# Function definition for box plot
def fig6():
    return px.box(df14,
             x="country",
             y="sample_counts",
             color="country",
             category_orders = {"country" : ["Sudan", "Zimbabwe", "Haiti","Ethiopia","Nigeria"]},
             title="Mean sample Count Among countries ")
# Function definition for violin plot
def fig7():
    return px.violin(country_wave,x="country",y="wave",color="country",
    #category_orders = {"country" : ["Sudan", "Zimbabwe", "Haiti","Ethiopia","Nigeria"]},
    box=True, title="Mean wise sample among waves and countries")
# Function definition for histogram plot
def fig8():
    return px.histogram(df15,x="month",title = "GDP spread over months histogram")
# Function definition for sunburst plot
def fig9():
    return px.sunburst(df19,path=["region", "wave", "ln_GDP_pc"],values="sample_total",title="Region wise sample count wrt Waves")
# Function definition for scatter matrix plot
def fig10():
    return px.scatter_matrix(df19,dimensions=["region", "ln_GDP_pc", "sample_total"],color="region",title="Pair plot among regions")
# Function definition for scatter rapid plot
def fig11():
    return px.scatter(df20,
                 x="year",
                 y="ln_GDP_pc",
                 color="country",
                 size="sample_total",
                 hover_name="country",
                 animation_frame="wave",
                 animation_group="country",
                 log_x = True,
                 size_max=60,
                 range_x=[2020,2021],
                 range_y=[1,10],
                 #labels = {"gdpPercap" : "GDP per capita","lifeExp" : "life expectancy", },
                 title="Animated scatter plot GDP over year")

# Function definition for choropleth plot
'''
def fig12():
    return px.choropleth(df21, locations="code",color="region",hover_name="region",color_continuous_scale = "tempo")
'''
# Function definition for pie plot
def fig12():
    return px.pie(df22, values='fcs', names='country',title='Sample count percentage country wise',hover_data=['country'])
# Function definition for scatter slide plot
def fig13():
    return px.scatter(top10_countries, x = top10_countries.index, y = 'sample_total', size = 'sample_total', size_max = 120,
                color = top10_countries.index, title = 'Top 10 Collections')
# Function definition for histogram plot
def fig14():
    return px.histogram(df23, x="ln_GDP_pc",title='Histogram of GDP',
        opacity=0.8,log_y=True,color_discrete_sequence=['indianred'])
# Function definition for imshow plot
def fig15():
    return px.imshow(df24,color_continuous_scale='RdBu_r', origin='lower',title='Correlation map')


        
