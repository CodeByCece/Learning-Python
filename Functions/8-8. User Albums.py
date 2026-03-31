"""Utilizing album.py this program uses a while loop that allows users 
to enter an album’s artist and title."""

def make_album(artist_name, album_title, num_songs = None):
    """Accepts user inputs of artist name and album title;
    and returns a dictionary containing this information."""
    music = {'artist': artist_name, 'album': album_title}

    if num_songs:
        music['songs'] = num_songs
    return music

# While loop to continously accept user to input on artist
while True:
    print("\nPlease input the artist information: ")
    print("(enter 'q' at any time to quit program)")

    artist_n = input("Artist name: ")
    if artist_n =='q':
        break

    title = input("Artist album: ")
    if title == 'q':
        break

artist = make_album(artist_n, title)
print(artist)


