from traceback import print_tb
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

# st.sidebar.title("Control Center")
years = range(2012,2021)
plt_style = 'bmh'
all_factors = {
    'Food System Resilience Score':'Score',

    'Natural Capital': 'natural',
    'Biodiversity and Habitat':'BDH.new',
    'Ecosystem Status': 'ECS',
    'Sealevel Rise': 'Sealevel',
    'Forest Area':'Forest',
    'Land Degradation':'Land',
     'Energy Footprint':'energy' ,
     'Water Footprint':'Water' ,
    'Greenhouse emission per capita':'GHP.new' ,
    'Agricultural water quantity':'WaterQuant' ,
    'Agricultural water quality':'WaterQual' ,

    'Human Capital':'human' ,
    'Population Growth':'Demographics',
   'Literacy Rate':'literacy' ,
    'HDI Score':'HDI' ,
    'Labor Participation Rate': 'labrate',
    'Agricultural Production Index': 'agprod',
    'Agricultural Production Volatility': 'agVol',
    'Obsesity Prevelance':'obesity',
    'Food Safety':'foodsafe',
     'Drinking Water':'drinking',
     'Micronutrient Availability':'Micro' ,
     'Protein Quality':'Protein' ,
     'Food Diversity Score':'Diversity' ,


     'Social Capital':'social' ,
     'Urban Absorption Capacity':'urbancap',
     'Presence of SafetyNet':'safetynet' ,
    'Food Policy Score':'policyfood',
   'Nutritional Standards':'nutritional' ,
    'Gender Equity':'gender' ,
    'Political Stability':'political' ,
     'Corruption':'corruption' ,
   'Conflict':'conflict',

     'Financial Capital':'financial',
    'Per-Capita Income': 'perCapita' ,
   'Agricultural Education and Resources':'edu' ,
    'Agricultural Import Tariff':'tariff' ,
     'Agricultural GDP':'agGDP' ,
     'Access to finance for farmers':'finance' ,
    'Food Price Volatility':'priceVol' ,
    'Food Loss and Waste':'foodloss' ,

    'Manufactured Capital':'manufactured' ,
    'Index of Globalization':'kofgi' ,
    'Adaptation of agricultural policy':'agadaptpolicy' ,
    'Climate smart agriculture':'climatesma' ,
    'Disaster Mangement':'disman' ,
    'Sustainable use of Nitrogen':'Nindex',
    'Agricultural R&D':'RND' ,
    'Mobile access to farmers':'mobile' ,
    'Transportation':'transport' ,
    'Food Storage Facilities':'storage'
}

all_factors1 = {
    'Score': 'Food System Resilience Score',

    'natural': 'Natural Capital',
    'BDH.new': 'Biodiversity and Habitat',
    'ECS': 'Ecosystem Status',
    'Sealevel': "Sealevel Rise",
    'Forest': 'Forest Area',
    'Land':'Land Degradation',
     'energy': 'Energy Footprint',
     'Water': 'Water Footprint',
    'GHP.new': 'Greenhouse emission per capita',
    'WaterQuant': 'Agricultural water quantity',
    'WaterQual': 'Agricultural water quality',

    'human': 'Human Capital',
    'Demographics': 'Population Growth',
   'literacy': 'Literacy Rate',
    'HDI': 'HDI Score',
     'labrate': 'Labor Participation Rate',
     'agprod':'Agricultural Production Index',
     'agVol':'Agricultural Production Volatility',
    'obesity':'Obsesity Prevelance',
    'foodsafe': 'Food Safety',
     'drinking':'Drinking Water',
     'Micro': 'Micronutrient Availability',
     'Protein': 'Protein Quality',
     'Diversity': 'Food Diversity Score',


     'social': 'Social Capital',
     'urbancap':'Urban Absorption Capacity',
     'safetynet': 'Presence of SafetyNet',
    'policyfood': 'Food Policy Score',
   'nutritional': 'Nutritional Standards',
    'gender': 'Gender Equity',
    'political': 'Political Stability',
     'corruption': 'Corruption',
   'conflict':'Conflict',

     'financial': 'Financial Capital',
     'perCapita': 'Per-Capita Income',
   'edu': 'Agricultural Education and Resources',
    'tariff': 'Agricultural Import Tariff',
     'agGDP': 'Agricultural GDP',
     'finance': 'Access to finance for farmers',
    'priceVol': 'Food Price Volatility',
    'foodloss': 'Food Loss and Waste',

    'manufactured': 'Manufactured Capital',
    'kofgi': 'Index of Globalization',
    'agadaptpolicy': 'Adaptation of agricultural policy',
    'climatesma': 'Climate smart agriculture',
    'disman': 'Disaster Mangement',
    'Nindex':'Sustainable use of Nitrogen',
    'RND': 'Agricultural R&D',
    'mobile': 'Mobile access to farmers',
    'transport': 'Transportation',
    'storage': 'Food Storage Facilities'
}

dataColl = {}
for i in years:
    abc = pd.read_csv(str(i)+'.csv',index_col= 'Country').transpose()
    # dataColl[i] = pd.read_csv(DATA_URL + "\\"+str(i)+'.csv',index_col= 'Country')
    dataColl[i] = abc
# org_data=pd.read_csv(DATA_URL + "\\"+str(2012)+'.csv',index_col= 'Country')
org_data=dataColl[2020]
trans_data = org_data.transpose()
countries = org_data.index


