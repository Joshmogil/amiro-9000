import pyautogui

delay = 3
screenWidth, screenHeight = pyautogui.size()
#pyautogui.moveTo(0, 0, delay)
firefox = pyautogui.locateCenterOnScreen("./vobjects/firefox.png",confidence=.75)
pyautogui.leftClick(firefox)
print(screenWidth, screenHeight)