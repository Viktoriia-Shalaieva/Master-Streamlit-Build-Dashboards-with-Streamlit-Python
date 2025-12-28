import pandas as pd
import plotly.express as px
import streamlit as st


def create_histograms(x, title):
    """
    Hepler function to create histograms
    :param x: str, column name in dataframe
    :param title: str, title of created chart
    :return: plotly graph object
    """
    hist = px.histogram(data_frame=df_plot,
                        x=x,
                        color_discrete_sequence=['blue'],
                        title=title)
    return hist

st.set_page_config(layout="wide")

df = pd.read_csv('iris.csv')
unique_species = df['species'].unique()

st.title("Iris Dataset")

cola, colb = st.columns([1,1])

selected_species = cola.selectbox(label = 'Select Species',
                                  options=unique_species,
                                  label_visibility='collapsed')
show_hist = colb.checkbox(label = 'Show Histogram',
                          key='show_hist',)

# subset of data
df_plot = df[df['species'] == selected_species]

sl_mean = round(df_plot['sepal_length'].mean(),2)
sw_mean = round(df_plot['sepal_width'].mean(),2)
pl_mean = round(df_plot['petal_length'].mean(),2)
pw_mean = round(df_plot['petal_width'].mean(),2)

# define 4 columns in streamlit for the metric widgets
col1, col2, col3,col4 = st.columns([1,1,1,1])
col1.metric(label = 'Sepal Length', value= sl_mean,)
col2.metric(label = 'Sepal Width', value= sw_mean,)
col3.metric(label = 'Petal Length', value= pl_mean,)
col4.metric(label = 'Petal Width', value= pw_mean,)

# color map distionary
color_map = {'setosa':'gray',
             'versicolor':'gray',
             'virginica':'gray'}

# alter dictionary based on selected option
color_map[selected_species] = 'blue'

# add a scatter plot
scatter_plot = px.scatter(data_frame=df,
                          color_discrete_map=color_map,
                          x='sepal_length',
                          y='petal_width',
                          color='species',
                          size='petal_length',
                          title= 'Sepal length vs Petal width for {}'.format(selected_species)
                          )
st.plotly_chart(scatter_plot)

if show_hist:
    # define 4 columns in streamlit for the histograms
    col5, col6, col7,col8 = st.columns([1,1,1,1])

    # create histograms
    hist1 = create_histograms(x='sepal_length', title = 'Distribution of Sepal Length')
    hist2 = create_histograms(x='sepal_width', title = 'Distribution of Sepal Width')
    hist3 = create_histograms(x='petal_length', title = 'Distribution of Petal Length')
    hist4 = create_histograms(x='petal_width', title = 'Distribution of Petal Width')

    col5.plotly_chart(hist1)
    col6.plotly_chart(hist2)
    col7.plotly_chart(hist3)
    col8.plotly_chart(hist4)
