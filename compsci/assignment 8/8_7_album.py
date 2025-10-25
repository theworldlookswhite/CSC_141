# 8-7 try it yourself
def make_album(artist, title, tracks=0):
    adict = {
        'artist': artist,
        'title': title,
    }
    if tracks: 
        adict['tracks'] = tracks
    return adict

album = make_album('talking heads', 'remain in light', tracks=8)
print(album)
album = make_album('swans', 'the great annihilator', tracks=17)
print(album)
album = make_album('LCD soundsystem', 'this is happening', tracks=9)
print(album)

