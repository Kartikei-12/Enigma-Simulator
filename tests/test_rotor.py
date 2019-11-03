"""Testing Enigma/rotor.py file"""

# Python module(s)
import unittest

# Project Module(s)
from Enigma import Rotor


class RotorTest(unittest.TestCase):
    """Rotor Test class"""

    def setUp(self):
        """Setup Method"""
        self.rotor = Rotor()

    def tearDown(self):
        """Tear Down Method"""
        del self.rotor

    def test_move(self):
        """Testing move method"""
        self.rotor.pos = 1
        self.assertEqual(self.rotor.move("A"), "B")
        self.rotor.pos = 2
        self.assertEqual(self.rotor.move("A"), "C")
        self.rotor.pos = 1
        self.assertEqual(self.rotor.move("A", -1), "Z")
        self.rotor.pos = 2
        self.assertEqual(self.rotor.move("A", -1), "Y")

    def test___getitem__(self):
        """Testing overloaded [] operator"""
        char = self.rotor["A"]
        string = self.rotor["ABCD"]
        self.assertIsInstance(char, str)
        self.assertIsInstance(string, list)
        self.assertEqual(len(char), 1)
        self.assertEqual(len(string), 4)

    def test_rotate(self):
        """Testing rotate command"""
        self.rotor.pos = 25
        self.rotor.rotate()
        self.assertEqual(self.rotor.pos, 0)
        self.rotor.pos = 24
        self.rotor.rotate()
        self.assertEqual(self.rotor.pos, 25)
        self.rotor.pos = 24
        self.rotor.rotate(2)
        self.assertEqual(self.rotor.pos, 0)

    def test_generate_rotor_board_direct(self):
        """Testing generate_rotor_board"""
        rotor_dict = self.rotor.generate_rotor_board()
        self.assertIsInstance(rotor_dict, dict)
        self.assertEqual("A", rotor_dict[rotor_dict["A"]])

    def test_generate_rotor_board(self):
        """Testing generate_rotor_board"""
        self.rotor.alphabet = ["A", "B", "C", "D", "E"]
        rotor_dict = self.rotor.generate_rotor_board()
        self.assertEqual("A", rotor_dict["A"])

    def test_generate_rotor_board_non_reflection(self):
        """Testing generate_rotor_board"""
        rotor_dict = self.rotor.generate_rotor_board_non_reflection()
        self.assertIsInstance(rotor_dict, dict)
        self.assertNotEqual("A", rotor_dict["A"])
