import unittest

from classes.guest import Guest
from classes.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Joanne", "Like a Prayer", 47)
        self.guest2 = Guest("Jane", "...Baby One More Time", 19)
        self.guest3 = Guest("Julie", "Dirrty", 35)
        self.guest4 = Guest("Jackie", "Toxic", 45)
        self.guest5 = Guest("Jamie", "Hung Up", 86)

    def test_guest_has_name(self):
        self.assertEqual("Jackie", self.guest4)
        
    