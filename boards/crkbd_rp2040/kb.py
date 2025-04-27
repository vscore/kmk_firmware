import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
#Importing the pinout from the helios board.
#you can change this to any Pro Micro clone pinout you want from Quickpin.
from kmk.quickpin.pro_micro.helios import pinout as pins
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        super().__init__()
        self.col_pins = (
           board.GP29,
           board.GP28,
           board.GP27,
           board.GP26,
           board.SCK,
           board.SDI,
        )
        self.row_pins = (
            board.GP4,
            board.GP5,
            board.GP6,
            board.GP7,
        )

        self.diode_orientation = DiodeOrientation.COLUMNS
        self.data_pin = board.RX
        #A bit of a hack to get the second data pin working
        #Since GP8 is not used for anything nor it is connected to anything.
        self.data_pin2 = board.GP8
        self.rgb_pixel_pin = pins[0]
        self.i2c = board.I2C

        # fmt: off
        self.coord_mapping = [
             0,  1,  2,  3,  4,  5,  29, 28, 27, 26, 25, 24,
             6,  7,  8,  9, 10, 11,  35, 34, 33, 32, 31, 30,
            12, 13, 14, 15, 16, 17,  41, 40, 39, 38, 37, 36,
                        21, 22, 23,  47, 46, 45,
        ]
        # fmt:on
