from audioop import reverse
from email.policy import default
from glob import glob
from re import T
from turtle import lt, width
from matplotlib.axis import XAxis
from matplotlib.colors import hexColorPattern
from numpy.core.fromnumeric import prod
from pandas.core.indexes import base
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from streamlit import caching
from validators import length


import copy

from pathlib import Path
import seaborn as sns
import geopandas
from mpl_toolkits.axes_grid1 import make_axes_locatable

import plotly.express as px
from PIL import Image
import plotly.graph_objects as go


# import SessionState 
# session = SessionState.get(run_id=0)

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
    'foodsafe': 'Food Safetly',
     'drinking':'Drinking Water',
     'Micro': 'Micronutrient Availability',
     'Protein': 'Protein Quality',
     'Diversity': 'Food Diversity Score',


     'social': 'Social',
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


     'Social':'social' ,
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


natural = ['BDH.new', 'ECS', 'Sealevel', 'Forest', 'Land', 'energy', 'Water', 'GHP.new', 'WaterQuant', 'WaterQual']
human = ['Demographics', 'literacy', 'HDI', 'labrate', 'agprod', 'agVol', 'obesity', 'foodsafe', 'drinking', 'Micro', 'Protein', 'Diversity']
social = ['urbancap', 'safetynet', 'policyfood', 'nutritional', 'gender', 'political', 'corruption', 'conflict']
financial = ['perCapita', 'edu', 'tariff', 'agGDP', 'finance', 'priceVol', 'foodloss']
manufactured = ['kofgi', 'agadaptpolicy', 'climatesma', 'disman', 'Nindex', 'RND', 'mobile', 'transport', 'storage']

natural1 = [all_factors1[i] for i in ['BDH.new', 'ECS', 'Sealevel', 'Forest', 'Land', 'energy', 'Water', 'GHP.new', 'WaterQuant', 'WaterQual']]
human1 = [all_factors1[i] for i in ['Demographics', 'literacy', 'HDI', 'labrate', 'agprod', 'agVol', 'obesity', 'foodsafe', 'drinking', 'Micro', 'Protein', 'Diversity']]
social1 = [all_factors1[i] for i in ['urbancap', 'safetynet', 'policyfood', 'nutritional', 'gender', 'political', 'corruption', 'conflict']]
financial1 = [all_factors1[i] for i in ['perCapita', 'edu', 'tariff', 'agGDP', 'finance', 'priceVol', 'foodloss']]
manufactured1 = [all_factors1[i] for i in ['kofgi', 'agadaptpolicy', 'climatesma', 'disman', 'Nindex', 'RND', 'mobile', 'transport', 'storage']]

plt_style = 'bmh'
# plt_style = 'fivethirtyeight'

# 
st.set_page_config(layout="wide")
st.title("Five Capitals Food System Resilience Score (5CFSRS) Analysis Tool")
st.markdown('The 5CFSRS gives the scores for several food system resilience indicators based on the performance of the countries.')
st.markdown('This Dashboard is the preliminary version of a diagnostic tool for rapidly scanning food stresses and shocks.')




@st.cache(persist=True)
def load_data(data_url):
    data=pd.read_csv(data_url)
    return data

DATA_URL = r"C:\Users\kc003\OneDrive - CSIRO\Projects\Composite Score\masterDataset\Yearwisedata"


years = range(2012,2021)
dataColl = {}
for i in years:
    abc = pd.read_csv(str(i)+'.csv',index_col= 'Country').transpose()
    # dataColl[i] = pd.read_csv(DATA_URL + "\\"+str(i)+'.csv',index_col= 'Country')
    dataColl[i] = abc
# org_data=pd.read_csv(DATA_URL + "\\"+str(2012)+'.csv',index_col= 'Country')
org_data=dataColl[2020]
trans_data = org_data.transpose()




## *********** FUNCTIONS ***********
def showOption():

    opts = ['Country','Indicator']
    op = st.sidebar.selectbox('Analysis by:',opts)
    return op

