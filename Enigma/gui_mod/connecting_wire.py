"""connecting_wire.py file"""


class ConnectingWire:
    """"""

    def __init__(self, wires):
        self.wires = wires
        self.__update__()

    def __update__(self, active=None):
        """"""
        for wire in self.wires:
            wire.__update__(active)

    def draw(self, surface):
        """"""
        for wire in self.wires:
            wire.draw(surface)
