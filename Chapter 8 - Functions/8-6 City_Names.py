def city_country(city, country):
    ci = city.title()
    co = country.title()
    full = ci + ', ' + co
    return full


europe = city_country('paris', 'france')
america = city_country('tucson', 'united states')
mexico = city_country('mexico city', 'mexico')

print(europe)
print(america)
print(mexico)