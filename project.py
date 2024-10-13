import streamlit as st
import streamlit as st
import numpy as np  # linear algebra
import pandas as pd  # data processing
import plotly as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly import subplots

st.set_page_config(
    page_title= "Energy Analysis Dashboard",
    layout= "wide",
    initial_sidebar_state= "expanded"
)


# Header, title, information
st.image('C:/Users/ppoli/Datacamp24/windmills.jpg')
st.title("Energy distributed in the world")
st.write("Project to discover energy resourses in different countries. Use this dashboard to explore energy production trends over time in different country.")

#Production plots
df = pd.read_csv('c:/Users/ppoli/Datacamp24/Panel format.csv')
country = st.sidebar.selectbox("Select a country:", df["Country"].unique())


#POPULATION COUNTRY
def plot_population(country):
    country_data = df[df['Country'] == country]

    fig_pop = px.line(country_data, x='Year', y='pop', title=f'Population Over Time in {country}')
    st.plotly_chart(fig_pop)

st.title('Population Growth Analysis')
plot_population(country)

#PRODUCTION
def plot_energy_production(country):
    country_data = df[df['Country'] == country]

    fig_pop = px.line(country_data, x='Year', y='pop', title=f'Population Over Time in {country}')
    st.plotly_chart(fig_pop)
    fig_wind = px.line(country_data, x='Year', y='wind_ej', title=f'Wind Energy Production in {country} (in Exajoules)')
    st.plotly_chart(fig_wind)
    fig_hydro = px.line(country_data, x='Year', y='hydro_ej', title=f'Hydro Energy Production in {country} (in Exajoules)')
    st.plotly_chart(fig_hydro)
    fig_nuclear = px.line(country_data, x='Year', y='nuclear_ej', title=f'Nuclear Energy Production in {country} (in Exajoules)')
    st.plotly_chart(fig_nuclear)
    fig_renewable = px.line(country_data, x='Year', y='ren_power_ej', title=f'Renewable Energy Production in {country} (in Exajoules)')
    st.plotly_chart(fig_renewable)
    fig_solar = px.line(country_data, x='Year', y='solar_ej', title=f'Solar Energy Production in {country} (in Exajoules)')
    st.plotly_chart(fig_solar)
    fig_coal = px.line(country_data, x='Year', y='coalprod_ej', title=f'Coal Energy Production in {country} (in Exajoules)')
    st.plotly_chart(fig_coal)
    fig_gas = px.line(country_data, x='Year', y='gasprod_ej', title=f'Gas Energy Production in {country} (in Exajoules)')
    st.plotly_chart(fig_gas)
    
    
st.title('Energy Production Analysis')
plot_energy_production(country)






