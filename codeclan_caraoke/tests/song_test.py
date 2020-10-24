import unittest

from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("I'm a Slave 4 u", "Britney Spears")
        self.song2 = Song("Toxic", "Britney Spears")
        self.song3 = Song("...Baby One More Time", "Britney Spears")
        self.song4 = Song("Dirrty", "Christina Aguilera")
        self.song5 = Song("Genie in a Bottle", "Christina Aguilera")
        self.song6 = Song("Beautiful", "Christina Aguilera")
        self.song7 = Song("Like a Prayer", "Madonna")
        self.song8 = Song("Hung Up", "Madonna")
        self.song9 = Song("Material Girl", "Madonna")
    
    def test_song_has_title(self):
        self.assertEqual("Toxic", self.song2.title)

    def test_song_has_artist(self):
        self.assertEqual("Christina Aguilera", self.song6.artist)