"""
Song class
Represent a simple song object, with attributes such as song title, artist, album, release year, and genre.
Provides functionalities, such as all necessary getters and setters, and overriding of __str__ method
"""


class Song:
    def __init__(self, title, artist, album, year, genre):
        """Constructor method\n
        Args: title (str): the name of the song\n
        artist (str): the artist who performs the song\n
        album (str): the album which the song belongs to\n
        year (int): the release year for the project
        genre (str): the genre by which the song is identified"""
        self.set_title(title)
        self.set_artist(artist)
        self.set_album(album)
        self.set_year(year)
        self.set_genre(genre)

    def __str__(self):
        """String representation of a Song object.\n
        Returns: str: formatted, essential details about the song"""
        return f"{self.title} by {self.artist} ({self.album}, {self.year})"

    # setters
    def set_title(self, title):
        """Setter method.\n
        Args: title (str): the name by which the song will be identified"""
        self.title = title

    def set_artist(self, artist):
        """Setter method.\n
        Args: artist (str): the name of the performer of the song"""
        self.artist = artist

    def set_album(self, album):
        """Setter method.\n
        Args: album (str): the name of the album, to which the song belongs"""
        self.album = album

    def set_year(self, year):
        """Setter method.\n
        Args: year (int): the year that the song was released"""
        self.year = year

    def set_genre(self, genre):
        """Setter method.\n
        Args: genre (str): the genre under which the song will be identified"""
        self.genre = genre

    # getters
    def get_title(self):
        """Getter method.\n
        Returns: str: the song's name"""
        return self.title

    def get_artist(self):
        """Getter method.\n
        Returns: str: the artist's name"""
        return self.artist

    def get_album(self):
        """Getter method.\n
        Returns: str: the album's name"""
        return self.album

    def get_year(self):
        """Getter method.\n
        Returns: int: the release year of the song"""
        return self.year

    def get_genre(self):
        """Getter method.\n
        Returns: str: the genre of the song"""
        return self.genre

    def __lt__(self, other):
        """Overrides lower than operator. Compares song titles."""
        if str.lower(self.title) < str.lower(other.title):
            return True
        else:
            return False
