"""line.py file"""

# Python module(s)
import pygame as pyg

from ..env import BLACK, GOLD


class Line:
    """"""

    def __init__(
        self,
        pos,
        length,
        color=BLACK,
        # a_color = GOLD,
        thinckness=4,
        rotate=None,
    ):
        self.left = pos[0]
        self.top = pos[1]
        self.length = length
        self.color = color
        # self.a_color = a_color
        self.surface = pyg.Surface((length, thinckness))
        if rotate is not None:
            self.surface = pyg.transform.rotate(self.surface, rotate)
        self.__update__()

    def __update__(self, active=None):
        """"""
        color = self.color if active is None else active
        self.surface.fill(color)

    def draw(self, surface):
        """"""
        surface.blit(self.surface, (self.left, self.top))
