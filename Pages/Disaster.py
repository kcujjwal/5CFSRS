import streamlit as st
import pandas as pd
import plotly.express as px
import geopandas
import numpy as np

damages = {
    'Drought': [1,4,7,10,12.36,13.83,14.62,15.24,15.59,16.33],
    'Earthquake':[1,6,10,12.39,13.34,14.24,15.12,15.82,16.18,16.79],
    'Flood':[1,5,10,12.54,14.94,15.79,16.12,16.63,17.04,17.58],
    'Landslide':[1,2.5,4,5.5,7,8.5,9.12,11.24,12.26,13.69],
    'Storm':[1,8,11.9,13.3,13.99,15.45,15.93,16.49,17.17,17.93],
    'Volcanic Activity':[1,2,3,4,5,6,7,9.5,11.39,13.09],
    'Wildfire':[1,4,7,8.46,11.77,12.96,13.94,14.61,15.19,15.89],
    'Economic Crises':[1,3,5,7,9,11,13,15,17,19,21]
    # 'Political Conflict':[1,3,5,7,9,11,13,15,17,19,21]
}
countries = ['Algeria', 'Angola', 'Argentina', 'Australia', 'Austria', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Belarus', 'Belgium', 'Benin', 'Bolivia', 'Botswana', 'Brazil', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Chad', 'Chile', 'China', 'Colombia', 'Costa Rica', 'Czech Republic', 'DR Congo', 'Denmark', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Ethiopia', 'Finland', 'France', 'Germany', 'Ghana', 'Greece', 'Guatemala', 'Guinea', 'Haiti', 'Honduras', 'Hungary', 'India', 'Indonesia', 'Ireland', 'Israel', 'Italy', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kuwait', 'Madagascar', 'Malawi', 'Malaysia', 'Mali', 'Mexico', 'Morocco', 'Mozambique', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Panama', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saudi Arabia', 'Senegal', 'Serbia', 'Sierra Leone', 'Singapore', 'South Africa', 'South Korea', 'Spain', 'Sudan', 'Sweden', 'Switzerland', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tunisia', 'Turkey', 'Uganda', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan']
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world = world[(world.pop_est>0) & (world.name!="Antarctica")].drop(columns =["pop_est","continent","iso_a3","gdp_md_est"])
world['name'] = world['name'].str.lower() 

