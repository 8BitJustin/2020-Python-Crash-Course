import json


filename = 'gpd.json'
with open(filename) as f:
    gdp_data = json.load(f)

for gdp_dict in gdp_data:
    if gdp_dict['Year'] == 2016:
        country_name = gdp_dict['Country Name']
        value = gdp_dict['Value']
        print(f'{country_name}: {value}')