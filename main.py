from Song import Song
from SongDatabase import SongDatabase

"""
Driver program.
Demonstrates the functionality of the multiple classes, and how they can be used.
Allows user to enter a file storing song data, and then allows the user to manipulate this data
"""


def get_valid_filename():
    """Method to Ensure that entered filename is valid, by checking if the file exists.\n
    Returns: str: the name of the file"""

    filename = input("Please enter the name of the file containing song data (format - example.csv): ")
    while True:
        try:
            with open(filename, "r") as file:
                print("File successfully opened!")
                break
        except FileNotFoundError:
            print("Cannot find file!")
            filename = input("Please enter the name of the file containing song data (format - example.csv): ")
    return filename


def get_valid_filter_data():
    """Method to ensure user enters valid data for the filter_by method in SongDatabase class.\n
    Returns: filter_type (str): the verified filter type
    filter_value (str): the filter value"""

    print("Please enter the attribute by which you would like to filter... ")
    filter_type = input("Must be one of five attributes - Title, Artist, Album, Year, or Genre: ")
    while filter_type not in ["Title", "Artist", "Album", "Year", "Genre"]:
        print("Please enter the attribute by which you would like to filter... ")
        filter_type = input("Must be one of five values - Title, Artist, Album, Year, or Genre: ")

    print("Please enter the value you are searching for...")
    filter_value = input("Value to filter by: ")

    return filter_type, filter_value


def get_song_data():
    """Method to prompt the user for the necessary data to create a Song object.\n
    Returns: title (str): the name of the song\n
    artist (str): the artist who performs the song\n
    album (str): the album which the song belongs to\n
    year (int): the release year for the project
    genre (str): the genre by which the song is identified"""

    print("Please enter the following data in order to create a new song entry:")
    title = input("Song Title: ")
    artist = input("Artist: ")
    album = input("Album: ")
    year = input("Year of Release: ")
    genre = input("Genre: ")
    return title, artist, album, year, genre


def action(db):
    """Method to prompt and facilitate for actions on the passed song database"""
    while True:
        print(
            "What action would you like to perform on the song database?")
        print("1. Filter the database\n",
              "2. Sort the database\n",
              "3. Add a song to the database\n",
              "4. Exit the program")
        option = input("(Please enter the corresponding digit): ")

        if option == "1":
            # Allow user to perform filtering on the song database
            print("Now performing filtering on the song database:")
            filter_type, filter_value = get_valid_filter_data()
            db.filter_by(filter_type, filter_value)
            db.display()
        elif option == "2":
            # allow the user to sort the song database
            print("Sorting the database in alphabetical order, based on Title")
            db.sort()
            db.display()
        elif option == "3":
            # allow the user to add a new song into the database
            print("Adding a new song to the database:")
            title, artist, album, year, genre = get_song_data()
            db.add_song(Song(title, artist, album, year, genre))
            db.display()
        elif option == "4":
            break
        else:
            print("Invalid action!")


if __name__ == '__main__':
    # Create a song database object from some file
    db1 = SongDatabase(get_valid_filename())
    db1.display()  # display the song database object to the user

    action(db1)  # call method to prompt user to make actions with the song database
