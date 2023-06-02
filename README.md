# Song-Database-Application
Console based song database application, programmed using Python. Supports some of the essential functionalities typical of a song database: reading and loading song data from a csv file, displaying songs in a table, filtering + sorting songs, and adding songs to the collection.

# Class Structure and Description:
My solution comprises of three classes which work together to implement the functionalities discussed in the above section.

# Song class
The purpose of the Song class is to represent a simple song object, with the attributes of song title, artist, album, release year, and genre. 
The class provides some functionalities, such as all necessary getters and setters, __str__ method to return a brief description of the song object and overriding of the larger than operator to support the sorting of songs by their title (as will be discussed later).
The class serves as a component of the SongCollection class.

# SongCollection
The purpose of the class is to represent a simple collection of songs. 
The class behaves in the same manner as a list – it inherits the list class and adds on functionalities such as getters and setters.
There is a composition relationship between the Song and SongCollection classes. The Song is a component of SongCollection – the constructor for the SongCollection class receives a list of Song objects and stores it in itself.

# SongDatabase
The purpose of this class is to read song data from a file, load the songs into a SongCollection object, and manipulate this object.
The class supports functionalities such as reading from a file, writing to a file, printing out data about the database in a tabular manner, manipulating the data through filtering and sorting, and the ability to add new songs to the database.
The class is a composition relationship between this class and the Song and SongCollection classes. The latter classes are both components of the SongDatabase class. The SongCollection object declared inside the SongDatabase class stores the songs in the database. The Song class allows us to declare new songs, and add them to the database.

# Special Functions/Algorithms used
One of the more interesting functions implemented in this program is the filter_by method.
The filter_by method filters the SongCollection instance in the SongDatabase, according to a set of parameters passed to the function. The user has the ability to sort the song collection by any attribute they wish (be it song title, artist, album, release year, or genre). This is implemented through calling a different filtering algorithm for each different attribute (for example, if user passes “Artist” as attribute, then the filtering algorithm will check if the user passed value is equal to the song’s artist)
The filtering itself is done efficiently by iterating through each song in the song collection list and checking if the attribute of the song is equal to the user passed attribute value. If that is the case, then the current song remains in the song collection, whilst other songs that do not have matching attributes are omitted.
After finishing with the filtering of the list, the method makes a call to the save_songs method of SongDatabase, which writes data to the file associated with the song database. Thus, the data in the file now only includes the filtered songs.

# How to start and work with the program
The main.py program is the driver program for my application. Thus, the user must run this program to start the application.
Upon running the program, the user will be prompted for the name of a csv file, that contains song data to be loaded into a song database. The format of the csv file must be the following:
The first line should be a header line...
ex. "Title,Artist,Album,Year,Genre"
The lines to follow should include song data, following the same format as the one above. For example, here is the format under which “Hotel California” by the Eagles would appear in the file, in its own row...
"Hotel California,The Eagles,Hotel California,1976,Rock"
Once the user has entered a valid file name, with valid data inside, the action method is called. This method offers the user four choices for operation – filter the database, sort the database, add a song, or terminate the program.
Based on what choice the user enters, the program walks them through the necessary steps in performing filtering, adding a song, etc.
