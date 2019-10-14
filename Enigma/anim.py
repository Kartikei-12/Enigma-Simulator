"""anim.py file"""

# Python Module(s)
import pygame as pyg

# Project Module(s)
from .enigma import Enigma
from .gui_mod.rec_button import RectangularButton
from .gui_mod.circle_button import CircleButton

# Environment Variable(s)
# Other
from .env import ALPHABET

# Color(s)
from .env import BACKGROUND_COLOR, RED, WHITE, BLACK, DARK_GREY, LIGHT_GREY
from .env import TITLE_BAR_COLOR, GOLD

QUIT_EVENT = pyg.QUIT
MOUSEBUTTONDOWN = pyg.MOUSEBUTTONDOWN


class Animation:
    """"""

    def __init__(self):
        pyg.init()
        pyg.display.set_caption("Enigma Simulator")

        # Common variable(s)
        self.active = None
        self.n_rotors = 3
        self.en_obj = Enigma(alphabet=ALPHABET[0:4], n_rotors=self.n_rotors)
        self.alphabet = self.en_obj.alphabet
        self.screen = pyg.display.set_mode((0, 0), pyg.FULLSCREEN)
        self.width, self.height = self.screen.get_size()

        # Title bar Image
        try:
            temp = pyg.image.load("Enigma/gui_mod/enigma_image.jpg")
            self.title_image = pyg.transform.scale(temp, (30, 30))
        except Exception as e:
            self.title_image = None

        # Quit Button (Famous X in RED background, at top right)
        self.quit_button = RectangularButton(
            text="X",
            pos=(self.width * 0.885, self.height * 0.1),
            dim=(30, 30),
            background=RED,
            hover=RED,
        )

        # Title Bar
        self.title_bar = pyg.Surface((self.width, 30))
        pyg.draw.rect(self.title_bar, TITLE_BAR_COLOR, (0, 0, self.width, 30), 0)
        if self.title_image is not None:
            self.title_bar.blit(self.title_image, (0, 0))
        self.title_bar.blit(
            pyg.font.SysFont("Comic Sans MS", 20).render("Enigma Simulator", 1, WHITE),
            (35, 0),
        )

        # Input Output Buttons
        RADIUS = int(self.height * 0.02)
        LEFT_MARGIN = int(self.width * 0.13)
        RIGHT_MARGIN = int(self.width * 0.85)
        TOP_MARGIN = int(self.height * 0.175)
        SEPRATION = int(self.height * 0.09)

        i = 0
        self.in_buttons = list()
        self.out_buttons = list()
        for alpha in self.alphabet:
            self.in_buttons.append(
                CircleButton(
                    text=alpha,
                    pos=(LEFT_MARGIN, i * SEPRATION + TOP_MARGIN),
                    radius=RADIUS,
                    hover=DARK_GREY,
                    high_light=LIGHT_GREY,
                    static=False,
                )
            )
            i += 1
        for alpha in self.alphabet:
            self.out_buttons.append(
                CircleButton(
                    text=alpha,
                    pos=(LEFT_MARGIN, i * SEPRATION + TOP_MARGIN),
                    radius=RADIUS,
                    hover=BACKGROUND_COLOR,
                    high_light=BACKGROUND_COLOR,
                    static=False,
                )
            )
            i += 1

        WIDTH = int((self.width / (self.n_rotors + 3)) * 0.69)
        HEIGHT = int(self.height * 0.7)
        LEFT_MARGIN = LEFT_MARGIN + 2 * RADIUS + 100
        TOP_MARGIN = int(self.height * 0.15)
        SEPRATION = int(self.width * 0.14)

        self.reflect = self.en_obj.reflect
        self.plug = self.en_obj.plug
        self.rotors = list()
        self.UpButtons = list()
        self.DownButtons = list()

        # Plug Board
        self.plug.animate(
            text="Plug Board",
            pos=(LEFT_MARGIN, TOP_MARGIN),
            dim=(WIDTH, HEIGHT),
            bground=BACKGROUND_COLOR,
        )
        self.plug.pos = None
        self.plug.update_img()

        # Rotors
        for i in range(1, self.n_rotors + 1):
            self.rotors.append(self.en_obj.rotors[i - 1])
            self.rotors[-1].animate(
                text="Rotor {}".format(i),
                pos=(LEFT_MARGIN + (i * SEPRATION), TOP_MARGIN),
                dim=(WIDTH, HEIGHT),
                bground=BACKGROUND_COLOR,
            )
            self.UpButtons.append(
                RectangularButton(
                    text="^",
                    pos=(
                        int((LEFT_MARGIN + i * SEPRATION) + 100),
                        int(TOP_MARGIN * 1.8),
                    ),
                    dim=(30, 30),
                    background=BACKGROUND_COLOR,
                    border=BLACK,
                    hover=DARK_GREY,
                )
            )
            self.DownButtons.append(
                RectangularButton(
                    text="^",
                    pos=(
                        int((LEFT_MARGIN + i * SEPRATION) + 100),
                        int(TOP_MARGIN * 2.5),
                    ),
                    dim=(30, 30),
                    background=BACKGROUND_COLOR,
                    border=BLACK,
                    hover=DARK_GREY,
                    rotate=180,
                )
            )

        # Reflection Board
        self.reflect.animate_reflection(
            text="Reflection Board",
            pos=((LEFT_MARGIN + (self.n_rotors + 1) * SEPRATION), TOP_MARGIN),
            dim=(WIDTH, HEIGHT),
            bground=BACKGROUND_COLOR,
        )

        self.start()

    def wait(self, t):
        """"""
        pyg.time.wait(t)

    def get_events(self):
        """"""
        return pyg.event.get()

    def rotate_rotor(self, rotor_no):
        """Rotates rotor with given index"""
        self.rotors[rotor_no].rotate()
        if rotor_no != (self.n_rotors - 1) and self.rotors[rotor_no].pos == 0:
            self.rotate_rotor(rotor_no + 1)

    def update_screen(self):
        """"""
        self.screen.fill(BACKGROUND_COLOR)
        self.screen.blit(self.title_bar, (190, 108))
        self.quit_button.draw(self.screen)

        for button in self.in_buttons:
            button.draw(self.screen)
        for button in self.out_buttons:
            button.draw(self.screen)

        self.plug.draw(self.screen)
        for rotor in self.rotors:
            rotor.draw(self.screen)
        for button in self.UpButtons:
            button.draw(self.screen)
        for button in self.DownButtons:
            button.draw(self.screen)
        self.reflect.draw(self.screen)
        pyg.display.update()

    def start(self):
        """"""
        running = True
        p_char = self.alphabet[0]
        while running:
            self.update_screen()
            if self.quit_button.click():
                running = False
            for i in range(len(self.UpButtons)):
                if self.UpButtons[i].click():
                    self.rotors[i].rotate()
                    self.rotors[i].update_img()
            for i in range(len(self.DownButtons)):
                if self.DownButtons[i].click():
                    self.rotors[i].rotate(by=-1)
                    self.rotors[i].update_img()
            for i in range(len(self.alphabet)):
                if self.in_buttons[i].click():
                    self.out_buttons[ord(p_char) - ord(self.alphabet[0])].__update__()
                    o_char = self.alphabet[i]
                    p_char, char_arr = self.en_obj.process_char(self.alphabet[i])
                    mid = len(char_arr) // 2
                    self.plug.update_img(o_char, char_arr[-1])
                    for i in range(self.n_rotors):
                        self.rotors[i].update_img(
                            char_arr[2 * i + 1],
                            char_arr[len(self.alphabet) - 2 * (i + 2)],
                        )
                    self.reflect.update_img(char_arr[mid - 1])
                    self.out_buttons[ord(p_char) - ord(self.alphabet[0])].__update__(
                        GOLD
                    )

            for event in self.get_events():
                if event.type == QUIT_EVENT:
                    running = False
            self.wait(1)
