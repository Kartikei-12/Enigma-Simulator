"""__init__.py file for the project Enigma Simulator"""

__author__ = "Kartikei Mittal"
__version__ = VERSION = "0.1d"
__description__ = "Welcome to Enigma simulator by {}, version {}".format(
    __author__, __version__
)

print(__description__)
from .rotor import Rotor
from .enigma import Enigma
from .anim import Animation
