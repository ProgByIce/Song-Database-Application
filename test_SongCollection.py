import unittest
from Song import Song
from SongCollection import SongCollection


class TestSongCollection(unittest.TestCase):
    def setUp(self):
        song1 = Song("Hey Jude", "The Beatles", "Hey Jude", 1968, "Rock")
        song2 = Song("Stairway to Heaven", "Led Zeppelin", "Led Zeppelin IV", 1971, "Rock")
        song3 = Song("Bohemian Rhapsody", "Queen", "A Night at the Opera", 1975, "Rock")
        self.song_collection = SongCollection([song1, song2, song3])

    def test_get_songs(self):
        songs = self.song_collection.get_songs()
        self.assertEqual(len(songs), 3)
        self.assertEqual(songs[0].get_title(), "Hey Jude")
        self.assertEqual(songs[0].get_artist(), "The Beatles")
        self.assertEqual(songs[0].get_album(), "Hey Jude")
        self.assertEqual(songs[0].get_year(), 1968)
        self.assertEqual(songs[0].get_genre(), "Rock")
        self.assertEqual(songs[1].get_title(), "Stairway to Heaven")
        self.assertEqual(songs[1].get_artist(), "Led Zeppelin")
        self.assertEqual(songs[1].get_album(), "Led Zeppelin IV")
        self.assertEqual(songs[1].get_year(), 1971)
        self.assertEqual(songs[1].get_genre(), "Rock")
        self.assertEqual(songs[2].get_title(), "Bohemian Rhapsody")
        self.assertEqual(songs[2].get_artist(), "Queen")
        self.assertEqual(songs[2].get_album(), "A Night at the Opera")
        self.assertEqual(songs[2].get_year(), 1975)
        self.assertEqual(songs[2].get_genre(), "Rock")

    def test_set_songs(self):
        song1 = Song("Hey Jude", "The Beatles", "Hey Jude", 1968, "Rock")
        song2 = Song("Bohemian Rhapsody", "Queen", "A Night at the Opera", 1975, "Rock")
        song3 = Song("Stairway to Heaven", "Led Zeppelin", "Led Zeppelin IV", 1971, "Rock")
        song_collection = SongCollection([song1, song2, song3])
        songs = song_collection.get_songs()
        self.assertEqual(songs, [song1, song2, song3])


if __name__ == '__main__':
    unittest.main()
