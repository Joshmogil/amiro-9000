import pyautogui
import time
import dotenv , os
from pyscreeze import Point
from chat_wrap import get_broscience

dotenv.load_dotenv(".env")

mob = os.getenv("FB_MOBILE")
pas = os.getenv("FB_PASSWORD")

delay = 3
screenWidth, screenHeight = pyautogui.size()
#pyautogui.moveTo(0, 0, delay)


click = pyautogui.leftClick
double_click = pyautogui.doubleClick


GROUP_CHAT_NAME="Mr. Arige and"

####some assumptions###
#1. pop os linux 
#2. using mozilla firefox
#3. facebook mobilized
#----> see vobjects screenshots to see exactly what it is looking for

#Confidence intervals could use some adjustment.
def send_mess_to_chat():
    """
    click(pyautogui.locateCenterOnScreen("./vobjects/firefox.png",confidence=.75))
    #double_click(pyautogui.locateCenterOnScreen("./vobjects/full_screen_browser.png",confidence=.75))
    time.sleep(8)
    click(pyautogui.locateCenterOnScreen("./vobjects/fb_logo.png",confidence=.88))
    time.sleep(4)

    click(pyautogui.locateCenterOnScreen("./vobjects/fblogin/mobile.png",confidence=.75))
    time.sleep(.30)
    pyautogui.typewrite(mob,0.08)

    click(pyautogui.locateCenterOnScreen("./vobjects/fblogin/pw_box.png",confidence=.75))
    time.sleep(.30)
    pyautogui.typewrite(pas,0.08)

    click(pyautogui.locateCenterOnScreen("./vobjects/fblogin/login.png",confidence=.75))
    time.sleep(4.7)

    double_click(pyautogui.locateCenterOnScreen("./vobjects/fblogin/login_ok.png",confidence=.88))
    time.sleep(4.5)

    click(pyautogui.locateCenterOnScreen("./vobjects/fbm/amirosmessages.png",confidence=.92))
    time.sleep(.05)
    click(pyautogui.locateCenterOnScreen("./vobjects/fbm/amiromessengernotif.png",confidence=.92))
    time.sleep(.21)
    #click(pyautogui.locateCenterOnScreen("./vobjects/fbm/messenger.png",confidence=.88))
    time.sleep(2)
    attempts = 0
    keep_trying = True
    while keep_trying:
        try:
            time.sleep(0.5)
            x = pyautogui.locateCenterOnScreen("./vobjects/fbm/messenger_plus_y.png",confidence=.88)
            pyautogui.moveTo(x.x,(x.y-80))
            pyautogui.leftClick()
            keep_trying = False
        except:
            attempts += 1
            print(attempts)
            if attempts == 5: keep_trying = False
            pass
    

    time.sleep(4)

    click(pyautogui.locateCenterOnScreen("./vobjects/fbm/search.png",confidence=.88))
    time.sleep(.21)
    pyautogui.typewrite(GROUP_CHAT_NAME,0.08)
    time.sleep(.35)
    click(pyautogui.locateCenterOnScreen("./vobjects/cvs/gc_pic.png",confidence=.88))
    time.sleep(1.8)
    """

    pyautogui.scroll(-250)
    time.sleep(.2)
    click(pyautogui.locateCenterOnScreen("./vobjects/fbm/message_box.png",confidence=.88))

    message = get_broscience()

    pyautogui.typewrite(message,0.08)
    time.sleep(.2)
    click(pyautogui.locateCenterOnScreen("./vobjects/fbm/send.png",confidence=.88))
    time.sleep(2)
    
    #click(pyautogui.locateCenterOnScreen("./vobjects/closewindow.png",confidence=.88))


if __name__ == "__main__":
    send_mess_to_chat()

print(screenWidth, screenHeight)