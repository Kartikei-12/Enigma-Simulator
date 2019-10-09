from Enigma import Enigma


def main():
    # engima_object = Enigma(".enigma/enigma_config.json")
    engima_object = Enigma()
    en = engima_object.process("HELLO WORLD")
    print(en)
    engima_object.reset_config_dict()
    print(engima_object.process(en))
    # a = engima_object.move('A', 15)
    # b = engima_object.move(a, -15)
    # print(b)


if __name__ == "__main__":
    main()
