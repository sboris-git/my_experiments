import time
from selenium import webdriver
# import urllib.parse as urlparse
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # to open a link in new tab
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains # scroll


# https://selenium-python.readthedocs.io/locating-elements.html
# https://www.techbeamers.com/locate-elements-selenium-python/
# https://www.browserstack.com/guide/locators-in-selenium
# https://www.pluralsight.com/guides/web-scraping-with-selenium
# https: // www.guru99.com / locate - by - link - text - partial - link - text.html
# https://www.youtube.com/watch?v=Mhj3p5Vo5bA

string = 'beautiful places in the world' # 'search phrase'
url = 'https://www.google.com/'
pause = 2 # sec
driver = webdriver.Chrome(r'/home/stable/Apps/chromedriver')  # Optional argument, if not specified will search path.
# driver = webdriver.Chrome('/home/boris/Apps/chromedriver')  # Optional argument, if not specified will search path.
# export PATH="$HOME/bin:$PATH"
# driver.get('http://www.google.com/')
# search_box = driver.find_element_by_name('q').send_keys(string)#\n.click()
# #search_box.submit()
# #time.sleep(2) #
# #driver.find_element_by_xpath('/html/body/div/div[3]/form/div[2]/div/div[3]/center/input[1]').click()
#
# # search_box.submit() #Ok
# # driver.find_element_by_name('q').submit() #Ok but - click() - doesn't work
# driver.find_element_by_name('btnK').submit()# Ok
# time.sleep(2) # Waiting for query result!
#
# # driver.get_screenshot_as_png()
# results = driver.find_elements_by_css_selector('div.g')
# link = results[0].find_element_by_tag_name("a")
# href = link.get_attribute("href")
# par = urlparse.parse_qs(urlparse.urlparse(href).query)
# print(par['q'][0], par['source'][0])
#
driver.get(url)
search_box = driver.find_element_by_name('q').send_keys(string)#\n.click()
driver.find_element_by_name('btnK').submit()
# text = driver.find_element_by_xpath('//*[@id="lst-ib"]')
# text.send_keys(string)

driver.implicitly_wait(2)# wait for action
#elems = driver.find_elements_by_xpath("//a[@href]")
elems = driver.find_elements_by_xpath('.//a')
# content = driver.find_element_by_class_name(class_name)

# strings = driver.find_elements_by_id('iUh30 bc') # doent work
# for hrefs in strings:
#     print('-', hrefs.get_attribute("href"))
# click submit button

target_link = driver.find_element_by_partial_link_text(string) # Ok
print(target_link.get_attribute("href"))
# target_link.click()

# actions = ActionChains(driver)
# actions.move_to_element(target)
# actions.perform()
# target.location_once_scrolled_into_view
# driver.implicitly_wait(pause)# wait for action
time.sleep(pause)

target_link.click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # to scroll to the bottom of the page.
# driver.implicitly_wait(pause)# wait for action
time.sleep(pause)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# driver.implicitly_wait(pause)# wait for action
time.sleep(pause*2)
driver.execute_script("window.scrollTo(0, 0);") # to scroll back to the top of the page.
# driver.implicitly_wait(pause+3)# wait for action
time.sleep(pause*2)
# driver.switchTo().window(windowName); to access any tab or window.
# driver.FindElement(By.CssSelector("body")).SendKeys(Keys.Control + "t");
# string newTabInstance = driver.WindowHandles[driver.WindowHandles.Count-1].ToString();
# driver.SwitchTo().Window(newTabInstance);
# driver.Navigate().GoToUrl(url);
# sendKeys(Keys.CONTROL + "\t")

class_name = 'dtviD'
content = driver.find_elements_by_xpath('//span[contains(@class, "{}")]'.format(class_name)) # Ok
# XPath: //div[contains(@class, 'article-heading')]
#tag = []
tag = [item.text for item in content]
print('tag3: ', tag[3])
# Next jump mVDMnf nJGrxf
# wonder = driver.find_elements_by_xpath('//span[contains(@class, "mVDMnf nJGrxf")]')#does not work
# wonder = driver.find_element_by_xpath('//*[@id="isr_chc"]/div[1]/div/a[4]/div/span')
link_to_go = driver.find_element_by_partial_link_text(tag[3])
# print('tags: ', wonder.text) # , link_to_go.get_attribute('href')
# open link_to_go in a new tab
body = driver.find_element_by_tag_name("body")
body.send_keys(Keys.CONTROL + '2')

driver.execute_script("window.scrollTo(0, 0);") # to scroll back to the top of the page.
link_to_go.click()
print('link_to_go: ')
#time.sleep(pause)
driver.implicitly_wait(pause)

# popup_close = driver.find_element_by_xpath('//*[@id="bx-close-inside-1060544"]') # find close element of popup element
# # //*[@id="bx-close-inside-1060544"]
# popup_close.click()
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # to scroll to the bottom of the page.
# # driver.implicitly_wait(pause)
# time.sleep(pause)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# driver.implicitly_wait(pause)
# Machu Picchu
time.sleep(pause)
# target = driver.find_elements_by_id('navcnt')
# target = driver.find_element_by_partial_link_text('amazing')

# target = driver.find_element_by_partial_link_text('Завантаження')
# print('----------------------{}'.format(pause))
# //Create an ArrayList and store the open tabs
# ArrayList<String> tabs = new ArrayList<String>(driver.getWindowHandles());
# //below code will switch to new tab
# driver.switchTo().window(tabs.get(1));
# //perform whatever actions you want in new tab then close it
# driver.close();
# //Switch back to your original tab
# driver.switchTo().window(tabs.get(0));

# driver.implicitly_wait(10)# wait for action
time.sleep(pause*5)
# content = driver.find_elements(By.CLASS_NAME, class_name)
# content = driver.find_elements_by_css_selector('//span[contains(@class, "dtviD")]') # Ok
# print(content.text, len(content))

#[print(item.text) for item in content]
# content = driver.find_elements_by_css_selector('//span[contains(@class, "dtviD")]') # Ok
# print(content.text)
# CSS: css=div.article-heading

# get_div = driver.find_element_by_class_name('round-button')
# text = driver.find_element_by_xpath('//*[@id="lst-ib"]')
# for links in content:
#     print(links.get_attribute("href"))


# span class ="dtviD"
# linkBox = driver.find_element_by_xpath('//*[@id="nav"]/tbody/tr')
# links = linkBox.find_elements_by_css_selector('a')
#
# for link in links:
#     linkList.append(link.get_attribute('href'))
#
# print(linkList)

driver.quit()