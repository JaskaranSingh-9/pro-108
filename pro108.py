import pandas as pe
import plotly.figure_factory as pf
import csv

df= pe.read_csv("projects\pro 108\data.csv")
fig=pf.create_distplot([df["Avg Rating"].tolist()], ["Rating"])
fig.show()