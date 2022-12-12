import pyautogui
import time
import dotenv , os
from pyscreeze import Point

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

#Confidence intervals could use some adjustment.
click(pyautogui.locateCenterOnScreen("./vobjects/firefox.png",confidence=.75))
#double_click(pyautogui.locateCenterOnScreen("./vobjects/full_screen_browser.png",confidence=.75))
time.sleep(4.5)
click(pyautogui.locateCenterOnScreen("./vobjects/fb_logo.png",confidence=.88))
time.sleep(3)

click(pyautogui.locateCenterOnScreen("./vobjects/fblogin/mobile.png",confidence=.75))
time.sleep(.30)
pyautogui.typewrite(mob,0.08)

click(pyautogui.locateCenterOnScreen("./vobjects/fblogin/pw_box.png",confidence=.75))
time.sleep(.30)
pyautogui.typewrite(pas,0.08)

click(pyautogui.locateCenterOnScreen("./vobjects/fblogin/login.png",confidence=.75))
time.sleep(4.7)

double_click(pyautogui.locateCenterOnScreen("./vobjects/fblogin/login_ok.png",confidence=.88))
time.sleep(1)

#click(pyautogui.locateCenterOnScreen("./vobjects/fbm/messenger.png",confidence=.88))

keep_trying = True
while keep_trying:
    try:
        time.sleep(0.5)
        x = pyautogui.locateCenterOnScreen("./vobjects/fbm/messenger_plus_y.png",confidence=.88)
        pyautogui.moveTo(x.x,(x.y-80))
        pyautogui.leftClick()
        keep_trying = False
    except:
        pass

time.sleep(3.1)

click(pyautogui.locateCenterOnScreen("./vobjects/cvs/vimal.png",confidence=.88))
time.sleep(1.8)
pyautogui.scroll(-250)
time.sleep(.2)
click(pyautogui.locateCenterOnScreen("./vobjects/fbm/message_box.png",confidence=.88))
pyautogui.typewrite("Sending this message from a robot [] _ []. Check the video I just sent you!",0.08)

click(pyautogui.locateCenterOnScreen("./vobjects/fbm/send.png",confidence=.88))

print(screenWidth, screenHeight)