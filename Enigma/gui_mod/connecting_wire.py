"""connecting_wire.py file"""


class ConnectingWire:
    """Class to describe connecting wires in reflection board

    Args:
        wires (list, tuple): Iterable sequence of Line objects"""

    def __init__(self, wires):
        self.wires = wires
        self.__update__()

    def __update__(self, active=None):
        """Updates wires

        Args:
            active(str): Which chracter is active"""
        for wire in self.wires:
            wire.__update__(active)

    def draw(self, surface):
        """Draw lines on supplied surface

        Args:
            surface(pygame.Surface): Surface to draw lines on"""
        for wire in self.wires:
            wire.draw(surface)
