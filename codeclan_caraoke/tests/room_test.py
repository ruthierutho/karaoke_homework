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

        self.guest1 = Guest("Joanne", "Like a Prayer", 47)
        self.guest2 = Guest("Jane", "...Baby One More Time", 19)
        self.guest3 = Guest("Julie", "Dirrty", 35)
        self.guest4 = Guest("Jackie", "Toxic", 45)
        self.guest5 = Guest("Jamie", "Hung Up", 86)

        self.room1 = Room("Britney Room", 12, [self.song1, self.song2, self.song3], [])
        self.room2 = Room("Christina Room", 6, [self.song4, self.song5, self.song6], [])
        self.room3 = Room("Madonna Room", 10, [self.song7, self.song8, self.song9], [])
        self.room4 = Room("Other Room", 2, [], [self.guest4, self.guest5])

       

    def test_room_has_name(self):
        self.assertEqual("Britney Room", self.room1.name)

    def test_room_capacity(self):
        self.assertEqual(10, self.room3.capacity)

    def test_room_has_song(self):
        self.assertEqual("Material Girl", self.room3.songs[2].title)

    def test_add_song_to_room(self):
        self.room4.add_song_to_room(self.room4, self.song8)
        self.assertEqual("Hung Up", self.room4.songs[0].title)
        # self.assertEqual(1, len(self.room4.songs))
        
    def test_how_many_songs_in_room(self):
        self.assertEqual(3, len(self.room1.songs))
    
    def test_find_song_in_room_by_title(self):
        self.assertEqual(self.room1.songs[1].title, self.room1.find_song_in_room_by_title("Toxic"))

    def test_if_song_is_in_room__True(self):
        self.assertEqual(True, self.room2.song_in_room(self.song5))

    def test_if_song_is_in_room__False(self):
        self.assertEqual(False, self.room2.song_in_room(self.song7))

    def test_add_guest_to_room(self):
        self.room1.add_guest_to_room(self.guest2)
        self.assertEqual("Jane", self.room1.guests[0].name)

    # def test_remove_guest_from_room(self):
    #     self.