def showPlot(df,c1,c2,visType="Des"):
    print(df)
    # df=df.transpose()
    # c1.write(df)
    # df.index.name=None
    plt.style.use(plt_style)
    for i in df.columns:
        # print(i)
        if i in all_factors1.keys():
            c1.write(str.upper(all_factors1[i]))
        else:
            c1.write(str.upper(i))

        # fig,axs = plt.subplots(figsize=(6,4))
        # df[i].sort_values(ascending= False).head(10).plot.barh()
        # plt.xlim([0,100])
        # # plt.show()
        # c1.pyplot(fig)

        # px.bar()
        # print(df[i])
        best_10 = df.sort_values(i,ascending = False)[i].head(10)

        fig1 = px.bar(best_10, x = i,y = best_10.index,orientation='h')
        fig1.update_layout(xaxis_range=[0,100],yaxis_title=None, xaxis_title=None)
        fig1.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
        fig1.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))
        # c1.write("Most Resilient Nations")
        c1.plotly_chart(fig1)

        if i in all_factors1.keys():
            c2.write(str.upper(all_factors1[i]))
        else:
            c2.write(str.upper(i))

        worst_10 = df.sort_values(i,ascending = True)[i].head(10)

        fig2 = px.bar(worst_10, x = i,y = worst_10.index,orientation='h')

        fig2.update_layout(xaxis_range=[0,100],yaxis_title=None, xaxis_title=None)
        fig2.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
        fig2.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))

        if(visType=="Des"):
            fig2.update_layout(xaxis_range=[0,100],yaxis_title=None, xaxis_title=None)
        else:
            fig2.update_layout(xaxis_range=[-100,5],yaxis_title=None, xaxis_title=None)
        # c1.write("Most Resilient Nations")
        c2.plotly_chart(fig2)
            
        
        # c1.write(df[i].sort_values(ascending= False).head(10))
 
        
        # # c2.write(df[i].sort_values(ascending= True).head(10))
        # fig1,axs1 = plt.subplots(figsize=(6,4))
        # # plt.style.use(plt_style)
        # # c1.write(df[i].sort_values(ascending= False).head(10))
        # df[i].sort_values(ascending= True).head(10).plot.barh()
        # if(visType=="Des"):
        #     plt.xlim([0,100])
        # else:
        #     plt.xlim([-50,5])
        # plt.ylabel(None)
        # # plt.show()
        # c2.pyplot(fig1)

def linePlot(df,countrySelect,c1,c2):
    df.index.name=None
    # c1.write(df)
    
    if(len(countrySelect)!=0):
        df =df[df.index.isin(countrySelect)]
        check = df.reset_index().set_index("Year")
        print(check)
        # c1.write(df)
        plt.style.use(plt_style)
        for i in range(int(len(df.columns)/2)):

            if(df.columns[2*i] in all_factors1.keys()):
        
                c1.write(str.upper(all_factors1[df.columns[2*i]]))


            # fig = px.line(check.groupby("index")[check.columns[2*i]])

            # c1.plotly_chart(fig)

            fig,axs = plt.subplots(figsize=(6,4))
                
            
            # c1.write(df[i].sort_values(ascending= False).head(10))
            # df[i].sort_values(ascending= False).head(10).plot.barh()
            df.reset_index().set_index("Year").groupby("index")[df.columns[2*i]].plot(legend = True,style='.-')

            plt.ylim([0,100])
            plt.legend(loc='lower left')
            # plt.show()
            c1.pyplot(fig)

            # c2.write(str.upper(df.columns[2*i+1]))
            c2.write(str.upper(all_factors1[df.columns[2*i+1]]))
            # c2.write(df[i].sort_values(ascending= True).head(10))
            fig1,axs1 = plt.subplots(figsize=(6,4))
            plt.style.use(plt_style)
            # c1.write(df[i].sort_values(ascending= False).head(10))
            df.reset_index().set_index("Year").groupby("index")[df.columns[2*i+1]].plot(legend = True,style='.-')
            plt.ylim([0,100])
            plt.legend(loc='lower left')
            # plt.show()
            c2.pyplot(fig1)

