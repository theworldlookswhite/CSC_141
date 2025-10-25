# 8-8 try it yourself
def make_album(artist, title, tracks=0):
    adict = {
        'artist': artist,
        'title': title,
    }
    if tracks: 
        adict['tracks'] = tracks
    return adict

tprompt = "name an album to recommend me"
aprompt = "who made it?"
print ("type quit to stop")

while True:
    title = input(tprompt)
    if title == 'quit':
        break
    artist = input(aprompt)
    if artist == 'quit': 
        break

    album = make_album(artist, title)
    print(album)

print("thank you for your recommendation")

