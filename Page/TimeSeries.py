import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


plt_style = 'bmh'
natural = ['BDH.new', 'ECS', 'Sealevel', 'Forest', 'Land', 'energy', 'Water', 'GHP.new', 'WaterQuant', 'WaterQual']
human = ['Demographics', 'literacy', 'HDI', 'labrate', 'agprod', 'agVol', 'obesity', 'foodsafe', 'drinking', 'Micro', 'Protein', 'Diversity']
social = ['urbancap', 'safetynet', 'policyfood', 'nutritional', 'gender', 'political', 'corruption', 'conflict']
financial = ['perCapita', 'edu', 'tariff', 'agGDP', 'finance', 'priceVol', 'foodloss']
manufactured = ['kofgi', 'agadaptpolicy', 'climatesma', 'disman', 'Nindex', 'RND', 'mobile', 'transport', 'storage']

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

natural1 = [all_factors1[i] for i in ['BDH.new', 'ECS', 'Sealevel', 'Forest', 'Land', 'energy', 'Water', 'GHP.new', 'WaterQuant', 'WaterQual']]
human1 = [all_factors1[i] for i in ['Demographics', 'literacy', 'HDI', 'labrate', 'agprod', 'agVol', 'obesity', 'foodsafe', 'drinking', 'Micro', 'Protein', 'Diversity']]
social1 = [all_factors1[i] for i in ['urbancap', 'safetynet', 'policyfood', 'nutritional', 'gender', 'political', 'corruption', 'conflict']]
financial1 = [all_factors1[i] for i in ['perCapita', 'edu', 'tariff', 'agGDP', 'finance', 'priceVol', 'foodloss']]
manufactured1 = [all_factors1[i] for i in ['kofgi', 'agadaptpolicy', 'climatesma', 'disman', 'Nindex', 'RND', 'mobile', 'transport', 'storage']]

capitals = ['Score','natural','human','social','financial','manufactured']

dataColl = {}
years = range(2012,2021)
for i in years:
    abc = pd.read_csv(str(i)+'.csv',index_col= 'Country').transpose()
    # dataColl[i] = pd.read_csv(DATA_URL + "\\"+str(i)+'.csv',index_col= 'Country')
    dataColl[i] = abc
# org_data=pd.read_csv(DATA_URL + "\\"+str(2012)+'.csv',index_col= 'Country')
org_data=dataColl[2020]
trans_data = org_data.transpose()
countries = org_data.index


def showOption():
    opts = ['Country','Indicator']
    op = st.sidebar.selectbox('Analysis by:',opts)
    return op


def linePlot1(df,countrySelect,capital):
    
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
    
    print(ltitle)

    if(len(countrySelect)!=0):
        for i in countrySelect:
            df1=df[df.index==i]
            print(df1)
            st.subheader(str.upper(i))
        


            fig2,axs = plt.subplots(figsize=(6,2.5))
            # fig2,axs = plt.subplots()
            
                    
            plt.style.use(plt_style)

            dfm =df1.melt('Year',var_name="Capitals",value_name="Score")
            sns.lineplot(x="Year", y="Score", hue = "Capitals", markers=True, data = dfm)
            plt.ylabel(None)
            plt.ylim([-5,105])
            plt.legend(ltitle,loc='center left',bbox_to_anchor=(1.1, 0.5),prop={'size': 5})
            plt.show()
            st.pyplot(fig2)

def linePlot(df,countrySelect):
    df.index.name=None
    # c1.write(df)
    c1,c2 = st.columns(2)
    if(len(countrySelect)!=0):
        df =df[df.index.isin(countrySelect)]
        check = df.reset_index().set_index("Year")
        print(check)
        # c1.write(df)
        plt.style.use(plt_style)
        for i in range(int(len(df.columns)/2)):

            if(df.columns[2*i] in all_factors1.keys()):
        
                c1.subheader(str.upper(all_factors1[df.columns[2*i]]))


            fig,axs = plt.subplots(figsize=(6,4))

            df.reset_index().set_index("Year").groupby("index")[df.columns[2*i]].plot(legend = True,style='.-')

            plt.ylim([0,100])
            plt.legend(loc='lower left')
            # plt.show()
            c1.pyplot(fig)

            # c2.write(str.upper(df.columns[2*i+1]))
            c2.subheader(str.upper(all_factors1[df.columns[2*i+1]]))
            # c2.write(df[i].sort_values(ascending= True).head(10))
            fig1,axs1 = plt.subplots(figsize=(6,4))
            plt.style.use(plt_style)
            # c1.write(df[i].sort_values(ascending= False).head(10))
            df.reset_index().set_index("Year").groupby("index")[df.columns[2*i+1]].plot(legend = True,style='.-')
            plt.ylim([0,100])
            plt.legend(loc='lower left')
            # plt.show()
            c2.pyplot(fig1)

         
def visualizeComp(op,choiceDiff):
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
        original = dataColl[yearChoice[0]][dataColl[yearChoice[0]].index.isin(countrySelect)].transpose()
        # df = org_data[countrySelect]
        print('*****')
        print(original.head())
        showPlot(df,"Comp","indx",present = original)
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
        linePlot(df1,countrySelect)

    elif op =="Capitals":
        indexes=[]
        capital = st.sidebar.selectbox("Choose a capital", ["Natural", "Human","Social","Financial","Manufactured"])
        countrySelect = st.sidebar.multiselect('Select Country(ies)',countries)
        
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
        if "Year" not in indexes:
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
        linePlot1(df1,countrySelect,capital)

    else:
        indSelect1 = st.sidebar.multiselect('Select indicator(s)',all_factors.keys())
        indSelect = [all_factors[i] for i in indSelect1]
        df1 = dataColl[yearChoice[0]].subtract(dataColl[yearChoice[1]])[indSelect]
        print(df1)
        showPlot(df1,index="country",visType="Comp")

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


def app():
    choiceDiff =  st.sidebar.selectbox('Select a type',["1-year Analysis","5-Year Analysis", "YTD Analysis", "Country vs Country", "Capitals"])
    if choiceDiff in ["1-year Analysis","5-Year Analysis", "YTD Analysis"]:
        op =showOption()
    elif choiceDiff== "Country vs Country":
        op = "Countryvs"
    else:
        op = choiceDiff
    visualizeComp(op,choiceDiff)