def linePlot1(df,countrySelect,conPlots,capital):
    # print(df)
    # df1 =df[df.index.isin(countrySelect)]
    # # c1.write(df)
    
    # df["Country"]=df.index
    
    # df.reset_index(inplace =True,drop=True)


    # conPlots.pyplot(df.plot())
    # conPlots.write(df)
    # print(df.columns)
    # if(len(countrySelect)!=0):
    #     fig2,axs = plt.subplots(figsize=(4,2))
    #     # df.reset_index().set_index("Year").plot()
    #     sns.lineplot(data=df,x = "Year",y = [df.columns])
    #     plt.legend(loc='lower left')
    #     plt.ylim([0,100])
    #     conPlots.pyplot(fig2)
    # print(df)
    # print(countrySelect)
    # print(df)
    # print(countrySelect)
    ltitle = []
    if capital=="Natural":
        ltitle = natural1
    elif capital=="Human":
        ltitle = human1
    elif capital=="Social":
        ltitle = social1
    elif capital=="Financial":
        ltitle = financial1
    else:
        ltitle = manufactured1
    
    if(len(countrySelect)!=0):
        for i in countrySelect:
            df1=df[df.index==i]
            print(df1)
            conPlots.write(str.upper(i))
        


            fig2,axs = plt.subplots(figsize=(6,2.5))
            # fig2,axs = plt.subplots()
            
                    
            plt.style.use(plt_style)
            # c1.write(df[i].sort_values(ascending= False).head(10))
            # df[i].sort_values(ascending= False).head(10).plot.barh()
            # df.reset_index().set_index("Year").plot(legend = True,style='.-')
            dfm =df1.melt('Year',var_name="Capitals",value_name="Score")
            sns.lineplot(x="Year", y="Score", hue = "Capitals", markers=True, data = dfm)
            plt.ylabel(None)
            plt.ylim([-5,105])
            plt.legend(ltitle,loc='center left',bbox_to_anchor=(1.1, 0.5),prop={'size': 5})
            plt.show()
            conPlots.pyplot(fig2)
            




def visualizeMap(c1,c2,conPlots):
     global dataColl  
     yearChoice =  st.sidebar.selectbox('Year',sorted(list(years),reverse=True))
     indicator1 = st.sidebar.selectbox('Indicator',all_factors.keys())
     indicator = all_factors[indicator1]
     df = dataColl[yearChoice][indicator]
     df.index = df.index.str.lower()
     
     world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
     world = world[(world.pop_est>0) & (world.name!="Antarctica")] 
     world['name'] = world['name'].str.lower()  
     merged = pd.merge(left = world, right = df, right_on = df.index, left_on = 'name', how = 'left').drop(["pop_est","continent","iso_a3","gdp_md_est"],1)
     print(merged)
     conPlots.write(str.upper(indicator1))
    #  conPlots.write(merged) 
    #  fig, ax = plt.subplots(figsize=(5,2.5))
    # #  ax.legend(fontsize=5,prop={'size': 2})
     gdf = geopandas.GeoDataFrame(merged, geometry="geometry")
     gdf.index = gdf.name
    # #  divider = make_axes_locatable(ax)
    # #  cax = divider.append_axes("right", size="5%", pad=0.1)
    #  gdf.plot(column=indicator, ax=ax, colormap='BuPu',vmin =0, vmax = 100,legend=True,legend_kwds={
    #                     'orientation': "horizontal",'shrink': 0.6, 'aspect':15},edgecolor='black',missing_kwds={
    #     "color": "lightgrey",
    #     "edgecolor": "black",
    #     # "hatch": "///",
    #     "label": "Missing values",
    #  })
    
    #  ax.axis('off')

     fig = px.choropleth(gdf, geojson=gdf.geometry, locations=gdf.index, color=indicator, width = 1200,color_continuous_scale="viridis",range_color=(0, 100),
     hover_name=gdf.index)
     fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
     fig.update_geos(fitbounds="locations", visible=False)
     fig.update_traces(marker_line_width=2)
    #  cb_ax = fig.axes[1] 
    #  cb_ax.tick_params(labelsize=5)


    #  fig.colorbar.lim(0,100)
     conPlots.plotly_chart(fig)






