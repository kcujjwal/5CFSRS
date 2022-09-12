import streamlit as st



def app():
    abc = """**Food Systems Resilience Diagnostics Tool**

**Abstract**

The food system is a complex web of actors/agents and interactions that spans production to the consumption of food. The global food system has been severely disrupted by the COVID-19 pandemic putting millions of people at risk of hunger and malnutrition. In a post-COVID-19 era, a stock-take will be required to see how our food system changed in response to current drivers/pressures and what lessons we learnt regarding the actions required to improve its resilience. The ability to understand, interpret, evaluate, and monitor key aspects of the food system is pivotal in building resilient food systems, as it is through this collection and analysis of information that we can improve resource allocation and effective decision-making. Thus, we present a diagnostic tool that can identify and monitor food stress using a food system resilience score. This score is derived from several indicators that describe natural, human, social, financial, and manufactured dimensions of the food system. The tool incorporates three major functionalities - situational awareness, scenario analysis, and intervention analysis. The situational awareness component helps derive a clear understanding of the strengths and weaknesses of food systems, while the scenario analysis component enables the anticipation of how various aspects within food systems may change when exposed to food shocks. The intervention analysis component points out the most effective and realistic interventions against anticipated food shocks. We have constructed the tool so that it can be deployed at various levels to enable better-informed decision-making toward building resilient food systems in the long term.

**A. Using the tool**

**1. Home Page**

It displays the basic information about the tool along with its components. It also describes the functionalities available in the tool along with what they contribute to. 

**2. Functionalities**

![Test](Decision.PNG)

**2.1 Situational Awareness**

The component helps derive a clear understanding of the strengths and weaknesses of national food systems. The world map, descriptive analysis and comparative analysis serve to enable situational awareness.

**2.1.1 World Map**

This component is displayed as the home page for the tool which displays animated and annotated world map based on the scores of countries for several indicators. The world map can be customized by selecting desired indicator in the Control Center.

**2.1.2 Descriptive Analysis**

This component summarizes the strengths and weaknesses of a national food system when the analysis is chosen by “Country”. When the analysis is chosen by “Indicator”, the component lists the best performing and the worst performing countries for the chosen indicator(s). The visualizations can also be customized for analysis years and multiple selections of countries and indicators.

**2.1.3 Comparative Analysis**

This component facilitates comparisons of performance of national food systems at a temporal scale. The visualizations in this component can be chosen by either “Country” or “Indicator”. The visualizations also allow for multiple selections of countries and indicators. Five different types of analyses are available in the component.

**1-year Analysis:** It draws a picture of the current strengths and weaknesses of a national food system when the analysis is chosen by “Country” and the current best performing and worst performing countries when the analysis is chosen by “Indicator” compared to that in the previous year.

**5-year Analysis:** It draws a picture of the current strengths and weaknesses of a national food system when the analysis is chosen by “Country” and the current best performing and worst performing countries when the analysis is chosen by “Indicator” compared to the statistics five years ago.

**YTD Analysis:** It draws a picture of the current strengths and weaknesses of a national food system when the analysis is chosen by “Country” and the current best performing and worst performing countries when the analysis is chosen by “Indicator” compared to the earliest statistics (2012).

**Country vs Country:** It directly compares a country against other and shows how the scores of the countries in five capitals including overall food system resilience have changed at a temporal scale.
Capitals: It displays the performance of chosen countries for all indicators within the selected capital at a temporal scale.

**2.2 Scenario Analysis**

This component helps anticipate how national food systems may change when exposed to food shocks with quantified shock intensity. When the scenario analysis is selected at a global scale, the component first displays the global vulnerability of the selected food shock, i.e., the most affected and the least affected nations and then the most resilient and the most vulnerable nations with the estimated percentage change (%) annotated in the visualization. When the scenario analysis is selected at a national scale, the component first displays the cumulative standardized impact scores of all food shocks for a selected range of years and then the most resilient and the most vulnerable indicators of the national food system for the chosen country.

**2.3 Best Interventions**

This component lists the most realistic and effective suite of interventions for a selected national food system based on historical data and expert opinions for any food shocks quantified with shock intensity. The component displays the suite of interventions ranked based on the effectiveness score for “Users” while the component asks the experts to express their opinions on the possible interventions for a quantified food shock scenario when the component is chosen for “Expert” users. Once the experts complete sharing their expert knowledge, the experts can also view the ranked suites of interventions.

**3. Five Capitals based framework for food system resilience assessment**

**The five capitals approach provides a holistic way to measure value.**

**Table 1: Categorization of the variables under five capitals**

| Capitals                       | Capitals categories           | Variables                             |
|--------------------------------|-------------------------------|---------------------------------------|
| **Natural**                        | Biodiversity                  | Biodiversity Status                   |
| Biodiversity                   |                               | Ecosystem                             |
| Air quality                    |                               | Forest Area                           |
| Water quality                  | Air quality                   | GHGE per capita                       |
| Land quality                   | Water quality                 | Water availability                    |
|                                |                               | Water quality                         |
|                                |                               | Water footprint                       |
|                                | Land quality                  | Total Arable land per capita          |
|                                |                               | Land degradation per arable land      |
|                                |                               |                                       |
| **Human**                          | Wellbeing                     | Obesity                               |
| Wellbeing                      |                               | Undernourishment                      |
| Skills and training            |                               | Foodborne diseases burden             |
|                                |                               | Drinking Water                        |
|                                |                               | Micronutrient Availability            |
|                                |                               | Protein availability                  |
|                                |                               | Food diversity                        |
|                                | Skills and Training           | Literacy rate                         |
|                                |                               | HDI                                   |
|                                |                               | Labor participation rate              |
|                                |                               | Population growth rate                |
| **Social**                        | Equality for all              | Gender equity                         |
| Equality for all               |                               | Income equity                         |
| Public services                | Public Services               | Urban absorption capacity             |
| Community engagement           |                               | Nutritional Standards                 |
| local political institution    |                               | Food policy                           |
|                                | Community engagement          | Public-private collaboration          |
|                                |                               | Food safety net                       |
|                                | local political institution   | political stability risk              |
|                                |                               | corruption                            |
|                                |                               | conflict                              |
|                                |                               |                                       |
| **Financial**                      |                               |                                       |
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
| **Manufactured**                   | Energy and carbon             | Energy footprint                      |
| Energy and carbon              |                               | Carbon footprint                      |
| Climate change and resilience  | Climate change resilience     | Climate smart agriculture             |
| Resource efficiency            |                               | Disaster management system            |
| Physical assets and services   | Resource efficiency           | Sustainable nitrogen use index        |
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
