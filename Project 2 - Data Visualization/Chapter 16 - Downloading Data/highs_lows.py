import csv

filename = 'sitka_weather_07-2014.csv'
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)