def visualizeOp(op,c1,c2,yearChoice=2020):
    global dataColl
    # countries = dataColl[yearChoice].index
    # global conPlots
    # conPlots.write("The default year is 2020")
    # print(type(yearChoice))
    if(isinstance(yearChoice,list)):
        if(len(yearChoice)==1):
            yearChoice = yearChoice[0]
        else:
            yearChoice=2020
        # if(len(yearChoice)==0):
        #     yearChoice = 2020
        # else:
        #     for i in yearChoice:
        #         dataColl[i] = pd.read_csv(DATA_URL + "\\"+str(i)+'.csv',index_col= 'Country')


    if op=="Country":
        countrySelect = st.sidebar.multiselect('Select Country(ies)',countries)
        print("choice of year = " + str(yearChoice))
        # abc = abc.append(i for i in countrySelect)
        # org_data=pd.read_csv(DATA_URL + "\\"+str(yearChoice)+'.csv',index_col= 'Country')
        org_data=dataColl[yearChoice]
        # df = org_data[countrySelect]
        df = org_data[org_data.index.isin(countrySelect)].transpose()

        showPlot(df,c1,c2)
     
    else:
        indSelect1 = st.sidebar.multiselect('Select indicator(s)',all_factors.keys())
        # trans_data=pd.read_csv(DATA_URL + "\\"+str(yearChoice)+'.csv',index_col= 'Country').transpose()
        indSelect = [all_factors[i] for i in indSelect1]
        print("choice of year = " + str(yearChoice))
        trans_data=dataColl[yearChoice]
        df1 = trans_data[indSelect]
        # print(df1)
        showPlot(df1,c1,c2)
  

def visualizeComp(op,c1,c2,conPlots,choiceDiff):
    global dataColl
    # global conPlots
    # conPlots.write("The default year is 2020")
    # print(type(yearChoice))
    yearChoice = []
    if choiceDiff=="1-year Analysis":
        yearChoice=[2020,2019]
    elif choiceDiff=="5-year Analysis":
        yearChoice=[2020,2015]
    elif choiceDiff == "YTD Analysis":
         yearChoice=[2020,2012]
    else:
        yearChoice=[i for i in range(2012,2021)]

    if op=="Country":
        countrySelect = st.sidebar.multiselect('Select Country(ies)',countries)
        # abc = abc.append(i for i in countrySelect)
        # df = dataColl[yearChoice[0]].subtract(dataColl[yearChoice[1]])[countrySelect]
        df = dataColl[yearChoice[0]].subtract(dataColl[yearChoice[1]])
        df = df[df.index.isin(countrySelect)].transpose()
        # df = org_data[countrySelect]
        showPlot(df,c1,c2,"Comp")
    elif op =="Countryvs":
        countrySelect = st.sidebar.multiselect('Select Country(ies)',countries)
        indexes = ["Score","natural","human","social","financial","manufactured","Year"]
        tempData ={}
        df = pd.DataFrame()
        for i in yearChoice:
            abc = dataColl[i]
            abc["Year"]=i
            tempData[i]=abc
            df =pd.concat([df,tempData[i]])
        # print(df)
        df1= df[indexes]
        linePlot(df1,countrySelect,c1,c2)

    elif op =="Capitals":
        capital = st.sidebar.selectbox("Choose a capital", ["Natural", "Human","Social","Financial","Manufactured"])
        countrySelect = st.sidebar.multiselect('Select Country(ies)',countries)
        indexes=[]
        if capital=="Natural":
            indexes = natural
        elif capital=="Human":
            indexes = human
        elif capital=="Social":
            indexes = social
        elif capital=="Financial":
            indexes = financial
        else:
            indexes = manufactured
        indexes.append("Year")
        # print(indexes)
        tempData ={}
        df = pd.DataFrame()
        # print(yearChoice)
        for i in yearChoice:
            abc = dataColl[i]
            # print(abc)
            abc = abc[abc.index.isin(countrySelect)]
            abc["Year"]=i
            tempData[i]=abc
            df =pd.concat([df,tempData[i]])
        # print(df)
        df1= df[indexes]
        # print(df1)
        # df1 = df1.reset_index()
        # print(df1.index)
        linePlot1(df1,countrySelect,conPlots,capital)

    else:
        indSelect1 = st.sidebar.multiselect('Select indicator(s)',all_factors.keys())
        indSelect = [all_factors[i] for i in indSelect1]
        df1 = dataColl[yearChoice[0]].subtract(dataColl[yearChoice[1]])[indSelect]
        showPlot(df1,c1,c2,"Comp")



