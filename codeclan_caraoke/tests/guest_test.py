import unittest

from classes.guest import Guest
from classes.song import Song
from classes.room import Room

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Joanne", "Like a Prayer", 47)
        self.guest2 = Guest("Jane", "...Baby One More Time", 19)
        self.guest3 = Guest("Julie", "Dirrty", 35)
        self.guest4 = Guest("Jackie", "Toxic", 45)
        self.guest5 = Guest("Jamie", "Hung Up", 86)

        self.song1 = Song("I'm a Slave 4 u", "Britney Spears")
        self.song2 = Song("Toxic", "Britney Spears")
        self.song3 = Song("...Baby One More Time", "Britney Spears")
        self.song4 = Song("Dirrty", "Christina Aguilera")
        self.song5 = Song("Genie in a Bottle", "Christina Aguilera")
        self.song6 = Song("Beautiful", "Christina Aguilera")
        self.song7 = Song("Like a Prayer", "Madonna")
        self.song8 = Song("Hung Up", "Madonna")
        self.song9 = Song("Material Girl", "Madonna")

        self.room1 = Room("Britney Room", 12, [self.song1, self.song2, self.song3], [], 90)
        self.room2 = Room("Christina Room", 6, [self.song4, self.song5, self.song6], [], 50)
        self.room3 = Room("Madonna Room", 10, [self.song7, self.song8, self.song9], [], 35)
        self.room4 = Room("Other Room", 2, [], [self.guest4, self.guest5], 15)

    def test_guest_has_name(self):
        self.assertEqual("Jackie", self.guest4.name)
    
    def test_guest_has_favourite_song(self):
        self.assertEqual("Dirrty", self.guest3.favourite_song)

    def test_guest_react_to_fave_song__positive(self):
        self.guest2.guest_react_to_fave_song(self.room1)
        # check guest favourite song in room
        # then guest can respond positively if it is, or negitively if not
        self.assertEqual("Yassss put it on! I know allll the words!!", self.guest2.guest_react_to_fave_song(self.room1))

    def test_guest_react_to_fave_song__negative(self):
        self.guest1.guest_react_to_fave_song(self.room2)
        self.assertEqual("Booooooo that's rubbish", self.guest1.guest_react_to_fave_song(self.room2))