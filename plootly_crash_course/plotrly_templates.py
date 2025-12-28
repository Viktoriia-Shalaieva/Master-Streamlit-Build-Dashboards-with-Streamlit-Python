import pandas as pd
import plotly.express as px


df = pd.read_csv('iris.csv')

plotly_themes =   ['ggplot2', 'seaborn', 'simple_white', 'plotly', 'plotly_white', 'plotly_dark', 'presentation',
                   'xgridoff', 'ygridoff', 'gridon', 'none']

plot = px.scatter(data_frame=df,
                  x='sepal_width',
                  size='sepal_length',
                  template='ggplot2',
                  color='species',
                  y='petal_length',
                  title='Plot of Sepal Length vs. Petal Length')

plot.show()