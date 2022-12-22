#######
# This line chart displays the same data
# three different ways along the y-axis.
######
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

np.random.seed(56)
x_values = np.linspace(0, 1, 100) # 100 evenly spaced values
y_values = np.random.randn(100)   # 100 random values

# create traces
up_offset = 5
dn_offset = -10
trace0 = go.Scatter(
    x = x_values,
    y = y_values + up_offset,
    mode = 'markers',    # type of chart
    name = 'markers A'     # label for chart legend
)
trace1 = go.Scatter(
    x = x_values,
    y = y_values,
    mode = 'lines+markers',
    name = 'lines+markers B'
)
trace2 = go.Scatter(
    x = x_values,
    y = y_values + dn_offset,
    mode = 'lines',
    name = 'lines C'
)
data = [trace0, trace1, trace2]  # assign traces to data which is a list
layout = go.Layout(
    title = 'Line chart showing three different modes'
)
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig, filename='line1.html')
