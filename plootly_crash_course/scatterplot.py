import pandas as pd
import plotly.express as px


df = pd.read_csv('iris.csv')

print(df.columns)

plot = px.scatter(data_frame=df,
                  size='sepal_length',
                  x='sepal_width',
                  color='species',
                  facet_row='species',
                  y='petal_length',
                  title='Plot of Sepal Length vs. Petal Length')

plot.show()