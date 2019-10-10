""""""

import pygame as pyg


class RectangularButton:
    """"""

    def __init__(
        self,
        text="",
        left=10,
        top=30,
        width=None,
        height=20,
        background=(255, 0, 0),
        border=(255, 0, 0),
        hover=(255, 0, 0),
    ):
        self.text = text
        self.left = left
        self.top = top
        self.height = height
        self.colour1 = background
        self.colour2 = border
        self.colour3 = hover
        self.colour4 = (225, 243, 252)
        self.fontname = "Arial"
        self.fontsize = self.height - 6
        self.mouse_over = False
        self.mouse_down = False
        self.mouse = "off"
        self.clicked = False
        self.font = pyg.font.SysFont(self.fontname, self.fontsize)
        self.text_width, self.text_height = pyg.font.Font.size(self.font, self.text)
        if width == None:
            self.width = self.text_width + 20
            self.width_type = "text"
        else:
            self.width = width
            self.width_type = "user"
        self.buttonUP = pyg.Surface((self.width, self.height))
        self.buttonDOWN = pyg.Surface((self.width, self.height))
        self.buttonHOVER = pyg.Surface((self.width, self.height))
        self.__update__()

    def __update__(self):
        """"""
        self.buttonUP.fill(self.colour1)
        pyg.draw.rect(
            self.buttonUP, self.colour1, (0, 0, self.width, self.height / 2), 0
        )
        pyg.draw.line(self.buttonUP, self.colour2, (2, 0), (self.width - 3, 0), 1)
        pyg.draw.line(
            self.buttonUP,
            self.colour2,
            (2, self.height - 1),
            (self.width - 3, self.height - 1),
            1,
        )
        pyg.draw.line(self.buttonUP, self.colour2, (0, 2), (0, self.height - 3), 1)
        pyg.draw.line(
            self.buttonUP,
            self.colour2,
            (self.width - 1, 2),
            (self.width - 1, self.height - 3),
            1,
        )
        self.buttonUP.blit(
            self.font.render(self.text, False, (0, 0, 0)),
            (
                (self.width / 2) - (self.text_width / 2),
                (self.height / 2) - (self.text_height / 2),
            ),
        )
        # hover
        self.buttonHOVER.fill(self.colour3)
        pyg.draw.rect(
            self.buttonHOVER, self.colour4, (0, 0, self.width, self.height / 2), 0
        )
        pyg.draw.line(self.buttonHOVER, self.colour2, (2, 0), (self.width - 3, 0), 1)
        pyg.draw.line(
            self.buttonHOVER,
            self.colour2,
            (2, self.height - 1),
            (self.width - 3, self.height - 1),
            1,
        )
        pyg.draw.line(
            self.buttonHOVER,
            self.colour4,
            (2, self.height - 2),
            (self.width - 3, self.height - 2),
            1,
        )
        pyg.draw.line(self.buttonHOVER, self.colour2, (0, 2), (0, self.height - 3), 1)
        pyg.draw.line(self.buttonHOVER, self.colour4, (1, 2), (1, self.height - 3), 2)
        pyg.draw.line(
            self.buttonHOVER,
            self.colour2,
            (self.width - 1, 2),
            (self.width - 1, self.height - 3),
            1,
        )
        self.buttonHOVER.blit(
            self.font.render(self.text, False, (0, 0, 0)),
            (
                (self.width / 2) - (self.text_width / 2),
                (self.height / 2) - (self.text_height / 2),
            ),
        )
        # down
        self.buttonDOWN.fill(self.colour3)
        pyg.draw.rect(
            self.buttonDOWN, self.colour4, (0, 0, self.width, self.height / 2), 0
        )
        pyg.draw.line(self.buttonDOWN, self.colour2, (2, 0), (self.width - 3, 0), 1)
        pyg.draw.line(self.buttonDOWN, self.colour3, (2, 1), (self.width - 3, 1), 2)
        pyg.draw.line(
            self.buttonDOWN,
            self.colour2,
            (2, self.height - 1),
            (self.width - 3, self.height - 1),
            1,
        )
        pyg.draw.line(self.buttonDOWN, self.colour2, (0, 2), (0, self.height - 3), 1)
        pyg.draw.line(self.buttonDOWN, self.colour2, (1, 2), (1, self.height - 3), 2)
        pyg.draw.line(
            self.buttonDOWN,
            self.colour2,
            (self.width - 1, 2),
            (self.width - 1, self.height - 3),
            1,
        )
        self.buttonDOWN.blit(
            self.font.render(self.text, False, (0, 0, 0)),
            (
                (self.width / 2) - (self.text_width / 2) + 1,
                (self.height / 2) - (self.text_height / 2),
            ),
        )

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
        if not _1:
            self.mouse = "off"
        if (
            mouse_x > self.left
            and mouse_x < self.left + self.width
            and mouse_y > self.top
            and mouse_y < self.top + self.height
            and not self.mouse == "down"
        ):
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
            mouse_x > self.left
            and mouse_x < self.left + self.width
            and mouse_y > self.top
            and mouse_y < self.top + self.height
            and self.clicked
            and not _1
        ):
            self.clicked = False
            return True
        else:
            return False
