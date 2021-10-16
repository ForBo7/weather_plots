import pandas as pd
import plotly.express as px

# Load data.
filename = 'data/death_valley_2018_simple.csv'
dv_weather = pd.read_csv(filename, parse_dates=True)

# Convert TMAX to celsius.
dv_weather['TMAX'] = dv_weather['TMAX'].apply(lambda f: (f - 32) * (5/9))

# Plot graph.
fig = px.line(dv_weather, x='DATE', y=['TMAX', 'PRCP'],
              title='Daily Temperature, Death Valley 2018',
              labels={'DATE': '', 'value': 'Temperature', 'variable': ''},
              category_orders={'': ['High Temperature', 'Precipitation']},
              color_discrete_sequence=['red', 'blue'])
fig.update_yaxes(ticksuffix=' °C', showgrid=True)
fig.show()
