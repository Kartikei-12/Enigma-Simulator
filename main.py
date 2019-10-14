"""main.py file for Enigma-Simulator

Author: Kartikei Mittal"""

# Python module(s)
import sys

# Project module(s)
from Enigma import Enigma, Animation


def __help():
    """Help Utility"""
    print("Once again Welcome to Enigma Simulator,")
    print("Parameters for main.py")
    print("\t-h or --help: to view this help")
    print("\t-g or --gui: to launch Graphical Inverface Animation")
    print("\t-c or --cli: to launch Command Line Interface")


def cmd():
    """Command Line Interface"""
    in_data = open(input("Enter file to de(code): "), "r").read()
    config_file = input("Enter configiration file(0 to generate a new one): ")
    if config_file == "0":
        engima_object = Enigma(save_config=True)
        print("All newly generated confirigation file are stored in .enigma folder")
    else:
        engima_object = Enigma(config_file)
    out_data = engima_object.process(in_data)
    open("out.txt", "w").write(out_data)
    out_data = out_data if len(out_data) < 100 else out_data[:100] + "..."
    print("Processed data:", out_data)
    print("Saving data in out.txt")
    # engima_object = Enigma()
    # en = engima_object.process("HELLO WORLD")
    # print(en)
    # engima_object.reset_from_config_dict()
    # print(engima_object.process(en))


def gui():
    """Graphical User Interface"""
    an = Animation()


if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv:
        __help()
    elif "--gui" in sys.argv or "-g" in sys.argv:
        gui()
    elif "--cli" in sys.argv or "-c" in sys.argv:
        cmd()
    else:
        print("Showing default help due to absence of proper parameters")
        __help()