def doSA(effect,scale,shock,intensity,duration,c1,c2,country=None):
    global dataColl
    yearChoice = 2020
    if scale=="Global":
        df_effect = effect[shock]
        df1 = dataColl[yearChoice]
        df = df1.transpose()
        print(df)
        data = pd.merge(df_effect,df, left_on = df_effect.index, right_on=df.index, how = "left")
        plot_data = pd.DataFrame()
        plot_data["Country"] = df_effect.index
        # print(data)
        

        for i in df1.index:
            plot_data[i] = data[i] - intensity*duration*data[shock]
        plot_data =plot_data.set_index("Country")
        plot_data[plot_data<0]=0
        
        plot_d = plot_data.T
        print(plot_d)
        plot_d['natural'] = plot_d[natural].mean(axis =1)
        plot_d['human'] = plot_d[human].mean(axis =1)
        plot_d['social'] = plot_d[social].mean(axis =1)
        plot_d['financial'] = plot_d[financial].mean(axis =1)
        plot_d['manufactured'] = plot_d[manufactured].mean(axis =1)
        plot_d['Score'] = np.round(plot_d[['natural','human','social', 'financial','manufactured']].mean(axis =1),1)
        # print(plot_d)
        # df['Score'] = np.round(df.mean(axis=1),1)
        # print('printing df after score')
        # print(df1)

        plot_d['diff'] = np.round(plot_d['Score']-df1['Score'],1)

        print(plot_d)

        

        best_10 = plot_d.sort_values("Score", ascending = False).head(10)
        fig1 = px.bar(best_10, x ="Score" , y = best_10.index,orientation='h', text = "diff")
        fig1.update_layout(xaxis_range=[0,100],yaxis_title=None)
        fig1.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
        fig1.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))
        fig1.update_traces(textposition='outside')
        c1.write("Most Resilient Nations")
        c1.plotly_chart(fig1)

        worst_10 = plot_d.sort_values("Score", ascending = True).head(10)
        fig2 = px.bar(worst_10, x = "Score", y = worst_10.index,orientation='h',text = "diff")
        fig2.update_layout(xaxis_range=[0,100],yaxis_title=None)
        fig2.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
        fig2.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))
        fig2.update_traces(textposition='outside')
        c2.write("Most Vulnerable Nations")
        c2.plotly_chart(fig2)
    elif(scale=="Country"):
        df_effect1 = effect[shock]

        df_effect = df_effect1[df_effect1>0]
        # df_effect = df_effect1[df_effect1>0].sort_values(shock, ascending= False)
        


        df1 = dataColl[yearChoice]

        print("prinding ddf1")

        df = df1[df1.index==country].transpose()
        print(df.transpose().index)
    
        data = pd.merge(df_effect,df, left_on = df_effect.index, right_on=df.index, how = "left")
        print(data)
        plot_data = pd.DataFrame()
        plot_data["Indicator"] = df_effect.index
        print(plot_data)

        

        for i in df.transpose().index:
            plot_data[i] = data[i] - intensity*duration*data[shock]
        plot_data =plot_data.set_index("Indicator")
        # plot_data[plot_data<0]=0

        plot_d = plot_data
        plot_d["var_name"] = [all_factors1[i] for i in plot_d.index]
        print(plot_d)
        # print(plot_data.sort_values(country, ascending=False))
        # plot_d['natural'] = plot_d[natural].mean(axis =1)
        # plot_d['human'] = plot_d[human].mean(axis =1)
        # plot_d['social'] = plot_d[social].mean(axis =1)
        # plot_d['financial'] = plot_d[financial].mean(axis =1)
        # plot_d['manufactured'] = plot_d[manufactured].mean(axis =1)
        # plot_d['Score'] = np.round(plot_d[['natural','human','social', 'financial','manufactured']].mean(axis =1),1)
        # print(plot_d)
        plot_d['diff'] = np.round(plot_d[country]-df[country],1)
        best_10 = plot_d[plot_d[country]>0].sort_values(country, ascending = False).head(10)
        # fig1 = px.bar(best_10, x =country , y = best_10.index,orientation='h')
        fig1 = px.bar(best_10, x =country , y = "var_name",orientation='h',text = "diff")
        fig1.update_layout(xaxis_range=[0,110],yaxis_title=None)
        fig1.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
        fig1.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))
        fig1.update_traces(textposition='outside')
        c1.write("Most Resilient Indicators")
        # c1.write(country)
        c1.plotly_chart(fig1)

        worst_10 = plot_d[plot_d[country]>0].sort_values(country, ascending = True).head(10)
        # fig2 = px.bar(worst_10, x = country, y = worst_10.index,orientation='h')
        fig2 = px.bar(worst_10, x = country, y = "var_name",orientation='h',text = "diff")
        fig2.update_layout(xaxis_range=[0,110],yaxis_title=None)
        fig2.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
        fig2.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))
        fig2.update_traces(textposition='outside')
        c2.write("Most Vulnerable Indicators")
        # c2.write(country)
        c2.plotly_chart(fig2)
      
        # print(plot_data)
        
        # plot_d = plot_data.T
        # print(plot_d)
        # plot_d['natural'] = plot_d[natural].mean(axis =1)
        # plot_d['human'] = plot_d[human].mean(axis =1)
        # plot_d['social'] = plot_d[social].mean(axis =1)
        # plot_d['financial'] = plot_d[financial].mean(axis =1)
        # plot_d['manufactured'] = plot_d[manufactured].mean(axis =1)
        # plot_d['Score'] = np.round(plot_d[['natural','human','social', 'financial','manufactured']].mean(axis =1),1)
        # print(plot_d)

        # best_10 = plot_d.sort_values("Score", ascending = False).head(10)
        # fig1 = px.bar(best_10, x ="Score" , y = best_10.index,orientation='h')
        # fig1.update_layout(xaxis_range=[0,100],yaxis_title=None)
        # c1.write("Most Resilient Nations")
        # c1.plotly_chart(fig1)

        # worst_10 = plot_d.sort_values("Score", ascending = True).head(10)
        # fig2 = px.bar(worst_10, x = "Score", y = worst_10.index,orientation='h')
        # fig2.update_layout(xaxis_range=[0,100],yaxis_title=None)
        # c2.write("Most Vulnerable Nations")
        # c2.plotly_chart(fig2)
    
    else:
        print("nth")



