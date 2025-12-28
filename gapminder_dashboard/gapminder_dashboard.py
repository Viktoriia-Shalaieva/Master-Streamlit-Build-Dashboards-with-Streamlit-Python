import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(layout="wide")

# Page title
st.markdown("# Gapminder Dashboard")

df = pd.read_csv('gapminder_data_graphs.csv')

# Computation
unique_years = df['year'].unique()

# add dropdown
selected_year = st.selectbox(label='Year',
                             options=unique_years)

df_plot = df[df['year'] == selected_year]

average_gdp = round(df_plot['gdp'].mean(), 2)
average_life_exp = round(df_plot['life_exp'].mean(), 2)
average_hdi = round(df_plot['hdi_index'].mean(), 2)

# add 3 columns and metric widget
col1, col2, col3 = st.columns([1, 1, 1])
col1.metric(label='Average GDP', value=average_gdp)
col2.metric(label='Average Life Expactancy', value=average_life_exp)
col3.metric(label='Average HDI', value=average_hdi)

# add the scatter plot
title = 'Plot of GDP vs. Life expectancy for year {}'.format(selected_year)
scatter_plot = px.scatter(data_frame=df_plot,
                          x='gdp',
                          y='life_exp',
                          color='continent',
                          title=title)
st.plotly_chart(scatter_plot)

col4, col5 = st.columns([1, 1])
with col4:
    title = 'Distribution of GDP across the different continents for year {}'.format(selected_year)
    box_plot = px.box(data_frame=df_plot,
                      x='continent',
                      y='gdp',
                      title=title)
    st.plotly_chart(box_plot)

with col5:
    title = 'Distribution of GDP across the different continents for year {}'.format(selected_year)
    hist_plot = px.histogram(data_frame=df_plot,
                             x='gdp',
                             title=title)
    st.plotly_chart(hist_plot)

col6, col7 = st.columns([1, 1])
with col6:
    title = 'Distribution of Life Exp across the different continents for year {}'.format(selected_year)
    box_plot = px.box(data_frame=df_plot,
                      x='continent',
                      y='life_exp',
                      title=title)
    st.plotly_chart(box_plot)

with col7:
    title = 'Distribution of Life Exp across the different continents for year {}'.format(selected_year)
    hist_plot = px.histogram(data_frame=df_plot,
                             x='life_exp',
                             title=title)
    st.plotly_chart(hist_plot)

col8, col9 = st.columns([1, 1])
with col8:
    title = 'Distribution of HDI across the different continents for year {}'.format(selected_year)
    box_plot2 = px.box(data_frame=df_plot,
                       x='continent',
                       y='hdi_index',
                       title=title)
    st.plotly_chart(box_plot2)

with col9:
    title = 'Distribution of HDI across the different continents for year {}'.format(selected_year)
    hist_plot2 = px.histogram(data_frame=df_plot,
                              x='hdi_index',
                              title=title)
    st.plotly_chart(hist_plot2)
