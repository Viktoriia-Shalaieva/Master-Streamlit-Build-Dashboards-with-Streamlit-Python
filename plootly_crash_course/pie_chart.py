import pandas as pd
import plotly.express as px


df = pd.read_csv('tips.csv')

print(df.columns)
print(df.nunique())

plot = px.pie(data_frame=df,
              values='tip',
              names='sex',
              facet_col='smoker',
              hole=0.5,
              title='Pie Chart showing total tips across gender',)

plot.show()
