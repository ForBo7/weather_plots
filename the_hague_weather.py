import pandas as pd
import plotly.express as px

# Load data.
filename = 'data/the_hague_weather.csv'
hague_weather = pd.read_csv(filename, parse_dates=True)
district_weather = hague_weather.groupby('NAME')
delft_weather = district_weather.get_group('DELFT, NL')

# Plot chat.
fig = px.line(delft_weather, x='DATE', y='PRCP',
              title='Daily Precipitation, Delft, The Hague - NL, 2020',
              labels={'DATE': '', 'PRCP': 'Precipitation (cm)'},
              color_discrete_sequence=['orange'],
              width=1920, height=1080)
fig.update_layout(title_font_size=36, font_size=24)
fig.update_yaxes(dtick=0.1, tickfont_size=18)
fig.update_xaxes(dtick='M1', tickfont_size=18)
fig.show()
