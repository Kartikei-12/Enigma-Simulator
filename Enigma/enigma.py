"""enigma.py file

Contains main Enigma class for the project

Author: Kartikei Mittal"""

import os
import json
import random
from pprint import pprint

from .env import NUMBER_OF_ROTORS, ALPHABET, DEFAULT_FILE_NAME, TRAIL_LIMIT


class Enigma:
    """Enigma class for Enigma simulator

    Args:
        configration_file(str): Name of confirigation file for enigma machine,
        pass 'None' or nothing if to generate new confirigation file"""

    def __init__(self, configration_file=None, alphabet=ALPHABET, save_config=False):
        self.alpha_len = len(alphabet)
        self.alphabet = alphabet
        if configration_file == None:
            print("Generating new confirigation")
            self.config_file_name = DEFAULT_FILE_NAME
            self.config_dict = self.generate_confirigation_dict()
            if save_config:
                self.save_config()
                print("Saved new confirigation")
        else:
            print("Loading confirigation file")
            self.config_file_name = configration_file
            self.config_dict = self.load_config()
        self.n_rotors = self.config_dict["n_rotors"]
        self.rotor_pos = list()
        for i in range(self.n_rotors):
            self.rotor_pos.append(self.config_dict["positions"][i])

    def get_congig_file_name(self):
        """Returns config file name"""
        return self.config_file_name

    def set_config_file_name(self, name):
        """Sets new config file name"""
        self.config_file_name = name

    def load_config(self):
        """Loads confirigation file"""
        with open(self.config_file_name, "r") as f:
            return json.loads(f.read())

    def save_config(self):
        """Saves confirigation file"""
        if not os.path.isdir(".enigma"):
            os.mkdir(".enigma")
        with open(self.config_file_name, "w") as f:
            f.write(json.dumps(self.config_dict))

    def get_rotor_positions(self):
        """Returns current of the rotors"""
        return self.rotor_pos

    def update_config_dict(self):
        """Updates confirigation dictionary"""
        for i in range(self.n_rotors):
            self.config_dict["positions"][i] = self.rotor_pos[i]

    def reset_config_dict(self):
        """Updates confirigation dictionary"""
        for i in range(self.n_rotors):
            self.rotor_pos[i] = self.config_dict["positions"][i]

    def get_plug_value(self, char):
        """Fetches plug board value"""
        return self.config_dict["plug_board"][char]

    def get_reflection_value(self, char):
        """Fetches reflection board value"""
        return self.config_dict["reflection"][char]

    def rotate_rotor(self, rotor_no):
        """Rotates rotor with given index"""
        self.rotor_pos[rotor_no] = (self.rotor_pos[rotor_no] + 1) % self.alpha_len
        if rotor_no != (self.n_rotors - 1) and self.rotor_pos[rotor_no] == 0:
            self.rotate_rotor(rotor_no + 1)

    def get_rotor_value(self, rotor_no, char):
        """Fetches rotor value"""
        rotor_char = char
        rotor = self.config_dict["rotors"][rotor_no]
        value = rotor[rotor_char]
        return value

    def move(self, char, pos):
        """Moves chracter forward"""
        return chr(((ord(char) - ord("A") + pos) % self.alpha_len) + ord("A"))

    def process_char(self, char):
        char = self.get_plug_value(char)

        for i in range(self.n_rotors):
            char = self.move(char, self.rotor_pos[i])
            char = self.get_rotor_value(i, char)
        char = self.get_reflection_value(char)
        for i in range(self.n_rotors - 1, -1, -1):
            char = self.get_rotor_value(i, char)
            char = self.move(char, -1 * self.rotor_pos[i])

        self.rotate_rotor(0)
        char = self.get_plug_value(char)
        return char

    def process(self, org_string):
        """Main processing method"""
        processed_str = ""
        for char in org_string:
            if char in self.alphabet:
                processed_str += self.process_char(char)
            else:
                processed_str += char
        return processed_str

    def generate_reflection_board(self):
        """Generates confirigation for reflection board"""
        reflection_rotor = dict()
        ALPHABET_copy = self.alphabet.copy()
        for character in self.alphabet:
            if character not in ALPHABET_copy:
                continue
            count = 0
            reflection_rotor[character] = random.choice(ALPHABET_copy)
            reflection_rotor[reflection_rotor[character]] = character
            while character == reflection_rotor[character]:
                reflection_rotor[character] = random.choice(ALPHABET_copy)
                reflection_rotor[reflection_rotor[character]] = character
                count += 1
                if count == TRAIL_LIMIT:
                    raise Exception("Error in random sampaling")
            ALPHABET_copy.remove(character)
            ALPHABET_copy.remove(reflection_rotor[character])
        return reflection_rotor

    def generate_confirigation_dict(self):
        """Generates configrigation dictionary"""
        config_dict = {
            "n_rotors": NUMBER_OF_ROTORS,
            "reflection": self.generate_reflection_board(),
            "plug_board": self.generate_reflection_board(),
            "rotors": list(),
            "positions": list(),
        }
        for i in range(NUMBER_OF_ROTORS):
            config_dict["positions"].append(random.randint(0, self.alpha_len))
            config_dict["rotors"].append(self.generate_reflection_board())
        return config_dict
