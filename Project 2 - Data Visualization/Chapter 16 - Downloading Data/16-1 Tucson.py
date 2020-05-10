import csv
from matplotlib import pyplot as plt
from datetime import datetime

# Get dates, highs, and lows from tucson_1980.csv file.
filename = "tucson_1980.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        if row[1] == "TUCSON INTERNATIONAL AIRPORT, AZ US":
            try:
                current_date = datetime.strptime(row[2], "%Y-%m-%d")
                high = int(row[3])
                low = int(row[4])
            except ValueError:
                print(current_date, 'missing data')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

# Plotting data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# Formatting plot.
plt.title("High and low temps, Tucson AZ\nJune 1980", fontsize=18)
plt.xlabel("", fontsize=12)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)

plt.savefig('tucson_temps_6-1980.png')