class Song:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'song(name={self.name})'


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = set()

    def add_song(self, song):
        self.songs.add(song)

    def __len__(self):
        return len(self.songs)

    # def song_count(self):
    #     return len(self.songs)


song1 = Song('Stand up')
song2 = Song('oh Boy')

rap = Playlist('Rap')
rap.add_song(song1)
rap.add_song(song2)
song_count = len(rap)
print(song_count)