###### SIDEBAR *****************




# countries = org_data.drop('Indicator',1).columns
countries = org_data.index

st.sidebar.image("icon.png",width =150)
st.sidebar.title('Control Center')
# st.sidebar.markdown('Control Parameters Here')
# st.sidebar.checkbox("Select a Country", True, key=1)

analysisType = st.sidebar.radio(
     "Visualization By:",
     ('World Map','Descriptive Analysis', 'Comparative Analysis','Scenario Analysis',"Best Interventions"))
print(analysisType)


conPlots = st.container()
col1, col2 = conPlots.columns((0.85,1))

conSliders = st.container()

# global c1,c2

c1,c2 = conSliders.columns(2)

if(analysisType=="World Map"):
    visualizeMap(c1,c2,conPlots)    



elif(analysisType=="Descriptive Analysis"):
    c1.markdown('__STRENGTHS__')
    c2.markdown('__WEAKNESSES__')
    yearChoice =  st.sidebar.selectbox('Select Year(s)',sorted(list(years),reverse=True))
    print(type(yearChoice))
    op =showOption()
    # if len(yearChoice)==0:
    #     # conPlots.write("If the year is empty, the default year is 2020")
    #     visualizeOp(op,c1,c2)
    # else:
    #     visualizeOp(op,c1,c2,yearChoice)
    visualizeOp(op,c1,c2,yearChoice)


