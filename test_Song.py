import unittest
from Song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Hey Jude", "The Beatles", "Hey Jude", 1968, "Rock")

    def test_set_title(self):
        self.song.set_title("Let It Be")
        self.assertEqual(self.song.get_title(), "Let It Be")

    def test_set_artist(self):
        self.song.set_artist("John Lennon")
        self.assertEqual(self.song.get_artist(), "John Lennon")

    def test_set_album(self):
        self.song.set_album("Let It Be")
        self.assertEqual(self.song.get_album(), "Let It Be")

    def test_set_year(self):
        self.song.set_year(1970)
        self.assertEqual(self.song.get_year(), 1970)

    def test_set_genre(self):
        self.song.set_genre("Pop")
        self.assertEqual(self.song.get_genre(), "Pop")

    def test_get_title(self):
        self.assertEqual(self.song.get_title(), "Hey Jude")

    def test_get_artist(self):
        self.assertEqual(self.song.get_artist(), "The Beatles")

    def test_get_album(self):
        self.assertEqual(self.song.get_album(), "Hey Jude")

    def test_get_year(self):
        self.assertEqual(self.song.get_year(), 1968)

    def test_get_genre(self):
        self.assertEqual(self.song.get_genre(), "Rock")

    def test_str(self):
        self.assertEqual(str(self.song), "Hey Jude by The Beatles (Hey Jude, 1968)")

    def test_lt(self):
        song2 = Song("Let It Be", "The Beatles", "Let It Be", 1970, "Rock")
        self.assertTrue(self.song < song2)
        self.assertFalse(song2 < self.song)


if __name__ == '__main__':
    unittest.main()
