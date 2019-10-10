""""""

import pygame as pyg


class CircleButton:
    """"""

    def __init__(
        self,
        text="",
        left=10,
        top=30,
        radius=10,
        background=(0, 0, 255),
        border=(0, 255, 0),
        hover=(255, 0, 0),
        high_light=(100, 100, 100),
    ):
        self.text = text
        self.left = left
        self.top = top
        self.radius = radius
        self.background = background
        self.border = border
        self.hover = hover
        self.high_light = high_light
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
        """"""
        center = (self.radius, self.radius)
        button_surface.fill(self.background)
        pyg.draw.circle(button_surface, self.border, center, self.radius, 2)
        pyg.draw.circle(button_surface, color, center, self.radius - 2, 0)
        button_surface.blit(
            self.font.render(self.text, False, (0, 0, 0)),
            (self.radius - (self.text_width / 2), self.radius - (self.text_height / 2)),
        )

    def __update__(self):
        """"""
        self.draw_this_button(self.buttonUP, self.background)
        self.draw_this_button(self.buttonDOWN, self.high_light)
        self.draw_this_button(self.buttonHOVER, self.hover)

    def draw(self, surface):
        """"""
        self.__mouse_check__()
        if self.mouse == "hover":
            surface.blit(self.buttonHOVER, (self.left, self.top))
        elif self.mouse == "off":
            surface.blit(self.buttonUP, (self.left, self.top))
        elif self.mouse == "down":
            surface.blit(self.buttonDOWN, (self.left, self.top))

    def __mouse_check__(self):
        """"""
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
        _1, _2, _3 = pyg.mouse.get_pressed()
        mouse_x, mouse_y = pyg.mouse.get_pos()
        if (
            ((mouse_x - self.left) ** 2 + (mouse_y - self.top) ** 2 - self.radius ** 2)
            < 0
            and self.clicked
            and not _1
        ):
            self.clicked = False
            return True
        else:
            return False

    def set_text(self, text, fontname="Arial", fontsize=None):
        self.text = text
        self.fontname = fontname
        if not fontsize == None:
            self.fontsize = fontsize
        self.font = pyg.font.SysFont(self.fontname, self.fontsize)
        self.text_width, self.text_height = pyg.font.Font.size(self.font, self.text)
        self.buttonUP = pyg.Surface((self.radius, self.radius))
        self.buttonDOWN = pyg.Surface((self.radius, self.radius))
        self.buttonHOVER = pyg.Surface((self.radius, self.radius))
        self.__update__()
