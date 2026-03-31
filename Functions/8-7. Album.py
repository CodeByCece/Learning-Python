"""Function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information."""

def make_album(artist_name, album_title, num_songs = None):
    """Accepts an artist name and album title
    and returns a dictionary containing these information."""
    music = {'artist': artist_name, 'album': album_title}
    if num_songs:
        music['songs'] = num_songs
    return music

r_n_b = make_album('frank ocean', 'blonde')
print(r_n_b)

rock = make_album('the beattles', 'abbey road')
print(rock)

jazz = make_album('kenny G', 'the moment')
print(jazz)

hip_hop = make_album('queen latifah', 'persona', num_songs = 14 )
print(hip_hop)
