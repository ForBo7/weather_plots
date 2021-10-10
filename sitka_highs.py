import pandas as pd
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_07-2018_simple.csv'
sitka_weather = pd.read_csv(filename)
sitka_weather.loc[:, 'DATE'] = pd.to_datetime(sitka_weather.loc[:, 'DATE'],
                                              format='%Y-%m-%d')
print(sitka_weather.loc[:, 'DATE'].dtypes)

# Plot the high temperatures.
plt.style.use('seaborn')
sitka_weather.set_index('DATE').loc[:, 'TMAX'].plot(c='red')

# Format plot.
plt.title("Daily high temperatures, July 2018", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.savefig('sitka_weather.png', bbox_inches='tight')
