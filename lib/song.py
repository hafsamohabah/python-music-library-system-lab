
class Song:
    # Class attributes shared by all songs
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Attributes belonging to each individual song
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update the shared class attributes
        self.add_song_to_count()
        self.add_to_genres(self.genre)
        self.add_to_artists(self.artist)
        self.add_to_genre_count(self.genre)
        self.add_to_artists_count(self.artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre not in cls.genre_count:
            cls.genre_count[genre] = 0
        cls.genre_count[genre] += 1

    @classmethod
    def add_to_artists_count(cls, artist):
        if artist not in cls.artist_count:
            cls.artist_count[artist] = 0
        cls.artist_count[artist] += 1
