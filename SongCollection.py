"""
SongCollection class, inheriting list class, and a composition of Song class
Purpose is to represent a simple collection of songs, providing functionalities such as getter and setters
"""


class SongCollection(list):
    def __init__(self, songs):
        """Constructor method\n
        Args: songs (list): list of Song objects to be stored in the song collection"""
        self.set_songs(songs)

    # setters
    def set_songs(self, songs):
        """Setter method\n
        Args: songs (list): list of Song objects to be stored in the song collection"""
        self.songs = songs

    # getters
    def get_songs(self):
        """Getter method for the list of songs stored in the song collection. \n
        Returns: list: Song objects in the song collection"""
        return self.songs
