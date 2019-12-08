import time
from selenium import webdriver
# from selenium.webdriver.common.by import By

import unittest


# python -m unittest -v test_task100.py
class TestTasks(unittest.TestCase):
    '''test of 100 tests'''

    @classmethod
    def setUpClass(cls):
        print('setupClass')
        # cls.driver = webdriver.Chrome(r'C:\Users\bskiptc\Documents\Selenium\chromedriver')
        # webdriver.Chrome(executable_path=os.path.abspath("chromedriver.exe")

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')
        # cls.driver.quit()

    def setUp(self):
        print('setUp')
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome(r'C:\Users\bskiptc\Documents\Selenium\chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('https://localhost:44364/home/events?page=1')
        # self.driver.title


    def tearDown(self):
        print('tearDown')
        self.driver.close()


    def test_Selenium(self):
        print('Sign In')
        pause = 3

        print("Locating a Sign in button and clicking it...")
        xpath = '//*[@id="root"]/div[2]/div/div/div/button/span[1]'  # Ok
        self.driver.find_element_by_xpath(xpath).click()  # Ok
        time.sleep(pause)

        print("Locating and fill in username")
        username = 'user@gmail.com'  # login
        # name = email
        username_elem = self.driver.find_element_by_name('email')
        username_elem.send_keys(username)

        print("Locating and fill in password form...")
        paswd = "1qaz1qaz"
        # name = password
        passwd_elem = self.driver.find_element_by_name('password')
        passwd_elem.send_keys(paswd)
        time.sleep(pause)

        print("Locating a Sign in button and clicking it...")
        # text = 'Sign In'
        css_sel = "[value~='Login']"
        # "body > div.MuiDialog-root > div.MuiDialog-container.MuiDialog-scrollPaper > div > div > div.MuiTypography-root.MuiTypography-body1 > div > div.auth > form > div:nth-child(3) > div > button:nth-child(2)"

        self.driver.find_element_by_css_selector(css_sel).click()

        print("Moving on navigate menu...")
        for item in range(1, 6):
            css_sel = f".sidebar-header:nth-child({item}) .link"
            time.sleep(pause)
            self.driver.find_element_by_css_selector(css_sel).click()
            time.sleep(pause)

        print('Back to "Profile" menu...')
        # Back to "Profile" menu
        css_sel = ".sidebar-header:nth-child(2) .link"
        self.driver.find_element_by_css_selector(css_sel).click()
        time.sleep(pause)

        print("Moving on events groups menu...")
        for i in range(5):
            css_sel = "#full-width-tab-{} > .MuiTab-wrapper".format(i)
            self.driver.find_element_by_css_selector(css_sel).click()
            time.sleep(pause)

        print('Back to "Archive events" menu...')
        css_sel = "#full-width-tab-1 > .MuiTab-wrapper"
        self.driver.find_element_by_css_selector(css_sel).click()
        time.sleep(pause)


if __name__ == '__main__':
    unittest.main()





