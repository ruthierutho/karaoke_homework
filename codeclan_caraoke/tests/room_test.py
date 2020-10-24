import unittest
from classes.room import *
from classes.song import *
from classes.guest import *


class TestRoom(unittest.TestCase):

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

        self.room1 = Room("Britney Room", 12, [self.song1, self.song2, self.song3])
        self.room2 = Room("Christina Room", 6, [self.song4, self.song5, self.song6])
        self.room3 = Room("Madonna Room", 10, [self.song7, self.song8, self.song9])
        self.room4 = Room("Other Room", 2, [])

    def test_room_has_name(self):
        self.assertEqual("Britney Room", self.room1.name)

    def test_room_capacity(self):
        self.assertEqual(10, self.room3.capacity)

    def test_room_has_song(self):
        self.assertEqual("Material Girl", self.room3.songs[2].title)

    # def test_add_song_to_room(self):
    #     self.room4.add_song_to_room(self.room4, self.song9)
    #     self.assertEqual(1, len(self.room4.songs))
        