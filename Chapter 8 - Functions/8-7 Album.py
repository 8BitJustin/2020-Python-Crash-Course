def make_album(artist_name, album_title, tracks=''):
    album = {'artist': artist_name.title(), 'title': album_title.title()}
    if tracks:
        album['tracks'] = tracks
    return album


lp = make_album('linkin park', 'hybrid theory')
soad = make_album('system of a down', 'toxicity', 14)
h2bhc = make_album('anabolic frolic', 'happy 2 b hardcore')

print(lp)
print(soad)
print(h2bhc)