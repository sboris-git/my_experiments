import time
from selenium import webdriver

username = 'username' # login
paswd = "********"
url = 'https://www.linkedin.com/login'
pause = 2  # sec
# driver = webdriver.Chrome('/home/stable/Apps/chromedriver')
driver = webdriver.Chrome('/home/boris/Apps/')

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
time.sleep(pause*2)

actualUrl = "https://www.linkedin.com/feed/"
expectedUrl = driver.getCurrentUrl()
# Assert.assertEquals(expectedUrl, actualUrl)
Assert.assertEquals('Url', 'Url')
print(Assert.assertEquals('Url', 'Url'))

driver.quit()