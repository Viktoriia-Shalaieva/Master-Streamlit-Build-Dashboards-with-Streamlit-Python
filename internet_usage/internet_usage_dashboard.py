import pandas as pd
import streamlit as st
import plotly.express as px


st.set_page_config(layout="wide")

df = pd.read_csv('share-of-individuals-using-the-internet.csv')
df = df[(df['Year'] >= 2000) & (df['Year'] <= 2016)]
print(df.columns)
print(df.info())

# get unique values
years = list(df['Year'].unique())
years.sort()
countries = df['Country'].unique()

st.header('Internet Usage Dashboard')

selected_year = st.selectbox(label='Select Year', index=0,
                             options=years)

df_plot = df[df['Year'] == selected_year]

col1, col2 = st.columns([3,1])

plot = px.choropleth(data_frame=df[df['Year'] == selected_year],
                     locations='Country',
                     locationmode='country names',
                     color='Individuals using the Internet (% of population)',
                     color_continuous_scale=px.colors.qualitative.Vivid,
                     title='Visual showing Internet Usage percentage across countries',)

histogram1 = px.histogram(data_frame=df_plot,
                          x='Individuals using the Internet (% of population)',
                          title='Distribution of Internet Usage for year {}'.format(selected_year),)

# Add to columns
col1.plotly_chart(plot)
col2.plotly_chart(histogram1)

# add a sidebar
st.sidebar.subheader('Country level detail')

# add a form
form = st.sidebar.form('form')
selected_country = form.selectbox(label='Select Country',
                                  options=countries,
                                  index=0)
submit = form.form_submit_button('Submit')

if submit:
    st.subheader('Country level analytics for {}'.format(selected_country))
    df_by_year_and_country = df[df['Country'] == selected_country]
    plot = px.line(data_frame=df_by_year_and_country,
                   x='Year',
                   y='Individuals using the Internet (% of population)',
                   title='Internet Usage over time in {}'.format(selected_country),)
    st.plotly_chart(plot)
