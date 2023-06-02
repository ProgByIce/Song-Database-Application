import unittest
import os
import csv
from SongDatabase import SongDatabase
from Song import Song
from SongCollection import SongCollection


class TestSongDatabase(unittest.TestCase):
    def setUp(self):
        self.filename = "test_songs.csv"
        with open(self.filename, "w", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Title', "Artist", "Album", "Year", "Genre"])
            csv_writer.writerow(['song1', 'artist1', 'album1', '2000', 'pop'])
            csv_writer.writerow(['song2', 'artist2', 'album2', '1995', 'rock'])
        self.db = SongDatabase(self.filename)

    def tearDown(self):
        os.remove(self.filename)

    def test_set_filename(self):
        self.db.set_filename("new_test_songs.csv")
        self.assertEqual(self.db.filename, "new_test_songs.csv")

    def test_set_song_collection(self):
        self.assertIsInstance(self.db.song_collection, SongCollection)
        self.assertEqual(len(self.db.song_collection), 2)
        self.assertEqual(self.db.song_collection[0].__str__(),
                         Song('song1', 'artist1', 'album1', '2000', 'pop').__str__())

    def test_save_songs(self):
        new_song = Song('song3', 'artist3', 'album3', '2003', 'pop')
        self.db.add_song(new_song)
        self.assertEqual(len(self.db.song_collection), 3)
        with open(self.filename, "r") as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=",")
            self.assertEqual(len(list(csv_reader)), 4)

    def test_add_song(self):
        new_song = Song('song3', 'artist3', 'album3', '2003', 'pop')
        self.db.add_song(new_song)
        self.assertEqual(len(self.db.song_collection), 3)
        self.assertEqual(self.db.song_collection[-1], new_song)

    def test_filter_by(self):
        self.db.filter_by("Title", "song1")
        self.assertEqual(len(self.db.song_collection), 1)
        self.assertEqual(self.db.song_collection[0].__str__(),
                         Song('song1', 'artist1', 'album1', '2000', 'pop').__str__())


if __name__ == '__main__':
    unittest.main()
