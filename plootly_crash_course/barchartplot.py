import pandas as pd
import plotly.express as px


df = pd.read_csv('iris.csv')

print(df.head())

df1 = df.groupby(['species']).mean().reset_index()

print(df1)

plot = px.bar(data_frame=df1,
              x='species',
              y='petal_length',
              title='Bar chart showing average petal width across species')

plot.show()