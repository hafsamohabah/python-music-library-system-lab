
class Song:
    """Represent a song and track music library statistics."""

    # Class attributes shared by all Song objects
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    # Support both names used in the assignment and automated tests
    artists_count = artist_count

    def __init__(self, name, artist, genre):
        """Create a song and update the library statistics."""
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artists_count(self.artist)

    @classmethod
    def add_song_to_count(cls):
        """Increment the total number of songs."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Add a genre if it has not already been recorded."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Add an artist if they have not already been recorded."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Count the number of songs in each genre."""
        if genre not in cls.genre_count:
            cls.genre_count[genre] = 0

        cls.genre_count[genre] += 1

    @classmethod
    def add_to_artists_count(cls, artist):
        """Count the number of songs by each artist."""
        if artist not in cls.artist_count:
            cls.artist_count[artist] = 0

        cls.artist_count[artist] += 1
