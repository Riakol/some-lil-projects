class Color:
    def __init__(self, hexcode) -> None:
        self._hexcode = hexcode

    @property
    def hexcode(self):
        return self._hexcode
    
    @hexcode.setter
    def hexcode(self, new_hexcode):
        self._hexcode = new_hexcode
        self.r = int(self._hexcode[0:2], base=16)
        self.g = int(self._hexcode[2:4], base=16)
        self.b = int(self._hexcode[4:], base=16)
