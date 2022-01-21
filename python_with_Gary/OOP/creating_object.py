class Playlist:
    def __init__(self, playlist_name: str, song_count: int):
        self.playlist_name = playlist_name
        self.song_count = song_count

    def play(self):
        return f'Playing {self.playlist_name} songs'

    def shuffle(self):
        return f'shuffling {self.song_count} songs'


my_playlist = Playlist("running song", 20)
# print(my_playlist.playlist_name)
# print(my_playlist.song_count)
print(my_playlist.play())
print(my_playlist.shuffle())
