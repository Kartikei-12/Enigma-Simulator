"""
main.py file for Enigma-Simulator

Author: Kartikei Mittal
"""

# Python module(s)
import sys

# Project module(s)
from Enigma import Enigma, Animation

def cmd():
    in_data = open(input("Enter file to de(code): "), 'r').read()
    config_file = input("Enter configiration file(0 to generate a new one): ")
    if config_file == "0":
        engima_object = Enigma(save_config=True)
        print("All newly generated confirigation file are stored in .enigma folder")
    else:
        engima_object = Enigma(config_file)
    out_data = engima_object.process(in_data)
    open("out.txt", 'w').write(out_data)
    out_data = out_data if len(out_data) < 100 else out_data[:100]+"..."
    print("Processed data:", out_data)
    print("Saving data in out.txt")
    # engima_object = Enigma(".enigma/enigma_config.json")
    # en = engima_object.process("HELLO WORLD")
    # print(en)
    # engima_object.reset_from_config_dict()
    # print(engima_object.process(en))


def gui():
    an = Animation()


if __name__ == "__main__":
    if sys.argv[0] == "--gui":
        gui()
    else:
        cmd()
