cities_info = {
    'naples': {
        'country': 'italy',
        'population': 975139,
        'fact': 'People living in Naples are called Neapolitans.'
    },
    'oslo': {
        'country': 'norway',
        'population': 634463,
        'fact': 'Most of Oslo consists of forest.'
    },
    'berlin': {
        'country': 'germany',
        'population': 3520031,
        'fact': 'Berlin is over 9 times the size of Paris, BUT it only has '
                '1/5 of Paris’ density.'
    }
}

for city, info in cities_info.items():
    print('\n' + city.title())
    co = info['country']
    pop = info['population']
    fac = info['fact']
    print('\tCountry: ' + co.title())
    print('\tPopulation: ' + str(pop))
    print('\tRandom Fact: ' + fac)