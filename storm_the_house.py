# This script is meant to auto-play one of my favorite childhood games "Storm The House"
# which can be found in https://www.crazygames.com/game/storm-the-house or any other website.

# In order to create a virtual environment for Python scripts,
# python3 -m venv .venv
# source .venv/bin/activate -> activates the virtual environment
# (Recommended to make a requirements.txt file for projects, run "pip install -r requirements.txt")
# When done, deactivate the environment by "deactivate"

from pyautogui import *
import pyautogui
import time
import keyboard
import random

# RGB Color of their head: 204, 204, 204
# RGB Color of their body: 0, 0, 0

pyautogui.FAILSAFE = True # Move mouse to top-left to stop script

pyautogui.moveTo(200, 200, duration=1) # Moves mouse to coordinate
pyautogui.moveRel(0, 100, duration=1) # Moves mouse relatively
pyautogui.displayMousePosition() # Can be used to find color and position
print(pyautogui.size()) # prints 3840, 1080 for dual monitor

gamescreenWidth = 1920
gamescreenHeight = 1080
while keyboard.is_pressed('q') == False:
    pixelColor = pyautogui.pixel(gamescreenWidth, gamescreenHeight) # How can I make this an area???
    print(pixelColor)
    if pixelColor == (204, 204, 204) or pixelColor == (0, 0, 0):
        pyautogui.click()
        time.sleep(random.uniform(0.1, 0.2))
    time.sleep(0.01)