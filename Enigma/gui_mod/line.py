"""line.py file"""

# Python module(s)
import pygame as pyg

# Environment Variable(s)
from ..env import BLACK, GOLD


class Line:
    """Line class

    Args:
        pos (tuple): Position of line in (left, top) format
        length (int): Length of the line
        color (tuple): RGB for color of the line
        thickness (int): Thickness of the line
        rotate (int): By how many degress to rotate line anti-clockwise"""

    def __init__(self, pos, length, color=BLACK, thinckness=4, rotate=0):
        self.left = pos[0]
        self.top = pos[1]
        self.length = length
        self.color = color
        self.surface = pyg.Surface((length, thinckness))
        self.surface = pyg.transform.rotate(self.surface, rotate)
        self.__update__()

    def __update__(self, active=None):
        """Updates line

        Args:
            active(tuple): New color of the line"""
        color = self.color if active is None else active
        self.surface.fill(color)

    def draw(self, surface):
        """Draws line

        Args:
            surface(pygame.Surface): Surface to draw line on"""
        surface.blit(self.surface, (self.left, self.top))
