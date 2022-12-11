import pyautogui
import time

delay = 3
screenWidth, screenHeight = pyautogui.size()
#pyautogui.moveTo(0, 0, delay)


click = pyautogui.leftClick
double_click = pyautogui.doubleClick

####some assumptions###
#1. pop os linux 
#2. using mozilla firefox
#3. facebook mobilized
#----> see vobjects screenshots to see exactly what it is looking for
click(pyautogui.locateCenterOnScreen("./vobjects/firefox.png",confidence=.75))
double_click(pyautogui.locateCenterOnScreen("./vobjects/full_screen_browser.png",confidence=.75))


print(screenWidth, screenHeight)