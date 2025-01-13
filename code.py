import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# Initialize the keyboard
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

# Function to open Opera GX and navigate to Google
def open_opera_gx():
    # Press Windows key
    keyboard.press(Keycode.WINDOWS)
    keyboard.release(Keycode.WINDOWS)
    time.sleep(0.5)
    
    # Type "Opera GX" and press Enter
    keyboard_layout.write("Opera GX")
    keyboard.press(Keycode.ENTER)
    keyboard.release(Keycode.ENTER)
    time.sleep(3)  # Wait for Opera GX to open
    
    # Type the URL and press Enter
    keyboard_layout.write("https://www.google.com")
    keyboard.press(Keycode.ENTER)
    keyboard.release(Keycode.ENTER)

# Wait for a few seconds before executing the function
time.sleep(5)
open_opera_gx()