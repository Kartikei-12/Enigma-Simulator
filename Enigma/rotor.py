""""""

# Python module(s)
import pygame as pyg
import random
from pprint import pprint

# Project module(s)
from .gui_mod.line import Line
from .gui_mod.circle_button import CircleButton
from .gui_mod.connecting_wire import ConnectingWire as ConnW

# Environment Variable(s)
# Other
from .env import ALPHABET, TRAIL_LIMIT

# Colors
from .env import BLACK, BACKGROUND_COLOR, GOLD, RED, GREEN


class Rotor:
    """"""

    def __init__(self, k_dict=None, alphabet=ALPHABET, pos=0, reflection=True):
        self.alpha_len = len(alphabet)
        self.alphabet = alphabet
        self.pos = pos
        if k_dict == None:
            self.k_dict = (
                self.generate_rotor_board()
                if reflection
                else self.generate_rotor_board_non_reflection()
            )
        else:
            self.k_dict = k_dict

    def move(self, char, by=1):
        """Moves chracter forward"""
        pos = self.pos * by
        return chr(((ord(char) - ord("A") + pos) % self.alpha_len) + ord("A"))

    def __getitem__(self, char):
        """Fetches rotor value"""
        return self.k_dict[char]

    def rotate(self, by=1):
        """Rotates rotor with given index"""
        self.pos = (self.pos + by) % self.alpha_len

    def generate_rotor_board(self):
        """Generates confirigation for reflection/plugboard board"""
        rotor = dict()
        ALPHABET_copy = self.alphabet.copy()
        if (self.alpha_len % 2) != 0:
            char = self.alphabet[0]
            rotor[char] = char
            ALPHABET_copy.remove(char)
        for character in self.alphabet:
            if character not in ALPHABET_copy:
                continue
            count = 0
            rotor[character] = random.choice(ALPHABET_copy)
            rotor[rotor[character]] = character
            while character == rotor[character]:
                rotor[character] = random.choice(ALPHABET_copy)
                rotor[rotor[character]] = character
                count += 1
                if count == TRAIL_LIMIT:
                    raise Exception("Error in random sampaling")
            ALPHABET_copy.remove(character)
            ALPHABET_copy.remove(rotor[character])
        return rotor

    def generate_rotor_board_non_reflection(self):
        """Generates confirigation for rotor board"""
        rotor = dict()
        self.pos = random.randint(0, self.alpha_len - 1)
        ALPHABET_copy = self.alphabet.copy()
        for character in self.alphabet:
            count = 0
            rotor[character] = random.choice(ALPHABET_copy)
            while character == rotor[character]:
                rotor[character] = random.choice(ALPHABET_copy)
                count += 1
                if count == TRAIL_LIMIT:
                    raise Exception("Error in random sampaling")
            ALPHABET_copy.remove(rotor[character])
        return rotor

    # ---------------------------------------------------------------------------------
    # ----------------------- COMMENT REST OF FOLLOWING CODE, -------------------------
    # ------------------------------- IF NOT USING GUI --------------------------------
    # ---------------------------------------------------------------------------------
    def animate(self, text, pos, dim, color=BLACK, bground=BACKGROUND_COLOR):
        """"""
        self.top = pos[1]
        self.left = pos[0]
        self.width = dim[0]
        self.height = dim[1]
        self.color = color
        self.bground = bground
        self.rotor_img = pyg.Surface(dim)
        self.text = text
        self.label = pyg.font.SysFont("Comic Sans MS", 25).render(text, 1, BLACK)
        self.symbols = list()

        RADIUS = int(self.height * 0.03)
        LEFT_MARGIN = int(self.width * 0.05)
        RIGHT_MARGIN = int(self.width * 0.72)
        TOP_MARGIN = int(self.height * 0.1)
        SEPRATION = int(self.height * 0.25)
        for i in range(self.alpha_len):
            self.symbols.append(
                CircleButton(
                    text=self.alphabet[i],
                    left=LEFT_MARGIN,
                    top=TOP_MARGIN + i * SEPRATION,
                    radius=RADIUS,
                )
            )
            self.symbols.append(
                CircleButton(
                    text=self.k_dict[self.alphabet[i]],
                    left=RIGHT_MARGIN,
                    top=TOP_MARGIN + i * SEPRATION,
                    radius=RADIUS,
                )
            )
            self.symbols.append(
                Line(
                    pos=(
                        1 + LEFT_MARGIN + 2 * RADIUS,
                        TOP_MARGIN + RADIUS + i * SEPRATION,
                    ),
                    length=RIGHT_MARGIN - LEFT_MARGIN - 2 * RADIUS - 2,
                )
            )
        self.update_img()

    def animate_reflection(self, text, pos, dim, color=BLACK, bground=BACKGROUND_COLOR):
        """"""
        self.pos = None
        self.top = pos[1]
        self.left = pos[0]
        self.width = dim[0]
        self.height = dim[1]
        self.color = color
        self.bground = bground
        self.rotor_img = pyg.Surface(dim)
        self.text = text
        self.label = pyg.font.SysFont("Comic Sans MS", 25).render(text, 1, BLACK)
        self.symbols = list()

        RADIUS = int(self.height * 0.03)
        LEFT_MARGIN = int(self.width * 0.05)
        TOP_MARGIN = int(self.height * 0.05)
        SEPRATION = int(self.height * 0.12)
        LENGTH = int((self.width - LEFT_MARGIN - 2 * RADIUS) * 0.2)
        L_LEFT = LEFT_MARGIN + 2 * RADIUS
        L_TOP = TOP_MARGIN + RADIUS

        for i in range(self.alpha_len):
            # INPUT
            self.symbols.append(
                CircleButton(
                    text=self.alphabet[i],
                    left=LEFT_MARGIN,
                    top=TOP_MARGIN + i * SEPRATION,
                    radius=RADIUS,
                )
            )
            # OUTPUT
            self.symbols.append(
                CircleButton(
                    text=self.k_dict[self.alphabet[i]],
                    left=LEFT_MARGIN,
                    top=TOP_MARGIN + (i + self.alpha_len) * SEPRATION,
                    radius=RADIUS,
                )
            )
            # --------------------------------------------------------------------
            # --------------------------------------------------------------------
            self.symbols.append(
                ConnW(
                    [
                        Line(
                            pos=(L_LEFT, L_TOP + i * SEPRATION),
                            length=LENGTH * (self.alpha_len - i),
                        ),
                        Line(
                            pos=(
                                (L_LEFT + LENGTH * (self.alpha_len - i)),
                                L_TOP + i * SEPRATION,
                            ),
                            length=int(SEPRATION * (2 * self.alpha_len - 2 * i - 1))
                            + 1,
                            rotate=90,
                        ),
                        Line(
                            pos=(
                                L_LEFT,
                                L_TOP + (2 * self.alpha_len - i - 1) * SEPRATION,
                            ),
                            length=LENGTH * (self.alpha_len - i) + 4,
                        ),
                    ]
                )
            )
            # --------------------------------------------------------------------
            # --------------------------------------------------------------------
            # --------------------------------------------------------------------
            # --------------------------------------------------------------------
        self.update_img()

    def update_img(self, active=None, active2=None):
        """"""
        pyg.draw.rect(self.rotor_img, self.bground, (0, 0, self.width, self.height), 0)
        pyg.draw.rect(
            self.rotor_img, self.color, (0, 0, self.width - 2, self.height - 2), 2
        )
        self.rotor_img.blit(
            self.label,
            (
                int((self.width - self.label.get_size()[0]) / 2),
                int((self.height - self.label.get_size()[1]) / 2),
            ),
        )

        if self.pos is not None:
            self.pos_label = pyg.font.SysFont("Comic Sans MS", 25).render(
                self.alphabet[self.pos], 1, BLACK
            )
            self.rotor_img.blit(
                self.pos_label,
                (
                    int((self.width - self.label.get_size()[0]) * 0.85),
                    int((self.height - self.label.get_size()[1]) * 0.25),
                ),
            )

        for symbol in self.symbols:
            symbol.__update__()
        if active is not None:
            index1 = 3 * (ord(active) - ord(self.alphabet[0]) + 1) - 1
            color = GREEN if self.text != "Reflection Board" else GOLD
            self.symbols[index1].__update__(color)
            if active2 is not None:
                index2 = 3 * (ord(active2) - ord(self.alphabet[0]) + 1) - 1
                self.symbols[index2].__update__(RED)
        for symbol in self.symbols:
            symbol.draw(self.rotor_img)

    def draw(self, surface):
        """"""
        surface.blit(self.rotor_img, (self.left, self.top))
