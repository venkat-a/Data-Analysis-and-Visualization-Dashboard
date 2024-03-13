"""
Created on Sun Apr 17 14:14:23 2021

@project: DSE_6000_SEM

@author: Venkata babu Alapati
"""


#Importing libs 
import pandas as pd

#cleaning data set in 4 steps
data_frame=pd.read_csv('dashboard-data-latest.csv')
#data_frame = pd.read_excel('dashboard-data-latest.xlsx',sheet_name='2. Data')
df_covid=data_frame.drop(['code','region_code','row_id','last_updated','region.1','survey_link','survey_producer',
'lending_category','indicator_val','footnote','GDP_pc','indicator_description','indicator','indicator_display',],axis=1)
df_covid.dropna(inplace=True)

#changing float values to int for use of convience
df_covid["sample_total"] = df_covid["sample_total"].astype('int')
df_covid["month"] = df_covid["month"].astype('int')
df_covid["year"] = df_covid["year"].astype('int')

#Defined various functions that will create data frames dynamically 
#These small size dataframes makes web interface to run efficiently 
#The objected are created only when the dataframe is required by particular plot function

def urban_rural():
    urban_rural=data_frame['urban_rural'].value_counts()
    return urban_rural

def income_group():
    income_group=data_frame['income_group'].value_counts()
    return income_group


def fcs():
    fcs=data_frame['FCS'].value_counts()
    return fcs

#Used groupby command to extract to 10 countrys 
def top10_countries1():
    top10_countries1 = pd.DataFrame(df_covid.groupby('country')['sample_total'].sum().nlargest(10).sort_values(ascending = False))
    return top10_countries1
#scater
def country_fcs():
    country_fcs = pd.DataFrame(df_covid,columns=['country','FCS']).value_counts()
    return country_fcs
#skater
def country_wave():
    country_wave = pd.DataFrame(df_covid,columns=['country','wave'])
    return country_wave
#skater
def country_wave_month():
    country_wave_month = pd.DataFrame(df_covid,columns=['country','wave','month'])
    return country_wave_month
#
def country_wave_gdp():
    country_wave_gdp = pd.DataFrame(df_covid,columns=['country','wave','ln_GDP_pc'])
    return country_wave_gdp
#correlation
def gdp_month():
    gdp_month = pd.DataFrame(df_covid,columns=['ln_GDP_pc','month'])
    return gdp_month

#Used Groubby command to generate top low sample among regions
def least_gdp():
    least_gdp = pd.DataFrame(df_covid.groupby('region')['ln_GDP_pc'].sum().nlargest(10).sort_values(ascending = True))
    return  least_gdp

# Used to plot diffrent express plots using plotly
def monthly_covid_df():
    monthly_covid_df = data_frame.groupby(['month']).agg({'sample_subset':'sum'}).reset_index()
    return monthly_covid_df
def df1():
    df1= df_covid[df_covid["country"] == 'Ethiopia']
    return df1
def df2():
    df2= df_covid[df_covid["country"] == 'Somalia']
    return df2
def df3():
    df3= df_covid[df_covid["country"] == 'Haiti']
    return df3
def df7():
    df7 = pd.DataFrame(df_covid.groupby('country')['sample_total'].sum().nlargest(10).sort_values(ascending = False).rename_axis('country').reset_index(name='samples'))
    return df7
def df4():
    df4= data_frame['urban_rural'].value_counts().rename_axis('type_of_people').reset_index(name='responded')
    return df4
def df5():
    df5= data_frame['income_group'].value_counts().rename_axis('income_group').reset_index(name='participated_survey')
    return df5
def df6():
    df6= data_frame['FCS'].value_counts().rename_axis('FCS').reset_index(name='counts')
    return df6
def df8():
    df8=pd.DataFrame(df_covid,columns=['country','FCS']).value_counts()
    return df8
def df9():
    df9=pd.DataFrame(df_covid,columns=['country','wave'])
    return df9
def df10():
    df10=pd.DataFrame(df_covid,columns=['country','wave','month'])
    return df10
def df11():
    df11=pd.DataFrame(df_covid,columns=['ln_GDP_pc','month'])
    return df11
def df12():
    df12=pd.DataFrame(df_covid,columns=['ln_GDP_pc','month'])
    return df12
def df13():
    df13=pd.DataFrame(df_covid,columns=['country','month','sample_total']).value_counts().reset_index(name='sample_counts')
    return df13
def df14():
    df13a=pd.DataFrame(df_covid,columns=['country','month','sample_total']).value_counts().reset_index(name='sample_counts')
    df14=pd.DataFrame(df13a,columns=['country','month','sample_counts'])
    return df14
def df15():
    df15=pd.DataFrame(df_covid,columns=['ln_GDP_pc','month'])
    return df15
def df17():
    df16=pd.DataFrame(df_covid,columns=['country','month','sample_total']).value_counts().reset_index(name='sample_counts')
    df17=pd.DataFrame(df16,columns=['country','month','sample_counts'])
    return df17
def df18():
    df18=pd.DataFrame(df_covid,columns=['ln_GDP_pc','month'])
    return df18
def df19():
    df19=pd.DataFrame(df_covid,columns=['region','wave','ln_GDP_pc','sample_total'])
    return df19
def df20():
    df20=pd.DataFrame(df_covid,columns=['region','year','country','wave','ln_GDP_pc','sample_total'])
    return df20
def df21():
    df21=pd.DataFrame(df_covid,columns=['code','region','year','country','wave','ln_GDP_pc','sample_total'])
    return df21
def df22():
    df22=pd.DataFrame(df_covid,columns=['country','FCS']).value_counts().reset_index(name='fcs')
    return df22
def df23():
    df23 = pd.DataFrame(df_covid,columns=['ln_GDP_pc'])
    return df23
def df24():
    df24 = df_covid.corr()
    return df24






