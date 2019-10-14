"""rec_button.py file"""

# Python module(s)
import pygame as pyg


class RectangularButton:
    """Class for Rectangular buttons

    Args:
        test (str): Text to display
        pos (tuple): 2 Elements describing position of button in (left, top) format
        dim (tuple): 2 Elements describing dimention of button in (width, height) format
        background (tuple): RGB for background color
        border (tuple): RGB for border color
        hover (tuple): RGB for highlight color on hover
        rotate (int): Number of degress to roate counter-clockwise"""

    def __init__(
        self,
        text="",
        pos=(10, 30),
        dim=(None, 20),
        background=(255, 0, 0),
        border=(255, 0, 0),
        hover=(255, 0, 0),
        rotate=0,
    ):
        self.text = text
        self.left = pos[0]
        self.top = pos[1]
        self.height = dim[1]
        self.width = dim[0]
        self.colour1 = background
        self.border = border
        self.colour3 = hover
        self.colour4 = (225, 243, 252)
        self.rotate = rotate
        self.fontname = "Arial"
        self.fontsize = self.height - 6
        self.mouse_over = False
        self.mouse_down = False
        self.mouse = "off"
        self.clicked = False
        self.font = pyg.font.SysFont(self.fontname, self.fontsize)
        self.text_width, self.text_height = pyg.font.Font.size(self.font, self.text)
        self.width_type = "user"
        self.buttonUP = pyg.Surface((self.width, self.height))
        self.buttonDOWN = pyg.Surface((self.width, self.height))
        self.buttonHOVER = pyg.Surface((self.width, self.height))
        self.__update__()

    def __update__(self):
        """Updates button"""
        # Normal button
        self.buttonUP.fill(self.colour1)
        pyg.draw.rect(
            self.buttonUP, self.colour1, (0, 0, self.width - 2, self.height - 2), 0
        )
        pyg.draw.rect(self.buttonUP, self.border, (0, 0, self.width, self.height), 2)
        self.buttonUP.blit(
            self.font.render(self.text, False, (0, 0, 0)),
            (
                (self.width / 2) - (self.text_width / 2),
                (self.height / 2) - (self.text_height / 2),
            ),
        )
        self.buttonUP = pyg.transform.rotate(self.buttonUP, self.rotate)

        # hover
        self.buttonHOVER.fill(self.colour3)
        pyg.draw.rect(
            self.buttonHOVER, self.colour4, (0, 0, self.width - 2, self.height - 2), 0
        )
        pyg.draw.rect(self.buttonHOVER, self.border, (0, 0, self.width, self.height), 2)
        self.buttonHOVER.blit(
            self.font.render(self.text, False, (0, 0, 0)),
            (
                (self.width / 2) - (self.text_width / 2),
                (self.height / 2) - (self.text_height / 2),
            ),
        )
        self.buttonHOVER = pyg.transform.rotate(self.buttonHOVER, self.rotate)

        # down
        self.buttonDOWN.fill(self.colour3)
        pyg.draw.rect(
            self.buttonDOWN, self.colour4, (0, 0, self.width - 2, self.height - 2), 0
        )
        pyg.draw.rect(self.buttonDOWN, self.border, (0, 0, self.width, self.height), 2)
        self.buttonDOWN.blit(
            self.font.render(self.text, False, (0, 0, 0)),
            (
                (self.width / 2) - (self.text_width / 2) + 1,
                (self.height / 2) - (self.text_height / 2),
            ),
        )
        self.buttonDOWN = pyg.transform.rotate(self.buttonDOWN, self.rotate)

    def draw(self, surface):
        """Draws button on supplied surface

        Args:
            surface (pygame.Surface): Surface to draw on"""
        self.__mouse_check__()
        if self.mouse == "hover":
            surface.blit(self.buttonHOVER, (self.left, self.top))
        elif self.mouse == "off":
            surface.blit(self.buttonUP, (self.left, self.top))
        elif self.mouse == "down":
            surface.blit(self.buttonDOWN, (self.left, self.top))

    def __mouse_check__(self):
        """Checks mouse action with respect to button"""
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
        """Button click status

        Returns:
            bool : Wheather button is pressed or not"""
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
