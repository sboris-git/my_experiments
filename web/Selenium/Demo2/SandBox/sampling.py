pause = 3
driver.get('https://localhost:44364/home/events?page=1')
driver.set_window_position(900, 0)
# https://localhost:44364/
assert 'EventsExpress' in driver.title

print("Locating a Sign in button and clicking it...")
xpath = '//*[@id="root"]/div[2]/div/div/div/button/span[1]' # Ok
driver. find_element_by_xpath(xpath).click() # Ok
time.sleep(pause)

print("Locating and fill in username")
username = 'user@gmail.com' # login
# name = email
username_elem = driver.find_element_by_name('email')
username_elem.send_keys(username)

print("Locating and fill in password form...")
paswd = "1qaz1qaz"
# name = password
passwd_elem = driver.find_element_by_name('password')
passwd_elem.send_keys(paswd)
time.sleep(pause)


print("Locating a Sign in button and clicking it...")
# text = 'Sign In'
css_sel = "body > div.MuiDialog-root > div.MuiDialog-container.MuiDialog-scrollPaper > div > div > div.MuiTypography-root.MuiTypography-body1 > div > div.auth > form > div:nth-child(3) > div > button:nth-child(2)"
driver.find_element_by_css_selector(css_sel).click()

print("Moving on navigate menu...")
for item in range(1, 6):
    css_sel = f".sidebar-header:nth-child({item}) .link"
    time.sleep(pause)
    driver.find_element_by_css_selector(css_sel).click()
    time.sleep(pause)

print('Back to "Profile" menu...')
# Back to "Profile" menu
css_sel = ".sidebar-header:nth-child(2) .link"
driver.find_element_by_css_selector(css_sel).click()
time.sleep(pause)

print("Moving on events groups menu...")
for i in range(5):
    css_sel = "#full-width-tab-{} > .MuiTab-wrapper".format(i)
    driver.find_element_by_css_selector(css_sel).click()
    time.sleep(pause)

print('Back to "Archive events" menu...')
css_sel = "#full-width-tab-1 > .MuiTab-wrapper"
driver.find_element_by_css_selector(css_sel).click()
time.sleep(pause)





# driver.assertEquals(expectedUrl, actualUrl)
# assertEqual is a method that belongs to the class TestCase from the unittest module (python unittest docs)
#     try:
#         assert expectedUrl in actualUrl
#         print("Assertion test completed successfully")
#     except AssertionError:
#         print('Assertion test failed')

# driver.assertEquals('Url', 'Url')
print()