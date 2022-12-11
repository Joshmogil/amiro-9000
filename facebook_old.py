import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains



from dotenv import load_dotenv

load_dotenv("./.env")
fb_email = os.getenv("FACEBOOK_USER")
fb_pass = os.getenv("FACEBOOK_PASS")

## Setup chrome options
WINDOW_SIZE = "500,500"
chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
#chrome_options.add_argument("--no-sandbox")
# Set path to chromedriver as per your configuration
webdriver_service = Service(f"./chromedriver/stable/chromedriver")
# Choose Chrome Browser
browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

try:

# Get page
    browser.get("https://m.facebook.com/")


    email_input = browser.find_element(By.ID, "m_login_email")
    print(email_input)
    email_input.send_keys(fb_email)

    password_input = browser.find_element(By.ID, "m_login_password")
    print(password_input)
    password_input.send_keys(fb_pass)

    browser.get_screenshot_as_file("./screenshots/login_with_creds.png")

    time.sleep(0.35)
    ac = ActionChains(browser)

    login_btn = browser.find_element(By.XPATH,"//button[@name='login']")
    print(login_btn)
    login_btn.screenshot("./screenshots/login_btn.png")
    login_btn.send_keys(Keys.RETURN)

    time.sleep(.55)
    login_btn.submit()
    time.sleep(.35)
    browser.get_screenshot_as_file(f"./screenshots/logged_in.png")


    ok_btn = browser.find_element(By.XPATH,"(//button[@value='OK'])[1]")
    print(ok_btn)
    ok_btn.screenshot("./screenshots/ok_btn.png")
    ac.move_to_element(password_input)
    time.sleep(.55)
    ac.double_click()
    ac.perform()
    time.sleep(0.25)
    browser.get_screenshot_as_file(f"./screenshots/logged_in1.png")

    browser.quit()
except Exception as e:
    print(e)
    browser.quit()



"""

for i in (-40,-35):
    time.sleep(0.35)
    ac.move_to_element(password_input)
    ac.move_by_offset(10,-35)
    ac.click()
    ac.perform()
    time.sleep(0.80)
    browser.get_screenshot_as_file(f"./screenshots/tests/logged_in{i}.png")
    print(i)


login_ok_button = browser.find_element(By.NAME, "Ok")
ac.click(login_ok_button).perform()
time.sleep(0.35)
browser.get_screenshot_as_file(f"./logged_in.png")
"""


# Extract description from page and print
#description = browser.find_element(By.NAME, "description").get_attribute("content")
#print(f"{description}")

#Wait for 10 seconds


browser.quit()

