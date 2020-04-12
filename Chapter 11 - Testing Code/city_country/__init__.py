def city_country(city, country, population=""):
    city_name = city
    country_name = country
    city_population = population
    if city_population:
        area = f"{city_name.title()}, {country_name.title()} - {str(population)}"
    else:
        area = f"{city_name.title()}, {country_name.title()}"
    return area


# Test
# print(city_country('santiago', 'chile', 5000000))
# print(city_country('santiago', 'chile'))
