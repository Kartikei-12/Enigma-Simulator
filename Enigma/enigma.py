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

    def __init__(self, configration_file=None):
        self.alpha_len = len(ALPHABET)
        if configration_file == None:
            self.config_file_name = DEFAULT_FILE_NAME
            self.config_dict = self.generate_confirigation_dict()
            self.save_config()
            print("Generated and saved new confirigation")
        else:
            print("Loading confirigation file")
            self.config_file_name = configration_file
            self.config_dict = self.load_config()

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

    def generate_reflection_board(self):
        """Generates confirigation for reflection board"""
        reflection_rotor = dict()
        ALPHABET_copy = ALPHABET.copy()
        for character in ALPHABET:
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

    def generate_single_rotor(self):
        """Generates confirigation for single rotor or plug board"""
        rotor = dict()
        ALPHABET_copy = ALPHABET.copy()
        for character in ALPHABET:
            count = 0
            rotor[character] = random.choice(ALPHABET_copy)
            while character == rotor[character]:
                rotor[character] = random.choice(ALPHABET_copy)
                count += 1
                if count == TRAIL_LIMIT:
                    raise Exception("Error in random sampaling")
            ALPHABET_copy.remove(rotor[character])
        return rotor

    def generate_confirigation_dict(self):
        """Generates configrigation dictionary"""
        config_dict = {
            "number_of_rotors": NUMBER_OF_ROTORS,
            "reflection_rotor": self.generate_reflection_board(),
            "plug_board": self.generate_single_rotor(),
            "rotors": list(),
            "initial_positions": list(),
        }
        for i in range(NUMBER_OF_ROTORS):
            config_dict["initial_positions"] = random.randint(0, len(ALPHABET))
            config_dict["rotors"].append(self.generate_single_rotor())
        return config_dict
