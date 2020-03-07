def make_album(artist_name, album_title, tracks=''):
    album = {'artist': artist_name.title(), 'title': album_title.title()}

    return album


while True:
    print('Lemme know your favorite artist and their best album:')
    print('(press \'q\' to quit')
    name = input('Artist name? ')
    if name == 'q':
        break
    album = input('Album name? ')
    if album == 'q':
        break

    full = 'Your artist is ' + name.title() + ' and your favorite album of ' \
                                              'their\'s is ' + album.title()\
           + '.'

    print(full)