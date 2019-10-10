__author__ = "Kartikei Mittal"
__version__ = "0.1d"
__description__ = "Welcome to Enigma simulator by {}, version {}".format(
    __author__, __version__
)

print(__description__)
from .enigma import Enigma
from .anim import Animation