flags = {
   'Afghanistan': 'af', 'Albania': 'al', 'Algeria': 'dz', 'American Samoa': 'as', 'Andorra': 'ad', 'Angola': 'ao', 'Anguilla': 'ai', 'Antarctica': 'aq', 'Antigua and Barbuda': 'ag', 'Argentina': 'ar', 'Armenia': 'am', 'Aruba': 'aw', 'Australia': 'au', 'Austria': 'at', 'Azerbaijan': 'az', 'Bahamas': 'bs', 'Bahrain': 'bh', 'Bangladesh': 'bd', 'Barbados': 'bb', 'Belarus': 'by', 'Belgium': 'be', 'Belize': 'bz', 'Benin': 'bj', 'Bermuda': 'bm', 'Bhutan': 'bt', 'Bolivia, Plurinational State of': 'bo', 'Bolivia': 'bo', 'Bosnia and Herzegovina': 'ba', 'Botswana': 'bw', 'Bouvet Island': 'bv', 'Brazil': 'br', 'British Indian Ocean Territory': 'io', 'Brunei Darussalam': 'bn', 'Brunei': 'bn', 'Bulgaria': 'bg', 'Burkina Faso': 'bf', 'Burundi': 'bi', 'Cambodia': 'kh', 'Cameroon': 'cm', 'Canada': 'ca', 'Cape Verde': 'cv', 'Cayman Islands': 'ky', 'Central African Republic': 'cf', 'Chad': 'td', 'Chile': 'cl', 'China': 'cn', 'Christmas Island': 'cx', 'Cocos (Keeling) Islands': 'cc', 'Colombia': 'co', 'Comoros': 'km', 'Congo': 'cg', 'Congo, the Democratic Republic of the': 'cd', 'Cook Islands': 'ck', 'Costa Rica': 'cr', "Côte d'Ivoire": 'ci', 'Ivory Coast': 'ci', 'Croatia': 'hr', 'Cuba': 'cu', 'Cyprus': 'cy', 'Czech Republic': 'cz', 'Denmark': 'dk', 'Djibouti': 'dj', 'Dominica': 'dm', 'Dominican Republic': 'do', 'Ecuador': 'ec', 'Egypt': 'eg', 'El Salvador': 'sv', 'Equatorial Guinea': 'gq', 'Eritrea': 'er', 'Estonia': 'ee', 'Ethiopia': 'et', 'Falkland Islands (Malvinas)': 'fk', 'Faroe Islands': 'fo', 'Fiji': 'fj', 'Finland': 'fi', 'France': 'fr', 'French Guiana': 'gf', 'French Polynesia': 'pf', 'French Southern Territories': 'tf', 'Gabon': 'ga', 'Gambia': 'gm', 'Georgia': 'ge', 'Germany': 'de', 'Ghana': 'gh', 'Gibraltar': 'gi', 'Greece': 'gr', 'Greenland': 'gl', 'Grenada': 'gd', 'Guadeloupe': 'gp', 'Guam': 'gu', 'Guatemala': 'gt', 'Guernsey': 'gg', 'Guinea': 'gn', 'Guinea-Bissau': 'gw', 'Guyana': 'gy', 'Haiti': 'ht', 'Heard Island and McDonald Islands': 'hm', 'Holy See (Vatican City State)': 'va', 'Honduras': 'hn', 'Hong Kong': 'hk', 'Hungary': 'hu', 'Iceland': 'is', 'India': 'in', 'Indonesia': 'id', 'Iran, Islamic Republic of': 'ir', 'Iraq': 'iq', 'Ireland': 'ie', 'Isle of Man': 'im', 'Israel': 'il', 'Italy': 'it', 'Jamaica': 'jm', 'Japan': 'jp', 'Jersey': 'je', 'Jordan': 'jo', 'Kazakhstan': 'kz', 'Kenya': 'ke', 'Kiribati': 'ki', "Korea, Democratic People's Republic of": 'kp', 'Korea, Republic of': 'kr', 'South Korea': 'kr', 'Kuwait': 'kw', 'Kyrgyzstan': 'kg', "Lao People's Democratic Republic": 'la', 'Latvia': 'lv', 'Lebanon': 'lb', 'Lesotho': 'ls', 'Liberia': 'lr', 'Libyan Arab Jamahiriya': 'ly', 'Libya': 'ly', 'Liechtenstein': 'li', 'Lithuania': 'lt', 'Luxembourg': 'lu', 'Macao': 'mo', 'Macedonia, the former Yugoslav Republic of': 'mk', 'Madagascar': 'mg', 'Malawi': 'mw', 'Malaysia': 'my', 'Maldives': 'mv', 'Mali': 'ml', 'Malta': 'mt', 'Marshall Islands': 'mh', 'Martinique': 'mq', 'Mauritania': 'mr', 'Mauritius': 'mu', 'Mayotte': 'yt', 'Mexico': 'mx', 'Micronesia, Federated States of': 'fm', 'Moldova, Republic of': 'md', 'Monaco': 'mc', 'Mongolia': 'mn', 'Montenegro': 'me', 'Montserrat': 'ms', 'Morocco': 'ma', 'Mozambique': 'mz', 'Myanmar': 'mm', 'Burma': 'mm', 'Namibia': 'na', 'Nauru': 'nr', 'Nepal': 'np', 'Netherlands': 'nl', 'Netherlands Antilles': 'an', 'New Caledonia': 'nc', 'New Zealand': 'nz', 'Nicaragua': 'ni', 'Niger': 'ne', 'Nigeria': 'ng', 'Niue': 'nu', 'Norfolk Island': 'nf', 'Northern Mariana Islands': 'mp', 'Norway': 'no', 'Oman': 'om', 'Pakistan': 'pk', 'Palau': 'pw', 'Palestinian Territory, Occupied': 'ps', 'Panama': 'pa', 'Papua New Guinea': 'pg', 'Paraguay': 'py', 'Peru': 'pe', 'Philippines': 'ph', 'Pitcairn': 'pn', 'Poland': 'pl', 'Portugal': 'pt', 'Puerto Rico': 'pr', 'Qatar': 'qa', 'Réunion': 're', 'Romania': 'ro', 'Russian Federation': 'ru', 'Russia': 'ru', 'Rwanda': 'rw', 'Saint Helena, Ascension and Tristan da Cunha': 'sh', 'Saint Kitts and Nevis': 'kn', 'Saint Lucia': 'lc', 'Saint Pierre and Miquelon': 'pm', 'Saint Vincent and the Grenadines': 'vc', 'Saint Vincent & the Grenadines': 'vc', 'St. Vincent and the Grenadines': 'vc', 'Samoa': 'ws', 'San Marino': 'sm', 'Sao Tome and Principe': 'st', 'Saudi Arabia': 'sa', 'Senegal': 'sn', 'Serbia': 'rs', 'Seychelles': 'sc', 'Sierra Leone': 'sl', 'Singapore': 'sg', 'Slovakia': 'sk', 'Slovenia': 'si', 'Solomon Islands': 'sb', 'Somalia': 'so', 'South Africa': 'za', 'South Georgia and the South Sandwich Islands': 'gs', 'South Sudan': 'ss', 'Spain': 'es', 'Sri Lanka': 'lk', 'Sudan': 'sd', 'Suriname': 'sr', 'Svalbard and Jan Mayen': 'sj', 'Swaziland': 'sz', 'Sweden': 'se', 'Switzerland': 'ch', 'Syrian Arab Republic': 'sy', 'Taiwan, Province of China': 'tw', 'Taiwan': 'tw', 'Tajikistan': 'tj', 'Tanzania': 'tz', 'Thailand': 'th', 'Timor-Leste': 'tl', 'Togo': 'tg', 'Tokelau': 'tk', 'Tonga': 'to', 'Trinidad and Tobago': 'tt', 'Tunisia': 'tn', 'Turkey': 'tr', 'Turkmenistan': 'tm', 'Turks and Caicos Islands': 'tc', 'Tuvalu': 'tv', 'Uganda': 'ug', 'Ukraine': 'ua', 'United Arab Emirates': 'ae', 'United Kingdom': 'gb', 'United States': 'us', 'United States Minor Outlying Islands': 'um', 'Uruguay': 'uy', 'Uzbekistan': 'uz', 'Vanuatu': 'vu', 'Venezuela, Bolivarian Republic of': 've', 'Venezuela': 've', 'Viet Nam': 'vn', 'Vietnam': 'vn', 'Virgin Islands, British': 'vg', 'Virgin Islands, U.S.': 'vi', 'Wallis and Futuna': 'wf', 'Western Sahara': 'eh', 'Yemen': 'ye', 'Zambia': 'zm', 'Zimbabwe': 'zw'
   }
