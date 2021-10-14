import pandas as pd
import matplotlib.pyplot as plt

# Load data.
filename = 'data/death_valley_2018_simple.csv'
death_valley_weather = pd.read_csv(filename, parse_dates=True)

# Convert date column from string to datetime.
death_valley_weather['DATE'] = pd.to_datetime(death_valley_weather['DATE'],
                                              format='%Y-%m-%d')

# Set overall style to use and plot data.
plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(16, 10), dpi=227)
ax.plot(death_valley_weather['DATE'], death_valley_weather['TMAX'], c='red')

# Set chart title and label axes.
ax.set_title('Daily High Temperatures, Death Valley', fontsize=24)
ax.set_xlabel('', fontsize=14)
ax.set_ylabel('Temperature (F)', fontsize=14)

ax.tick_params(axis='both', labelsize=14)

plt.show()
