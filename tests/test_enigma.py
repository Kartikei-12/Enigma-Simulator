"""Testing Enigma/enigma.py file"""

# Python module(s)
import unittest

# Project Module(s)
from Enigma import Enigma


class EnigmaTest(unittest.TestCase):
    """Enigma Test class"""

    def setUp(self):
        """Setup Method"""
        self.en_obj = Enigma(save_config=True)

    def tearDown(self):
        """Tear Down Method"""
        del self.en_obj

    def test_complete_process(self):
        """Testing complete process"""
        plain = "HELLO WORLD THIS IS TEST METHOD FOR ENIGMA"
        cipher = self.en_obj.process(plain)
        self.en_obj.reset_from_config_dict()
        plain_again = self.en_obj.process(cipher)
        self.assertEqual(plain, plain_again)

    def test_load_config(self):
        """Testing load_config method"""
        c_dict = self.en_obj.load_config()
        self.assertIsInstance(c_dict, dict)
        self.assertEqual(c_dict["n_rotors"], 3)

    def test_rotate_rotor(self):
        """Testing rotate rotor method"""
        for r in self.en_obj.rotors:
            r.pos = self.en_obj.alpha_len - 1
        self.en_obj.rotate_rotor(0)
        self.assertEqual(self.en_obj.rotors[0].pos, 0)
        self.assertEqual(self.en_obj.rotors[1].pos, 0)

    def test_process_char(self):
        """Testing complete process for single chracter"""
        in_char = "A"
        out_char, char_list = self.en_obj.process_char(in_char)
        self.assertEqual(len(char_list), 14)
