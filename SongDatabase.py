import csv
from Song import Song
from SongCollection import SongCollection

"""
SongDatabase class
Purpose is to read song data from a file, load the songs into a SongCollection object, and manipulate this object.
The class supports functionalities such as printing out data about the collection in a tabular manner and manipulating 
the collection in one way or another.
"""


class SongDatabase:
    def __init__(self, filename):
        """Constructor method\n
        Args: filename (str): the name of the file, from which the program should read song data\n"""
        self.set_filename(filename)
        self.set_song_collection()

    # setters
    def set_filename(self, filename):
        """Setter method.\n
        Args: filename (str): the name of the file, from which the program should read song data"""
        self.filename = filename

    def set_song_collection(self):
        """Method to read songs from a file, and store them into a SongCollection object"""
        try:
            with open(self.filename, "r") as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=",")  # declare a reader object
                self.song_collection = SongCollection([])  # initialize an empty SongCollection object, to store songs

                header = next(csv_reader)  # read the first line in the file, which is a header line

                # read remaining lines in the file, create a song object for each, and append it to the song collection
                for row in csv_reader:
                    cur_song = Song(row[0], row[1], row[2], row[3], row[4])
                    self.song_collection.append(cur_song)
        except IndexError:
            print("Data inside file is not formatted accordingly! Cannot load data into a SongCollection object")
        except FileNotFoundError:
            print("Cannot open file!")

    def display(self):
        """Method to display a tabular visualization of song data to the user"""
        print("--------------------------------------------------------------------------")
        print("Title".center(16), "Artist".center(12), "Album".center(20), "Year".center(6), "Genre".center(16))
        print("--------------------------------------------------------------------------")
        for song in self.song_collection:
            print(song.get_title().center(16), song.get_artist().center(12), song.get_album().center(20),
                  str(song.get_year()).center(6), song.get_genre().center(16))
        print("--------------------------------------------------------------------------")

    def save_songs(self):
        """Method to write to the file. Used in the cases where the song collection object associated with the
        database changes, and the file needs to be updated accordingly."""
        with open(self.filename, "w", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Title', "Artist", "Album", "Year", "Genre"])  # write the header for the file
            for song in self.song_collection:  # write each song from song_collection into the csv file, on a new line
                csv_writer.writerow([song.get_title(), song.get_artist(), song.get_album(), song.get_year(),
                                     song.get_genre()])  # write the song in appropriate format

    def add_song(self, song):
        """Method to append a song to the file.
        Args: song (Song): the song to be added"""
        self.song_collection.append(song)  # add the song to the SongCollection object
        with open(self.filename, "a", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([song.get_title(), song.get_artist(), song.get_album(), song.get_year(),
                                 song.get_genre()])  # append the new song to the file, in appropriate format

    def filter_by(self, filter_type, filter_value):
        """This method filters the SongCollection object associated with this database\n
        Args: filter_type (str): the attribute by which the song collection will be filtered (Artist, Title, Album,
        Year, or Genre)\n
        filter_value (str): the value of the attribute, with which to compare the attribute of the song"""

        if filter_type == "Title":
            self.song_collection = [song for song in self.song_collection if song.get_title() == filter_value]
        elif filter_type == "Artist":
            self.song_collection = [song for song in self.song_collection if song.get_artist() == filter_value]
        elif filter_type == "Album":
            self.song_collection = [song for song in self.song_collection if song.get_album() == filter_value]
        elif filter_type == "Year":
            self.song_collection = [song for song in self.song_collection if song.get_year() == filter_value]
        elif filter_type == "Genre":
            self.song_collection = [song for song in self.song_collection if song.get_genre() == filter_value]
        else:
            print("Please enter a valid filter type!")
            # self.song_collection remains the same

        self.save_songs()

    def sort(self):
        """Sorts the song collection by Title"""
        self.song_collection.sort()
        self.save_songs()
