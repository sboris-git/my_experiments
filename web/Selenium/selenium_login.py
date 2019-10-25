import time
from selenium import webdriver

username = 'username' # login
paswd = "********"
url = 'https://www.linkedin.com/login'
pause = 2  # sec
# driver = webdriver.Chrome('/home/stable/Apps/chromedriver')
driver = webdriver.Chrome(r'/home/boris/Apps/chromedriver')

# Move the window to the top middle of the primary monitor
driver.set_window_position(900, 0)

driver.get(url)
print("Locating and fill in username")
username_elem = driver.find_element_by_id('username')
username_elem.send_keys(username)
time.sleep(pause)

print("Locating and fill in password form...")
passwd_elem = driver.find_element_by_id('password')
passwd_elem.send_keys(paswd)
time.sleep(pause)

print("Locating a Sign in button and clicking it...")
xpath = '//button[contains(@aria-label,"Sign in")]'
driver.find_element_by_xpath(xpath).click()
time.sleep(pause)

actualUrl = "https://www.linkedin.com/feed/"
expectedUrl = driver.current_url
# driver.assertEquals(expectedUrl, actualUrl)
# assertEqual is a method that belongs to the class TestCase from the unittest module (python unittest docs)
try:
    assert expectedUrl in actualUrl
    print("Assertion test completed successfully")
except AssertionError:
    print('Assertion test failed')

# driver.assertEquals('Url', 'Url')
print()

driver.quit()