class Song:
    def __init__(self, name):
        self.name = name


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = set()

    def add_song(self, song):
        self.songs.add(song)

    def song_count(self):
        return len(self.songs)


Jamming = Song("Jamming")

my_playlist = Playlist("The Wailers")
three_little_bird = Playlist("Three little Bird")

my_playlist.add_song(Jamming)
my_playlist.add_song(three_little_bird)

print(my_playlist.song_count())
