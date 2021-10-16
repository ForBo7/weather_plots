import pandas as pd
import plotly.express as px

# Load data.
filename = 'data/islamabad_weather_2020.csv'
islo_weather = pd.read_csv(filename, parse_dates=True)

# Convert from fahrenheit to celsius.
islo_weather['TAVG'] = islo_weather['TAVG'].apply(lambda f: (f-32) * (5/9))

# Plot chart.
fig = px.line(islo_weather, x='DATE', y='TAVG',
              title='Daily Average Temperature, Islamabad, 2020',
              labels={'DATE': '', 'TAVG': 'Temperature (C)'},
              color_discrete_sequence=['green'], width=1920, height=1080)
fig.update_layout(title_font_size=36, font_size=24)
fig.update_yaxes(dtick=2, tickfont_size=18)
fig.update_xaxes(dtick='M1', tickfont_size=18)
fig.show()
