# Import Library's
import PIL.ImageGrab
from pynput.mouse import Controller
import time

while True:
    mouse = Controller()
    # Get the mouse position
    current_mouse_position = mouse.position
    # Get the rbg-value from mouse position
    rgb = PIL.ImageGrab.grab().load()[current_mouse_position]
    # print the position + rgb-value
    print("On position: " + str(current_mouse_position) + " is the rgb-value: " + str(rgb))
    # Wait 1 sec
    time.sleep(1)