# alldata1 = pd.read_csv("restructure.csv")


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


    #  fig = px.choropleth(gdf, geojson=gdf.geometry, locations=gdf.index, color="Value", width = 1000,color_continuous_scale="RdYlGn",range_color=(0, 100),
    #  hover_name=gdf.index,animation_frame="Year")
     fig = px.choropleth(gdf, geojson=gdf.geometry, locations=gdf.index, color="Value", width = 1000,color_continuous_scale="RdYlGn_r",
     hover_name=gdf.index)
     fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
     fig.update_geos(fitbounds="locations", visible=False)
     fig.update_traces(marker_line_width=2)
    #  cb_ax = fig.axes[1] 
    #  cb_ax.tick_params(labelsize=5)


    #  fig.colorbar.lim(0,100)
     st.plotly_chart(fig)
# @st.cache(suppress_st_warning=True)


def app():
    df = pd.read_csv("alldisaster.csv")
    years_df = df['Year'].unique()
    low = min(years_df)
    high = max(years_df)
    print(low,high)
    scale = st.sidebar.selectbox('Select a scale',["Global","Country"])
    country=None
    
    # shock = st.sidebar.selectbox('Select a shock',damages.keys())
    # # intensity_score = st.sidebar.slider('Enter the shock intensity', min_value=0,max_value=10,value=0)
    # ranger = st.sidebar.slider('Choose the range!', min_value=int(low),max_value=int(high),value=(2000,2022))
    # # print(intensity_score,ranger)
    # df = df[(df["Year"]>=ranger[0]) & (df["Year"]<=ranger[1])]
    # print(df.head())

    if (scale=="Global"):
      shock = st.sidebar.selectbox('Select a shock',damages.keys())
      choice = st.sidebar.selectbox("Choose a Disaster Impact",["Deaths","Total Affected","Economic Damages"])
      # intensity_score = st.sidebar.slider('Enter the shock intensity', min_value=0,max_value=10,value=0)
      ranger = st.sidebar.slider('Choose the range!', min_value=int(low),max_value=int(high),value=(2000,2022))
      # print(intensity_score,ranger)
      df = df[(df["Year"]>=ranger[0]) & (df["Year"]<=ranger[1])]
      print(df.head())
      df = df[df["Disaster Type"]==shock]
      fd = df.groupby(["Country","Disaster Type"])[["Total Deaths_new","Total Affected_new", "AdjustedDamages_new"]].sum().reset_index()
      print(fd)
      
      if choice=="Deaths":
        df1 = fd[["Country","Disaster Type","Total Deaths_new"]]
      elif choice=="Total Affected":
        df1 = fd[["Country","Disaster Type","Total Affected_new"]]
      else:
        df1 = fd[["Country","Disaster Type","AdjustedDamages_new"]]
      print(df1)

      df1["Country"]=df1["Country"].str.lower()
      # df["Year"] = df["Year"].astype("int")
      merged = pd.merge(left = world, right = df1, right_on = "Country", left_on = 'name', how = 'left')

      gdf = geopandas.GeoDataFrame(merged, geometry="geometry").dropna()
      # print(gdf.head())

      
      gdf.index = gdf.name
      gdf = gdf.rename(columns = {gdf.columns[4]:"Value"})
      print(gdf.head())
      # gdf["Year"]=gdf["Year"].astype("int")
      st.subheader(str.upper(choice))
      visualizeMap1(gdf)


    else:
        country = st.sidebar.selectbox('Select a country',countries)
        df = df[df["Country"]==country]
        d1,d2 = st.columns([1,10])
        d1.image("Con_Flags/"+flags[country]+".png",width=50)
        d2.subheader(str.upper(country))
        ranger = st.sidebar.slider('Choose the range!', min_value=int(low),max_value=int(high),value=(2000,2022))
        df = df[(df["Year"]>=ranger[0]) & (df["Year"]<=ranger[1])]
        print(df.head())

        fd = df.groupby(["Country","Disaster Type"])[["Total Deaths_new","Total Affected_new", "AdjustedDamages_new"]].sum()
        fd = fd.assign(intensity=lambda x: x[['Total Deaths_new','Total Affected_new','AdjustedDamages_new']].mean(axis=1)).reset_index()
        fd = fd[["Country","Disaster Type","intensity"]]

        # fd = fd["intensity"].apply(np.round)
        

        fd["intensity"] = fd["intensity"].apply(np.ceil)
        print(fd.head())
        fig3 = px.bar(fd.sort_values(by="intensity",ascending=False), x ="Disaster Type" , y = 'intensity',orientation='v',text = 'intensity')
        fig3.update_layout(yaxis_range=[0,max(fd['intensity'])+3],yaxis_title='Standardized Impact Score',xaxis_title=None, font = dict(
                size =18,
        )
        )
        fig3.update_xaxes(tickfont=dict(size =15, family = "Arial Black"))
        fig3.update_yaxes(tickfont=dict(size =15,family = "Arial Black"))
        fig3.update_traces(textposition='outside')
        st.subheader("Impacts of Food Shocks")
        st.plotly_chart(fig3)
        # conPlots.write(country)

    # print(alldata1)
    # df = alldata1.copy()
    # indicator1 = st.sidebar.selectbox('Indicator',all_factors.keys())
    # print(indicator1)
    # indicator = all_factors[indicator1]
    # df = df[["Year","Country",'Indicator',"Value"]][df["Indicator"]==indicator1]
    # df["Country"]=df["Country"].str.lower()
    # df["Year"] = df["Year"].astype("int")
    # merged = pd.merge(left = world, right = df, right_on = "Country", left_on = 'name', how = 'left')

    # gdf = geopandas.GeoDataFrame(merged, geometry="geometry").dropna()

    # print(gdf.head())
    # gdf.index = gdf.name
    # gdf["Year"]=gdf["Year"].astype("int")
    # st.subheader(str.upper(indicator1))
    # visualizeMap1(gdf)
    
