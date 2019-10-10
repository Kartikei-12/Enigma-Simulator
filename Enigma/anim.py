""""""

# Python Module(s)
import pygame

# Project Module(s)
from .enigma import Enigma
from .rec_button import RectangularButton
from .circle_button import CircleButton

# Environment Variable(s)
# Other
from .env import STANDARD_WAIT, ANIM_ALPHABET

# Color(s)
from .env import BACKGROUND_COLOR, RED, WHITE, BLACK, DARK_GREY, LIGHT_GREY


QUIT_EVENT = pygame.QUIT
MOUSEBUTTONDOWN = pygame.MOUSEBUTTONDOWN


class Animation:
    """"""

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Enigma Simulator")
        self.n_rotors = 2
        self.en_obj = Enigma(alphabet=ANIM_ALPHABET, n_rotors=self.n_rotors)
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.width, self.height = self.screen.get_size()
        self.quit_button = RectangularButton(
            text="X",
            left=self.width * 0.885,
            top=self.height * 0.1,
            width=30,
            height=30,
            background=RED,
            border=RED,
            hover=RED,
        )

        RADIUS = int(self.height * 0.02)
        LEFT_MARGIN = int(self.width * 0.13)
        TOP_MARGIN = int(self.height * 0.12)
        SEPRATION = int(self.height * 0.1)
        self.in_buttons = list()
        self.out_buttons = list()
        i = 0
        for alpha in ANIM_ALPHABET:
            self.in_buttons.append(
                CircleButton(
                    text=alpha,
                    left=LEFT_MARGIN,
                    top=i * SEPRATION + TOP_MARGIN,
                    radius=RADIUS,
                    background=BACKGROUND_COLOR,
                    border=BLACK,
                    hover=DARK_GREY,
                    high_light=LIGHT_GREY,
                )
            )
            i += 1
        for alpha in ANIM_ALPHABET:
            self.out_buttons.append(
                CircleButton(
                    text=alpha,
                    left=LEFT_MARGIN,
                    top=i * SEPRATION + TOP_MARGIN,
                    radius=RADIUS,
                    background=BACKGROUND_COLOR,
                    border=BLACK,
                    hover=BACKGROUND_COLOR,
                    high_light=BACKGROUND_COLOR,
                )
            )
            i += 1

        WIDTH = int(self.width / (self.n_rotors + 3 + 1))
        HEIGHT = int(self.height * 0.75)
        LEFT_MARGIN = LEFT_MARGIN + 2 * RADIUS + 60
        TOP_MARGIN = int(self.height * 0.12)
        SEPRATION = int(self.width * 0.2)
        self.rotors = list()
        for i in range(self.n_rotors):
            self.rotors.append(self.en_obj.rotors[i])
            self.rotors[-1].animate(
                x=LEFT_MARGIN + i * SEPRATION,
                y=TOP_MARGIN,
                width=WIDTH,
                height=HEIGHT,
                background=BACKGROUND_COLOR,
            )
        # self.rotor_1 = self.en_obj.rotors[0]
        # self.rotor_1.animate(x=500, y=200, width=100, height=200)

        self.start()

    def wait(self, t):
        """"""
        pygame.time.wait(t)

    def get_events(self):
        """"""
        return pygame.event.get()

    def update_screen(self):
        """"""
        self.screen.fill(BACKGROUND_COLOR)
        self.quit_button.draw(self.screen)

        for button in self.in_buttons:
            button.draw(self.screen)
        for button in self.out_buttons:
            button.draw(self.screen)

        # self.rotor_1.draw(self.screen)
        for rotor in self.rotors:
            rotor.draw(self.screen)

        pygame.display.update()

    def start(self):
        """"""
        running = True
        while running:
            self.update_screen()
            if self.quit_button.click():
                running = False
            for event in self.get_events():
                if event.type == QUIT_EVENT:
                    running = False
            self.wait(5)
