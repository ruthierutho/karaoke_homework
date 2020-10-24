import unittest

from classes.room import *
from classes.song import *
from classes.guest import *
from classes.karaoke_bar import *


class TestKaraokeBar(unittest.TestCase):

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

        
        self.guest1 = Guest("Joanne", "Like a Prayer", 47),
        self.guest2 = Guest("Jane", "...Baby One More Time", 19),
        self.guest3 = Guest("Julie", "Dirrty", 35),
        self.guest4 = Guest("Jackie", "Toxic", 45),
        self.guest5 = Guest("Jamie", "Hung Up", 86)

        self.guests = [self.guest1, self.guest2, self.guest3, self.guest4, self.guest5]

     
        self.room1 = Room("Britney Room", 12, [self.song1, self.song2, self.song3]),
        self.room2 = Room("Christina Room", 6, [self.song4, self.song5, self.song6]),
        self.room3 = Room("Madonna Room", 10, [self.song7, self.song8, self.song9])

        self.rooms = [self.room1, self.room2, self.room3]

        self.karaoke_bar = Karaoke_Bar("Pop Paradise", self.guests, self.rooms)

    def test_karaoke_bar_has_name(self):
        self.assertEqual("Pop Paradise", self.karaoke_bar.name)

    def test_karaoke_bar_has_guests(self):
        print(self.karaoke_bar.guests.name)
