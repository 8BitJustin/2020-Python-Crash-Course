import csv

filename = 'sitka_weather_07-2014.csv'
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)
    print(header_row)