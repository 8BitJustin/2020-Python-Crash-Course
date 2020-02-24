fav_languages = {
    'justin': 'python',
    'james': 'php',
    'nick': 'ruby'
}

take_poll = ['dave', 'james', 'toby', 'nick']

for j in take_poll:
    if j in fav_languages.keys():
        print('Thank you for taking our poll, ' + j.title() + '!')
    else:
        print('Please take our poll, ' + j.title() + '.')