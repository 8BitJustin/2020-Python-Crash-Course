def city_country(city, country, population):
    city_name = city
    country_name = country
    area = f"{city_name.title()}, {country_name.title()} - {str(population)}"

    return area


# Test
print(city_country('santiago', 'chile', 5000000))