elif(analysisType=="Comparative Analysis"):
    
    choiceDiff =  st.sidebar.selectbox('Select a type',["1-year Analysis","5-Year Analysis", "YTD Analysis", "Country vs Country", "Capitals"])
    if choiceDiff in ["1-year Analysis","5-Year Analysis", "YTD Analysis",]:
        op =showOption()
    elif choiceDiff== "Country vs Country":
        op = "Countryvs"
    else:
        op = choiceDiff
    visualizeComp(op,c1,c2,conPlots,choiceDiff)


elif((analysisType=="Scenario Analysis")):
    effect = pd.read_csv('effect1.csv', index_col = "Variables")
    scale = st.sidebar.selectbox('Select a scale',["Global","Country"])
    country=None
    if (scale=="Country"):
        country = st.sidebar.selectbox('Select a country',countries)
        conPlots.write(country)
    shock = st.sidebar.selectbox('Select a shock',["Flood","Drought", "Storm", "Pandemic", "Civil War", "Economic Crisis","Earthquake"])
    intensity = st.sidebar.slider('Intensity of Shock', min_value = 0, max_value = 10,value = 0)
    duration = st.sidebar.slider('Duration of Shock', min_value = 1, max_value = 10,value = 0)
    
    doSA(effect,scale,shock,intensity,duration,c1,c2,country)
    # st.markdown("# _Page will be up and running soon.... Hang on!!!_")

else:
    # st.markdown("# _Page will be up and running soon.... Hang on!!!_")
    shock = st.sidebar.selectbox('Select a shock',["Flood","Drought", "Storm", "Pandemic", "Civil War", "Economic Crisis","Earthquake"])
    intensity = st.sidebar.slider('Intensity of Shock', min_value = 0, max_value = 10,value = 0)
    duration = st.sidebar.slider('Duration of Shock in days', min_value = 1, max_value = 120,value = 0)
    co1, co2,co3 = conPlots.columns(3)
    fig1 = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = np.round(np.random.rand(),2)*100,
    mode = "gauge+number",
    number ={'suffix': "%"},
    title = {'text': "Intervention 1"},
   # delta = {'reference': 380},
    gauge = {'axis': {'range': [None, 100]},
             'steps' : [
                 {'range': [0, 25], 'color': "lightgray"},
                 {'range': [25, 50], 'color': "gray"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.8, 'value': 100}}))
    fig1.update_layout(width=500)
    fig2 = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = np.round(np.random.rand(),2)*100,
    mode = "gauge+number",
    number ={'suffix': "%"},
    title = {'text': "Intervention 2"},
   # delta = {'reference': 380},
    gauge = {'axis': {'range': [None, 100]},
             'steps' : [
                 {'range': [0, 25], 'color': "lightgray"},
                 {'range': [25, 50], 'color': "gray"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.8, 'value': 100}}))    

    fig3 = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = np.round(np.random.rand(),2)*100,
    mode = "gauge+number",
    number ={'suffix': "%"},
    title = {'text': "Intervention 3"},
   # delta = {'reference': 380},
    gauge = {'axis': {'range': [None, 100]},
             'steps' : [
                 {'range': [0, 25], 'color': "lightgray"},
                 {'range': [25, 50], 'color': "gray"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.8, 'value': 100}}))   
    fig1.update_layout(width=500) 
    fig2.update_layout(width=500)  
    fig3.update_layout(width=500) 
    co1.plotly_chart(fig1)
    co2.plotly_chart(fig2)
    co3.plotly_chart(fig3)

    

expander = st.expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")