def showPlot(df,index = "country",visType="Des",check="nice",present=pd.DataFrame()):
    # print(df)
    # df=df.transpose()
    # c1.write(df)
    # df.index.name=None
    plt.style.use(plt_style)
    for i in df.columns:
        print(i)
        
        d1,d2 = st.columns(2)

        if i in all_factors1.keys():
            d1.subheader(str.upper(all_factors1[i]))
        else:
            d1.subheader(str.upper(i))
        # else:
        #     d1.subheader(str.upper(i))
        print(df.head())



        if index!="country":
            df["var_name"] = [all_factors1[i] for i in df.index]
        else:
             df["var_name"]  = df.index

        print(df.head())

        if(index!="country"):
            a1,a2,a3,a4,a5,a6 = st.columns(6)

            if(present.empty):    
                print("Present Empty")   

                a1.metric(label="Food System Resilience Score",value=df.loc[df["var_name"]=="Food System Resilience Score",i])
                a2.metric(label="Natural Capital",value=df.loc[df["var_name"]=="Natural Capital",i])
                a3.metric(label="Human Capital",value=df.loc[df["var_name"]=="Human Capital",i])
                a4.metric(label="Social Capital",value=df.loc[df["var_name"]=="Social Capital",i])
                a5.metric(label="Financial Capital",value=df.loc[df["var_name"]=="Financial Capital",i])
                a6.metric(label="Manufactured Capital",value=df.loc[df["var_name"]=="Manufactured Capital",i])
            else:
                print(present.head())
                print("OKOK")
                print(df.head())
                a1.metric(label="Food System Resilience Score",value=present.loc[present.index=="Score",i][0],delta=str(np.round(df.loc[df["var_name"]=="Food System Resilience Score",i][0],2)))
                a2.metric(label="Natural Capital",value=present.loc[present.index=="natural",i][0],delta=str(np.round(df.loc[df["var_name"]=="Natural Capital",i][0],2)))
                a3.metric(label="Human Capital",value=present.loc[present.index=="human",i][0],delta=str(np.round(df.loc[df["var_name"]=="Human Capital",i][0],2)))
                a4.metric(label="Social Capital",value=present.loc[present.index=="social",i][0],delta=str(np.round(df.loc[df["var_name"]=="Social Capital",i][0],2)))
                a5.metric(label="Financial Capital",value=present.loc[present.index=="financial",i][0],delta=str(np.round(df.loc[df["var_name"]=="Financial Capital",i][0],2)))
                a6.metric(label="Manufactured Capital",value=present.loc[present.index=="manufactured",i][0],delta=str(np.round(df.loc[df["var_name"]=="Manufactured Capital",i][0],2)))   
            
       
        best_10 = df.sort_values(i,ascending = False).head(10)
        best_10[i] = best_10[i].apply(np.round)
        best_10 = best_10.sort_values(i,ascending=True)

        print(best_10)

        c1,c2 = st.columns(2)


        fig1 = px.bar(best_10, x = i,y = "var_name",orientation='h',text=i)
        
        fig1.update_layout(xaxis_range=[0,100],yaxis_title=None, xaxis_title=None)
        fig1.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
        fig1.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))
        fig1.update_traces(textposition='outside')
    
        c1.plotly_chart(fig1)



        worst_10 = df.sort_values(i,ascending = True).head(10)
        worst_10[i] = worst_10[i].apply(np.round)
        worst_10 = worst_10.sort_values(i,ascending=False)
        print(worst_10)

        fig2 = px.bar(worst_10, x = i,y = "var_name",orientation='h',text=i)


        fig2.update_layout(xaxis_range=[0,100],yaxis_title=None, xaxis_title=None)
        fig2.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
        fig2.update_traces(textposition='outside')
        fig2.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))


        if(visType=="Des"):
            fig2.update_layout(xaxis_range=[0,100],yaxis_title=None, xaxis_title=None)
        else:
            fig2.update_layout(xaxis_range=[-100,5],yaxis_title=None, xaxis_title=None)
   
        c2.plotly_chart(fig2)

        del d1,d2,c1,c2

        if index!="country":
            del a1,a2,a3,a4,a5,a6




def showOption():
    opts = ['Country','Indicator']
    op = st.sidebar.selectbox('Analysis by:',opts)
    return op

def visualizeOp(op,yearChoice=2020):
    global dataColl
    if(isinstance(yearChoice,list)):
        if(len(yearChoice)==1):
            yearChoice = yearChoice[0]
        else:
            yearChoice=2020
    if op=="Country":
        countrySelect = st.sidebar.multiselect('Select Country(ies)',countries)
        print("choice of year = " + str(yearChoice))
        # abc = abc.append(i for i in countrySelect)
        # org_data=pd.read_csv(DATA_URL + "\\"+str(yearChoice)+'.csv',index_col= 'Country')
        org_data=dataColl[yearChoice]
        # df = org_data[countrySelect]
        df = org_data[org_data.index.isin(countrySelect)].transpose()
        print(df)
        showPlot(df,index='indicator')

     
    else:
        indSelect1 = st.sidebar.multiselect('Select indicator(s)',all_factors.keys())
        # trans_data=pd.read_csv(DATA_URL + "\\"+str(yearChoice)+'.csv',index_col= 'Country').transpose()
        indSelect = [all_factors[i] for i in indSelect1]
        print("choice of year = " + str(yearChoice))
        trans_data=dataColl[yearChoice]
        df1 = trans_data[indSelect]
        # print(df1)

        showPlot(df1,index='country')



def app():
    yearChoice =  st.sidebar.selectbox('Select Year(s)',sorted(list(years),reverse=True))
    print(type(yearChoice))
    op =showOption()
    visualizeOp(op,yearChoice)