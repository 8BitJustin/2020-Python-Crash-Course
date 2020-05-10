import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get high/low temps and dates from files.
dv = 'death_valley_2014.csv'
sit = 'sitka_weather_2014.csv'

# Death Valley data.
with open(dv) as file:
    reader = csv.reader(file)
    header_row = next(reader)

    dv_dates, dv_highs, dv_lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dv_dates.append(current_date)
            dv_highs.append(high)
            dv_lows.append(low)

# Sitka data.
with open(sit) as file:
    reader = csv.reader(file)
    header_row = next(reader)

    sit_dates, sit_highs, sit_lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            sit_dates.append(current_date)
            sit_highs.append(high)
            sit_lows.append(low)

# Death Valley plot data.
fig = plt.figure(dpi=128, figsize=(12, 6))
plt.plot(dv_dates, dv_highs, c='#ff3600', alpha=0.8, label="DV High")
plt.plot(dv_dates, dv_lows, c='#ff7000', alpha=0.8, label="DV Low")
plt.fill_between(dv_dates, dv_highs, dv_lows, facecolor="red", alpha=0.3)

# Sitka plot data.
plt.plot(sit_dates, sit_highs, c='#0083ff', alpha=0.8, label="Sitka High")
plt.plot(sit_dates, sit_lows, c='#00c1ff', alpha=0.8, label="Sitka Low")
plt.fill_between(sit_dates, sit_highs, sit_lows, facecolor="blue", alpha=0.3)

# Format plot.
title = "Daily high and low temp comparison, 2014\nDeath Valley, CA / Sitka"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=12)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)
plt.legend()

plt.show()