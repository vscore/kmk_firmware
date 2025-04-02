from kb import KMKKeyboard

from kmk.extensions.rgb import RGB
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide, SplitType

keyboard = KMKKeyboard()
keyboard.debug_enabled = True
# Adding extensions
# rgb = RGB(
#     pixel_pin=keyboard.rgb_pixel_pin,
#     num_pixels=27,
#     val_limit=100,
#     hue_default=190,
#     sat_default=100,
#     val_default=5,
# )

# TODO Comment one of these on each side
split_side = SplitSide.LEFT
#split_side = SplitSide.RIGHT
#split = Split(split_type=SplitType.BLE, split_side=split_side)

# Uncomment this to use WiFi split instead of BLE split
split = Split(
    split_type=SplitType.WIFI,
    wifi_ssid="VivKB",
    wifi_password="vivek123",
    wifi_port=12345,
    split_side=SplitSide.LEFT,  # Set this half as the left side
)

layers = Layers()

keyboard.modules = [layers, split]
#keyboard.extensions = [rgb]
#
# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

LOWER = KC.MO(1)
RAISE = KC.MO(2)
ADJUST = KC.LT(3, KC.SPC)

RGB_TOG = KC.RGB_TOG
RGB_HUI = KC.RGB_HUI
RGB_HUD = KC.RGB_HUI
RGB_SAI = KC.RGB_SAI
RGB_SAD = KC.RGB_SAD
RGB_VAI = KC.RGB_VAI
RGB_VAD = KC.RGB_VAD


# fmt:off
keyboard.keymap = [
       [KC.KP_ASTERISK,KC.N7,KC.N4,KC.N1,
     KC.HASH,KC.N9,KC.N6,KC.N3,
     KC.N0,KC.N8,KC.N5,KC.N2,
     KC.D,KC.C,KC.B,KC.A,]
]
# fmt:on

if __name__ == '__main__':
    keyboard.go()
