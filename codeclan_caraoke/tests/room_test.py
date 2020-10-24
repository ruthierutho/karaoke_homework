import unittest
from classes.room import *


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("Britney Room", 12, [["I'm a Slave 4 u", "Britney Spears"], ["Toxic", "Britney Spears"], ["...Baby One More Time", "Britney Spears"]])
        self.room2 = Room("Christina Room", 6, [["Dirrty", "Christina Aguilera"], ["Genie in a Bottle", "Christina Aguilera"], ["Beautiful", "Christina Aguilera"]])
        self.room3 = Room("Madonna Room", 10, [["Like a Prayer", "Madonna"], ["Hung Up", "Madonna"], ["Material Girl", "Madonna"]])

    def test_room_has_name(self):
        self.assertEqual("Britney Room", self.room1.name)
