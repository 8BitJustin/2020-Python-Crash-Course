import csv
from matplotlib import pyplot as plt
from datetime import datetime

# Pull precip values from file.
filename = 'tucson_tia_precip_2019.csv'

with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)

    precipitation, dates = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%m/%d/%Y")
        dates.append(current_date)

        value = float(row[3])
        precipitation.append(value)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 4))
plt.plot(dates, precipitation, c='blue', alpha=0.7)
plt.fill_between(dates, precipitation, 0, facecolor="blue", alpha=0.5)

# Format plot.
plt.title('Precipitation totals, Tucson 2019', fontsize=18)
plt.xlabel('', fontsize=12)
fig.autofmt_xdate()
plt.ylabel('Precipitation (inches)', fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)

plt.show()