import csv
from matplotlib import pyplot as plt
from datetime import datetime

# Get dates, highs, and lows from tucson_1980.csv file.
filename = "tucson_high_low_2019.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        # Only runs rows from Tucson Int'l Airport.
        if row[1] == "TUCSON INTERNATIONAL AIRPORT, AZ US":
            # Will create variables current_date, high, and low.
            try:
                current_date = datetime.strptime(row[2], "%Y-%m-%d")
                high = int(row[3])
                low = int(row[4])
            # Exception ran if above can't be done.
            except ValueError:
                print(current_date, 'missing data')
            # If all is present, variables are appended to their lists.
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

# Plotting data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5, label="High")
plt.plot(dates, lows, c='blue', alpha=0.5, label="Low")
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# Formatting plot.
plt.title("High and low temps, Tucson AZ\nApril 1 - Sept 30 2019", fontsize=18)
plt.xlabel("", fontsize=12)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)
plt.legend()

plt.savefig('tucson_high_low_2019.png')
