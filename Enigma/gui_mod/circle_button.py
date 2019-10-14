"""circle_button.py file"""

# Python module(s)
import pygame as pyg

# Environment variable(s)
from ..env import BACKGROUND_COLOR


class CircleButton:
    """Class to manage circular buttons

    Args:
        test (str): Text to display
        pos (tuple): 2 Elements describing position of button in (left, top) format
        radius (int): Radius of the button
        border (tuple): RGB color value for border color
        hover (tuple): RGB color value for hover color
        high_light (tuple): RGB color value for button press color"""

    def __init__(
        self,
        text,
        pos,
        radius=10,
        border=(0, 0, 0),
        background=BACKGROUND_COLOR,
        hover=BACKGROUND_COLOR,
        high_light=BACKGROUND_COLOR,
        static=True,
    ):
        self.text = text
        self.left = pos[0]
        self.top = pos[1]
        self.radius = radius
        self.background = background
        self.border = border
        self.hover = hover
        self.high_light = high_light
        self.static = static
        self.diameter = self.radius * 2
        self.fontname = "Arial"
        self.fontsize = int(self.radius * 1.5)
        self.mouse_over = False
        self.mouse_down = False
        self.mouse = "off"
        self.clicked = False
        self.font = pyg.font.SysFont(self.fontname, self.fontsize)
        self.text_width, self.text_height = pyg.font.Font.size(self.font, self.text)
        self.buttonUP = pyg.Surface((self.diameter, self.diameter))
        self.buttonDOWN = pyg.Surface((self.diameter, self.diameter))
        self.buttonHOVER = pyg.Surface((self.diameter, self.diameter))
        self.__update__()

    def draw_this_button(self, button_surface, color):
        """Draws button from supplied button_surface argument

        Args:
            button_surface(pygame.Surface): Surface to draw button on
            color(tuple): RGB for normal color of the button"""
        center = (self.radius, self.radius)
        button_surface.fill(self.background)
        pyg.draw.circle(button_surface, self.border, center, self.radius, 2)
        pyg.draw.circle(button_surface, color, center, self.radius - 2, 0)
        button_surface.blit(
            self.font.render(self.text, False, (0, 0, 0)),
            (self.radius - (self.text_width / 2), self.radius - (self.text_height / 2)),
        )

    def __update__(self, background=None):
        """Updates the button

        Args:
            background(tuple): RGB for normal background of the button"""
        background = self.background if background is None else background
        self.draw_this_button(self.buttonUP, background)
        self.draw_this_button(self.buttonDOWN, self.high_light)
        self.draw_this_button(self.buttonHOVER, self.hover)

    def draw(self, surface):
        """Draws circular button of self object on supplied surface

        Args:
            surface(pygame.Surface): Surface to draw button on"""
        if not self.static:
            self.__mouse_check__()
        if self.mouse == "off":
            surface.blit(self.buttonUP, (self.left, self.top))
        elif self.mouse == "hover":
            surface.blit(self.buttonHOVER, (self.left, self.top))
        elif self.mouse == "down":
            surface.blit(self.buttonDOWN, (self.left, self.top))

    def __mouse_check__(self):
        """Check mouse action with respect to this button"""
        _1, _2, _3 = pyg.mouse.get_pressed()
        mouse_x, mouse_y = pyg.mouse.get_pos()
        left = self.left + self.radius
        top = self.top + self.radius
        if not _1:
            self.mouse = "off"
        if (
            (mouse_x - left) ** 2 + (mouse_y - top) ** 2 - self.radius ** 2
        ) < 0 and not self.mouse == "down":
            self.mouse = "hover"
        if not self.mouse_down and _1 and self.mouse == "hover":
            self.mouse = "down"
            self.clicked = True
        if self.mouse == "off":
            self.clicked = False

    def click(self):
        """Checks if button is pressed

        Returns:
            bool : True if button is pressed"""
        _1, _2, _3 = pyg.mouse.get_pressed()
        mouse_x, mouse_y = pyg.mouse.get_pos()
        if (
            ((mouse_x - self.left) ** 2 + (mouse_y - self.top) ** 2 - self.radius ** 2)
            > 0
            and self.clicked
            and not _1
        ):
            self.clicked = False
            return True
        else:
            return False
