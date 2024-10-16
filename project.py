import streamlit as st
import streamlit as st
import numpy as np  # linear algebra
import pandas as pd  # data processing
# import plotly as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly import subplots

#PAGE SETS
st.set_page_config(
    page_title= "Energy Analysis Dashboard",
    page_icon="🔋", 
    layout= "wide",
    initial_sidebar_state= "expanded",
)

#MAIN SETS
st.title("Energy Production Distribution in the World")
st.image('/workspaces/data_analysis/windmills.jpg')
st.write("Project to discover energy resourses in different countries. Use this dashboard to explore energy production trends over time in different country.")

#DATA
df = pd.read_csv('/workspaces/data_analysis/Panel format.csv')
df["Year"] = pd.to_datetime(df["Year"],format="%Y")
country = st.sidebar.selectbox("Select a country:", df["Country"].unique())


#COUNTRIES PER REGION
region_counts = df.groupby('Region')['Country'].nunique().reset_index()
region_counts.columns = ['Region', 'Country']
st.title('Countries Distribution by Regions')
fig_donut = px.pie(
    region_counts,
    values='Country',
    names='Region',
    hole=0.3, 
    color_discrete_sequence=px.colors.qualitative.Set3
)

for index, row in region_counts.iterrows():
    countries = df[df['Region'] == row['Region']]['Country'].unique().tolist()
    country_list = ", ".join(countries)
    fig_donut.add_annotation(
        text='',
        xref='paper', yref='paper',
        x=0.5, y=0.5,
        showarrow=False,
        font=dict(size=12),
        align='center'
    )

st.plotly_chart(fig_donut)

#POPULATION COUNTRY
def plot_population(country):
    country_data = df[df['Country'] == country]

    fig_pop = px.line(country_data, x='Year', y='pop',title=f'Population Over Time in {country}')
    fig_pop.update_layout(
                yaxis_title='Population' 
            )
    st.plotly_chart(fig_pop)

st.title('Population Analysis (by country)')
plot_population(country)

#PRODUCTION PLOTS
def plot_energy_production(country):
    country_data = df[df['Country'] == country]
    
    with st.container():
        # Create two columns
        col1, col2 = st.columns(2)

        with col1:
            fig_wind = px.line(country_data, x='Year', y='wind_ej', title=f'Wind Energy Production in {country} (in Exajoules)', color_discrete_sequence=['green'])
            fig_wind.update_layout(
                yaxis_title='Wind Energy Production (Exajoules)' 
            )
            st.plotly_chart(fig_wind)
            
            fig_hydro = px.line(country_data, x='Year', y='hydro_ej', title=f'Hydro Energy Production in {country} (in Exajoules)', color_discrete_sequence=['red'])
            fig_hydro.update_layout(
                yaxis_title='Hydro Energy Production (Exajoules)' 
            )
            st.plotly_chart(fig_hydro)
            
            fig_nuclear = px.line(country_data, x='Year', y='nuclear_ej', title=f'Nuclear Energy Production in {country} (in Exajoules)', color_discrete_sequence=['yellow'])
            fig_nuclear.update_layout(
                yaxis_title='Nuclear Energy Production (Exajoules)' 
            )
            st.plotly_chart(fig_nuclear)
            
            fig_renewable = px.line(country_data, x='Year', y='ren_power_ej', title=f'Renewable Energy Production in {country} (in Exajoules)', color_discrete_sequence=['purple'])
            fig_renewable.update_layout(
                yaxis_title='Renewable Energy Production (Exajoules)' 
            )
            st.plotly_chart(fig_renewable)
            
        with col2:
            fig_solar = px.line(country_data, x='Year', y='solar_ej', title=f'Solar Energy Production in {country} (in Exajoules)', color_discrete_sequence=['pink'])
            fig_solar.update_layout(
                yaxis_title='Solar Energy Production (Exajoules)' 
            )
            st.plotly_chart(fig_solar)
            
            fig_coal = px.line(country_data, x='Year', y='coalprod_ej', title=f'Coal Energy Production in {country} (in Exajoules)', color_discrete_sequence=['white'])
            fig_coal.update_layout(
                yaxis_title='Coal Energy Production (Exajoules)' 
            )
            st.plotly_chart(fig_coal)
            
            fig_gas = px.line(country_data, x='Year', y='gasprod_ej', title=f'Gas Energy Production in {country} (in Exajoules)', color_discrete_sequence=['orange'])
            fig_gas.update_layout(
                yaxis_title='Gas Energy Production (Exajoules)' 
            )
            st.plotly_chart(fig_gas)
    
    
st.title('Energy Production Analysis (by country)')
plot_energy_production(country)






