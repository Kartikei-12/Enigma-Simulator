"""Testing Enigma/animation.py file"""

# Python module(s)
import unittest

# Project Module(s)
from Enigma import Animation


class AnimationTest(unittest.TestCase):
    """Animation Test class"""

    def setUp(self):
        """Setup Method"""
        self.an = Animation()

    def tearDown(self):
        """Tear Down Method"""
        del self.an

    def test_animation(self):
        """Testing animation"""
        self.an.start(testing=True)
