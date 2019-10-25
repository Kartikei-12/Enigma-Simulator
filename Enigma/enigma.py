"""enigma.py file

Contains main Enigma class for the project

Author: Kartikei Mittal"""

# Python module(s)
import os
import json
from pprint import pprint

# Project Module(s)
from .rotor import Rotor

# Environment Variable(s)
from .env import NUMBER_OF_ROTORS, ALPHABET, DEFAULT_FILE_NAME


class Enigma:
    """Enigma class for Enigma simulator

    Args:
        configration_file(str): Name of confirigation file for enigma machine,
            pass 'None' or nothing if to generate new confirigation file
        alphabet(list, tuple): Iterable object containning set of alphabet for Enigma to work on
        save_config(bool): Wheather to save confirigation in case a new one is generated
        n_rotors(int): Number of rotors in the Enigma Machine"""

    def __init__(
        self,
        configration_file=None,
        alphabet=ALPHABET,
        save_config=False,
        n_rotors=NUMBER_OF_ROTORS,
    ):
        self.alpha_len = len(alphabet)
        self.alphabet = alphabet
        self.n_rotors = n_rotors
        self.rotors = list()
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

    def get_congig_file_name(self):
        """Returns config file name

        Returns:
            str : Name of confirigation file"""
        return self.config_file_name

    def set_config_file_name(self, name):
        """Sets new config file name

        Args:
            name(str): Name of confirigation file"""
        self.config_file_name = name

    def load_config(self):
        """Loads confirigation file

        Returns:
            dict : New confirigation dictionary"""
        with open(self.config_file_name, "r") as f:
            config_dict = json.loads(f.read())
        self.rotors = list()
        self.n_rotors = config_dict["n_rotors"]
        self.alphabet = config_dict["alphabet"]
        self.plug = config_dict["plug_board"]
        self.reflect = config_dict["reflection"]
        for i in range(self.n_rotors):
            self.rotors.append(
                Rotor(
                    k_dict=config_dict["rotors"][i],
                    alphabet=self.alphabet,
                    pos=config_dict["positions"][i],
                )
            )
        return config_dict

    def save_config(self):
        """Saves confirigation file"""
        if not os.path.isdir(".enigma"):
            os.mkdir(".enigma")
        with open(self.config_file_name, "w") as f:
            f.write(json.dumps(self.config_dict))

    def update_config_dict(self):
        """Updates confirigation dictionary"""
        for i in range(self.n_rotors):
            self.config_dict["positions"][i] = self.rotors[i].pos

    def reset_from_config_dict(self):
        """Updates confirigation dictionary"""
        for i in range(self.n_rotors):
            self.rotors[i].pos = self.config_dict["positions"][i]

    def get_plug_value(self, char):
        """Fetches plug board value"""
        return self.plug[char]

    def get_reflection_value(self, char):
        """Fetches reflection board value"""
        return self.reflect[char]

    def rotate_rotor(self, rotor_no):
        """Rotates rotor with given index"""
        self.rotors[rotor_no].rotate()
        if rotor_no != (self.n_rotors - 1) and self.rotors[rotor_no].pos == 0:
            self.rotate_rotor(rotor_no + 1)

    def process_char(self, char):
        """"""
        out_arr = list()
        char = self.get_plug_value(char)
        out_arr.append(char)
        for i in range(self.n_rotors):
            char = self.rotors[i].move(char)
            out_arr.append(char)
            char = self.rotors[i][char]
            out_arr.append(char)
        char = self.get_reflection_value(char)
        out_arr.append(char)
        for i in range(self.n_rotors - 1, -1, -1):
            char = self.rotors[i][char]
            out_arr.append(char)
            char = self.rotors[i].move(char, by=-1)
            out_arr.append(char)

        char = self.get_plug_value(char)
        self.rotate_rotor(0)
        return (char, out_arr)

    def process(self, org_string):
        """Main processing method"""
        processed_str = ""
        for char in org_string:
            if char in self.alphabet:
                processed_str += self.process_char(char)[0]
            else:
                processed_str += char
        return processed_str

    def generate_confirigation_dict(self):
        """Generates configrigation dictionary"""
        self.rotors = list()
        self.reflect = Rotor(alphabet=self.alphabet)
        self.plug = Rotor(alphabet=self.alphabet)
        config_dict = {
            "alphabet": self.alphabet,
            "n_rotors": self.n_rotors,
            "reflection": self.reflect.k_dict,
            "plug_board": self.plug.k_dict,
            "rotors": list(),
            "positions": list(),
        }
        for i in range(self.n_rotors):
            r = Rotor(alphabet=self.alphabet)
            self.rotors.append(r)
            config_dict["positions"].append(r.pos)
            config_dict["rotors"].append(r.k_dict)
        return config_dict
