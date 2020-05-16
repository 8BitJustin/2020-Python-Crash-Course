import json
from pygal.maps.world import World
from country_codes import get_country_code

# Loads data into a list.
filename = 'gpd.json'
with open(filename) as f:
    gdp_data = json.load(f)

# Build a dictionary of GDP data.
values = {}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == 2016:
        country_name = gdp_dict['Country Name']
        value = int(gdp_dict['Value'])
        code = get_country_code(country_name)
        if code:
            values[code] = value

# Value levels.
cc_value_1, cc_value_2, cc_value_3 = {}, {}, {}
for c, v in values.items():
    if v < 100000000000:
        cc_value_1[c] = v
    elif v < 1000000000000:
        cc_value_2[c] = v
    else:
        cc_value_3[c] = v

# Prints numerical value of the three categories of GDP.
print(len(cc_value_1), len(cc_value_2), len(cc_value_3))

wm = World()
wm.title = "World Gross Domestic Product in 2016, by country"
# Keeps value from being scientific notation.
wm.value_formatter = lambda x: "{:,}".format(x)
wm.add('< 100B', cc_value_1)
wm.add('100B - 1T', cc_value_2)
wm.add('> 1T', cc_value_3)

wm.render_to_file('world_gdp_2016.svg')
