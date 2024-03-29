import streamlit as st



def app():
    abc = """**Food Systems Resilience Diagnostics Tool**

**Abstract**

The food system is a complex web of actors/agents and interactions that spans production to the consumption of food. The global food system has been severely disrupted by the COVID-19 pandemic putting millions of people at risk of hunger and malnutrition. In a post-COVID-19 era, a stock-take will be required to see how our food system changed in response to current drivers/pressures and what lessons we learnt regarding the actions required to improve its resilience. The ability to understand, interpret, evaluate, and monitor key aspects of the food system is pivotal in building resilient food systems, as it is through this collection and analysis of information that we can improve resource allocation and effective decision-making. Thus, we present a diagnostic tool that can identify and monitor food stress using a food system resilience score. This score is derived from several indicators that describe natural, human, social, financial, and manufactured dimensions of the food system. The tool incorporates three major functionalities - situational awareness, scenario analysis, and intervention analysis. The situational awareness component helps derive a clear understanding of the strengths and weaknesses of food systems, while the scenario analysis component enables the anticipation of how various aspects within food systems may change when exposed to food shocks. The intervention analysis component points out the most effective and realistic interventions against anticipated food shocks. We have constructed the tool so that it can be deployed at various levels to enable better-informed decision-making toward building resilient food systems in the long term.

**A. Using the tool**

**1. About**

This page displays the basic information about the tools with its components. The components of the tool offer different functionalities for food system resilience diagnostics.

**2. Components/Functionalities**


**2.1 World Map**

This component generates color-coded world map based on the value of the indicator chosen in the Control Center. You can also customize the world map for year.


**2.2 Diagnostics**

This component summarizes the strengths and weaknesses of a national food system when the analysis is chosen by “Country”. When the analysis is chosen by “Indicator”, the component lists the best performing and the worst performing countries for the chosen indicator(s). The visualizations can also be customized for analysis years and multiple selections of countries and indicators.

**2.3 Time-Series Analysis**

This component facilitates comparisons of performance of national food systems at a temporal scale. The visualizations in this component can be chosen by either “Country” or “Indicator”. The visualizations also allow for multiple selections of countries and indicators. Five different types of analyses are available in the component.

**1-year Analysis:** It draws a picture of the current strengths and weaknesses of a national food system when the analysis is chosen by “Country” and the current best performing and worst performing countries when the analysis is chosen by “Indicator” compared to that in the previous year.

**5-year Analysis:** It draws a picture of the current strengths and weaknesses of a national food system when the analysis is chosen by “Country” and the current best performing and worst performing countries when the analysis is chosen by “Indicator” compared to the statistics five years ago.

**YTD Analysis:** It draws a picture of the current strengths and weaknesses of a national food system when the analysis is chosen by “Country” and the current best performing and worst performing countries when the analysis is chosen by “Indicator” compared to the earliest statistics (2012).

**Country vs Country:** It directly compares a country against other and shows how the scores of the countries in five capitals including overall food system resilience have changed at a temporal scale.
Capitals: It displays the performance of chosen countries for all indicators within the selected capital at a temporal scale.


**2.4 Disaster Vulnerability**

This component represents the vulnerability of countries to several forms of hazards. When the chosen scale is "Global", the component generates a color-coded world map based on the standardized values of either total deaths, total affected, or total economic damages. For the country scale, the component generates a chart that shows the standardized mean impact of several hazards for the chosen country.

**3. Five Capitals based framework for food system resilience assessment**

**The five capitals approach provides a holistic way to measure value.**

**Table 1: Categorization of the variables under five capitals**

| Capitals                       | Capitals categories           | Variables                             |
|--------------------------------|-------------------------------|---------------------------------------|
| **Natural**                    |                               |                                       |
| Biodiversity                   | Biodiversity                  | Biodiversity Status                   |
| Air quality                    |                               | Ecosystem                             |
| Water quality                  |                               | Forest Area                           |
| Land quality                   | Air quality                   | GHGE per capita                       |
|                                | Water quality                 | Water availability                    |
|                                |                               | Water quality                         |
|                                |                               | Water footprint                       |
|                                | Land quality                  | Total Arable land per capita          |
|                                |                               | Land degradation per arable land      |
|                                |                               |                                       |
| **Human**                      |                               |                                       |
| Wellbeing                      | Wellbeing                     | Obesity                               |
| Skills and training            |                               | Undernourishment                      |
|                                |                               | Foodborne diseases burden             |
|                                |                               | Drinking Water                        |
|                                |                               | Micronutrient Availability            |
|                                |                               | Protein availability                  |
|                                |                               | Food diversity                        |
|                                | Skills and Training           | Literacy rate                         |
|                                |                               | HDI                                   |
|                                |                               | Labor participation rate              |
|                                |                               | Population growth rate                |
|                                |                               |                                       |
| **Social**                     |                               |                                       |
| Equality for all               | Equality for all              | Gender equity                         |
| Public Services                |                               | Income equity                         |
| Community engagement           | Public Services               | Urban absorption capacity             |
| Local political institution    |                               | Nutritional Standards                 |
|                                |                               | Food policy                           |
|                                | Community engagement          | Public-private collaboration          |
|                                |                               | Food safety net                       |
|                                | Local political institution   | political stability risk              |
|                                |                               | corruption                            |
|                                |                               | conflict                              |
|                                |                               |                                       |
| **Financial**                  |                               |                                       |
| Governance                     | Governance                    | Agricultural education and resources  |
| Financing                      |                               | Agricultural import tariffs           |
| Whole life value for money     | Financing                     | Per capita income                     |
| Wider economic impacts         |                               | Agricultural GDP                      |
|                                |                               | Access to financing for farmers       |
|                                | Whole life value for money    | Food expenses                         |
|                                |                               | Food price volatility                 |
|                                |                               | Food loss and waste                   |
|                                | Wider economic impacts        | Agricultural R&D                      |
|                                |                               | Adaptation of new technologies        |
|                                |                               |                                       |
| **Manufactured**               |                               |                                       |
| Energy and carbon              | Energy and carbon             | Energy footprint                      |
| Climate change and resilience  |                               | Carbon footprint                      |
| Resource efficiency            | Climate change resilience     | Climate smart agriculture             |
| Physical assets and services   |                               | Disaster management system            |
|                                | Resource efficiency           | Sustainable nitrogen use index        |
|                                |                               | Globalization                         |
|                                | Physical assets and services  | Access to quality seeds               |
|                                |                               | Telecommunications                    |
|                                |                               | Transportation                        |
|                                |                               | Food storage and facilities           |
|                                |                               | Irrigation   
|    """
    st.markdown(abc)
    

    # st.subheader('Abstract')
    # st.write('The food system is a complex web of actors/agents and interactions that spans production to the consumption of food. The global food system has been severely disrupted by the COVID-19 pandemic putting millions of people at risk of hunger and malnutrition. In a post-COVID-19 era, a stock-take will be required to see how our food system changed in response to current drivers/pressures and what lessons we learnt regarding the actions required to improve its resilience. The ability to understand, interpret, evaluate, and monitor key aspects of the food system is pivotal in building resilient food systems, as it is through this collection and analysis of information that we can improve resource allocation and effective decision-making. Thus, we present a diagnostic tool that can identify and monitor food stress using a food system resilience score. This score is derived from several indicators that describe natural, human, social, financial, and manufactured dimensions of the food system. The tool incorporates three major functionalities - situational awareness, scenario analysis, and intervention analysis. The situational awareness component helps derive a clear understanding of the strengths and weaknesses of food systems, while the scenario analysis component enables the anticipation of how various aspects within food systems may change when exposed to food shocks. The intervention analysis component points out the most effective and realistic interventions against anticipated food shocks. We have constructed the tool so that it can be deployed at various levels to enable better-informed decision-making toward building resilient food systems in the long term.')
