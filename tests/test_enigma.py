""""""

# Python module(s)
import unittest

# Project Module(s)
from Enigma import Enigma


class EnigmaTest(unittest.TestCase):
    """Enigma Test class"""

    def setUp(self):
        """Setup Method"""
        self.en_obj = Enigma()

    def tearDown(self):
        """Tear Down Method"""
        del self.en_obj

    def test_complete_process(self):
        """Testing complete process"""
        plain = "HELLO WORLD THIS IS TEST METHOD FOR ENIGMA"
        cipher = self.en_obj.process(plain)
        self.en_obj.reset_config_dict()
        plain_again = self.en_obj.process(cipher)
        self.assertEqual(plain, plain_again)
