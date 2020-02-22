rivers = {
    'nile': 'africa',
    'amazon': 'south america',
    'yangtze': 'asia',
    'yellow': 'china',
    'mississippi': 'north america'
}

for k, v in rivers.items():
    print('The ' + k.title() + ' River runs through ' + v.title() + '.')