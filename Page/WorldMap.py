import streamlit as st
import geopandas
import pandas as pd
import plotly.express as px

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

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world = world[(world.pop_est>0) & (world.name!="Antarctica")].drop(columns =["pop_est","continent","iso_a3","gdp_md_est"])
world['name'] = world['name'].str.lower() 

alldata1 = pd.read_csv("restructure.csv")


# print(df.head())
# # visualizeMap(c1,c2,conPlots)    
# indicator1 = st.sidebar.selectbox('Indicator',all_factors.keys())
# indicator = all_factors[indicator1]
# df = df[["Year","Country",'Indicator',"Value"]][df["Indicator"]==indicator1]
# print(df.head())

# df["Country"]=df["Country"].str.lower()
# df["Year"] = df["Year"].astype("int")
# # world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
# # world = world[(world.pop_est>0) & (world.name!="Antarctica")] 
# # world['name'] = world['name'].str.lower()  
# # merged = pd.merge(left = world, right = df, right_on = "Country", left_on = 'name', how = 'left').drop(columns =["pop_est","continent","iso_a3","gdp_md_est"])
# merged = pd.merge(left = world, right = df, right_on = "Country", left_on = 'name', how = 'left')

# gdf = geopandas.GeoDataFrame(merged, geometry="geometry").dropna()

# print(gdf.head())
# gdf.index = gdf.name
# gdf["Year"]=gdf["Year"].astype("int")
# conPlots.subheader(str.upper(indicator1))
# visualizeMap1(gdf,conPlots)

# @st.cache(suppress_st_warning=True)
def visualizeMap1(gdf):


     fig = px.choropleth(gdf, geojson=gdf.geometry, locations=gdf.index, color="Value", width = 1000,color_continuous_scale="Viridis",range_color=(0, 100),
     hover_name=gdf.index,animation_frame="Year")
     fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
     fig.update_geos(fitbounds="locations", visible=False)
     fig.update_traces(marker_line_width=2)
    #  cb_ax = fig.axes[1] 
    #  cb_ax.tick_params(labelsize=5)


    #  fig.colorbar.lim(0,100)
     st.plotly_chart(fig)
# @st.cache(suppress_st_warning=True)
def app():
    print(alldata1)
    df = alldata1.copy()
    indicator1 = st.sidebar.selectbox('Indicator',all_factors.keys())
    print(indicator1)
    indicator = all_factors[indicator1]
    df = df[["Year","Country",'Indicator',"Value"]][df["Indicator"]==indicator1]
    df["Country"]=df["Country"].str.lower()
    df["Year"] = df["Year"].astype("int")
    merged = pd.merge(left = world, right = df, right_on = "Country", left_on = 'name', how = 'left')

    gdf = geopandas.GeoDataFrame(merged, geometry="geometry").dropna()

    print(gdf.head())
    gdf.index = gdf.name
    gdf["Year"]=gdf["Year"].astype("int")
    st.subheader(str.upper(indicator1))
    visualizeMap1(gdf)
    
