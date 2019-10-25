""""""

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
