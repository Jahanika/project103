import pandas as pd
import plotly.express as px

df=pd.read_csv("projectdata103.csv")
figure=px.scatter(df, x="date", y="cases", color="country")
figure.show()