import pandas as pd
import plotly.express as px


df = pd.read_csv('iris.csv')

print(df.columns)

plot = px.histogram(data_frame=df,
                    x='sepal_length',
                    nbins=8,
                    color='species',
                    barmode='overlay',
                    title='Distribution of sepal_length')
plot.show()
