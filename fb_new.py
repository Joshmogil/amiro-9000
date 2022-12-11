import pyautogui
import time
import dotenv , os

dotenv.load_dotenv(".env")

mob = os.getenv("FB_MOBILE")
pas = os.getenv("FB_PASSWORD")

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
#double_click(pyautogui.locateCenterOnScreen("./vobjects/full_screen_browser.png",confidence=.75))
time.sleep(.30)
click(pyautogui.locateCenterOnScreen("./vobjects/facebook_shortcut.png",confidence=.75))
time.sleep(3)

click(pyautogui.locateCenterOnScreen("./vobjects/fblogin/mobile.png",confidence=.75))
time.sleep(.30)
pyautogui.typewrite(mob)

click(pyautogui.locateCenterOnScreen("./vobjects/fblogin/pw_box.png",confidence=.75))
time.sleep(.30)
pyautogui.typewrite(pas)


print(screenWidth, screenHeight)