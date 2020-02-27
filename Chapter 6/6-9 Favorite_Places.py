favorite_places = {
    'justin': ['norway', 'japan', 'italy'],
    'lynette': ['germany'],
    'skyler': ['italy', 'germany']
}

for names, locs in favorite_places.items():
    print('\n' + names.title() + ' would like to visit:')
    for loc in locs:
        print('\t' + loc.title())