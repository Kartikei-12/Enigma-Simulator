""""""

# Python module(s)
import pygame as pyg
import random
from pprint import pprint

# Environment Variable(s)
# Other
from .env import ALPHABET, TRAIL_LIMIT

# Colors
from .env import BLACK, BACKGROUND_COLOR


class Rotor:
    """"""

    def __init__(self, k_dict=None, alphabet=ALPHABET, pos=0):
        self.alpha_len = len(alphabet)
        self.alphabet = alphabet
        self.pos = pos
        if k_dict == None:
            self.k_dict = self.generate_rotor_board()
        else:
            self.k_dict = k_dict

    def move(self, char, by=1):
        """Moves chracter forward"""
        pos = self.pos * by
        return chr(((ord(char) - ord("A") + pos) % self.alpha_len) + ord("A"))

    def __getitem__(self, char):
        """Fetches rotor value"""
        return self.k_dict[char]

    def rotate(self):
        """Rotates rotor with given index"""
        self.pos = (self.pos + 1) % self.alpha_len

    def generate_rotor_board(self):
        """Generates confirigation for reflection/rotor/plugboard board"""
        rotor = dict()
        self.pos = random.randint(0, self.alpha_len)
        ALPHABET_copy = self.alphabet.copy()
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

    def animate(self, x, y, width, height, color=BLACK, background=BACKGROUND_COLOR):
        """"""
        self.top = y
        self.left = x
        self.width = width
        self.height = height
        self.color = color
        self.background = background
        self.rotor_img = pyg.Surface((width, height))
        self.update_img()

    def update_img(self):
        """"""
        pyg.draw.rect(
            self.rotor_img, self.background, (0, 0, self.width, self.height), 0
        )
        pyg.draw.rect(
            self.rotor_img, self.color, (0, 0, self.width - 2, self.height - 2), 2
        )

    def draw(self, surface):
        """"""
        surface.blit(self.rotor_img, (self.left, self.top))
