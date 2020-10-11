#IMPORT LIBRARIES
import pandas as pd
import plotly_express as px

#READ GRAPH DATA
df = pd.read_csv('data.csv')

#SHOW THE GRAPH
graph = px.scatter(df,x = 'date',y = 'cases',color = 'country',title = "COVID-19 CASES OF COUNTRIES DAYWISE")
graph.show()