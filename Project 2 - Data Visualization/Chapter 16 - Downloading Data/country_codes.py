from pygal.maps.world import COUNTRIES


def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    for code, name in COUNTRIES.items():
        if country_name == 'Yemen, Rep.':
            return 'ye'
        elif country_name == 'Venezuela, RB':
            return 've'
        elif country_name == 'Micronesia, Fed. Sts':
            return 'fm'
        elif country_name == 'Korea, Rep.':
            return 'kr'

        if name == country_name:
            return code





