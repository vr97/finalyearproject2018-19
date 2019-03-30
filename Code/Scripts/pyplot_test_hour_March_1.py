# plotly.offline doesn't push your charts to the clouds
import plotly.offline as pyo
# allows us to create the Data and Figure objects
from plotly.graph_objs import *
# plotly.plotly pushes your charts to the cloud
import plotly.plotly as py
import plotly.io as pio

# pandas is a data analysis library
import pandas as pd
from pandas import DataFrame

popularityData = pd.read_excel("D:\\Users\\yashk\\Campaign-Assistant\\Data\\Annotated\\graph_hour_output_March_1.xls")  ##get DATA

trace1 = {'type': 'scatter',
          'mode': 'lines',
          'name': 'trace1',
          'x': popularityData['hour'],
          'y': popularityData['popularity']}
data = Data([trace1])

layout = {'title': 'Rahul Gandhi ',
          'xaxis': {'title': 'Hour'},
          'yaxis': {'title': 'Popularity in %'}}

fig = Figure(data=data, layout=layout)

pyo.plot(fig,filename = 'line-demo')
# static_image_bytes = pio.to_image(fig, format='png')
# pio.write_image(fig, file='plotly_static_image.png', format='png')