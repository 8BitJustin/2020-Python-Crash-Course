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
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            dates.append(current_date)

            high = int(row[3])
            highs.append(high)

            low = int(row[4])
            lows.append(low)

# Plotting data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')

# Formatting plot.
plt.title("High and low temps, Tucson AZ\nJune 1980", fontsize=18)
plt.xlabel("", fontsize=12)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)

plt.show()