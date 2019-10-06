import time
from selenium import webdriver
# import urllib.parse as urlparse
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # to open a link in new tab
# from selenium.webdriver.common.action_chains import ActionChains # scroll


# https://selenium-python.readthedocs.io/locating-elements.html
# https://www.techbeamers.com/locate-elements-selenium-python/
# https://www.browserstack.com/guide/locators-in-selenium
# https://www.pluralsight.com/guides/web-scraping-with-selenium
# https: // www.guru99.com / locate - by - link - text - partial - link - text.html
# https://www.youtube.com/watch?v=Mhj3p5Vo5bA

string = 'beautiful places in the world' # 'search phrase'
url = 'https://www.google.com/'
driver = webdriver.Chrome(r'/home/stable/Apps/chromedriver')  # Optional argument, if not specified will search path.
# driver = webdriver.Chrome('/home/boris/Apps/chromedriver')  # Optional argument, if not specified will search path.
# driver.get('http://www.google.com/')
# time.sleep(1) # Let the user actually see something!
# search_box = driver.find_element_by_name('q').send_keys(string)#\n.click()
# #search_box.submit()
# #time.sleep(2) # Let the user actually see something!
# #driver.find_element_by_xpath('/html/body/div/div[3]/form/div[2]/div/div[3]/center/input[1]').click()
#
# # search_box.submit() #Ok
# # driver.find_element_by_name('q').submit() #Ok click() - doesn't work
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
linkList = []
driver.get(url)
search_box = driver.find_element_by_name('q').send_keys(string)#\n.click()
driver.find_element_by_name('btnK').submit()
# text = driver.find_element_by_xpath('//*[@id="lst-ib"]')
# text.send_keys(string)

time.sleep(2)
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
time.sleep(1)

target_link.click()
# driver.execute_script("window.scrollTo(0, 800)")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # to scroll to the bottom of the page.
# time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(2)
driver.execute_script("window.scrollTo(0, 0);") # to scroll back to the top of the page.

# driver.switchTo().window(windowName); to access any tab or window.
# driver.FindElement(By.CssSelector("body")).SendKeys(Keys.Control + "t");
# string newTabInstance = driver.WindowHandles[driver.WindowHandles.Count-1].ToString();
# driver.SwitchTo().Window(newTabInstance);
# driver.Navigate().GoToUrl(url);
# sendKeys(Keys.CONTROL + "\t")

# time.sleep(2)
class_name = 'dtviD'
content = driver.find_elements_by_xpath('//span[contains(@class, "dtviD")]') # Ok
# XPath: //div[contains(@class, 'article-heading')]
[print(item.text) for item in content]

# //*[@id="rg_s"]/div[2]/a[2]/div[1]
# Next jump mVDMnf nJGrxf
# wonder = driver.find_elements_by_xpath('//span[contains(@class, "mVDMnf nJGrxf")]')#does not work
wonder = driver.find_element_by_xpath('//*[@id="rg_s"]/div[2]/a[2]/div[1]')
link_to_go = driver.find_element_by_partial_link_text(wonder.text)
print(wonder.text, link_to_go.get_attribute('href'))
link_to_go.click()
time.sleep(5)
# open in new tab
body = driver.find_element_by_tag_name("body")
body.send_keys(Keys.CONTROL + '2')
# target = driver.find_elements_by_id('navcnt')
# target = driver.find_element_by_partial_link_text('amazing')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # to scroll to the bottom of the page.
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, 0);") # to scroll back to the top of the page.
# target = driver.find_element_by_partial_link_text('Завантаження')

# //Create an ArrayList and store the open tabs
# ArrayList<String> tabs = new ArrayList<String>(driver.getWindowHandles());
# //below code will switch to new tab
# driver.switchTo().window(tabs.get(1));
# //perform whatever actions you want in new tab then close it
# driver.close();
# //Switch back to your original tab
# driver.switchTo().window(tabs.get(0));

time.sleep(5)


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


print("*"*50)
# span class ="dtviD"
# linkBox = driver.find_element_by_xpath('//*[@id="nav"]/tbody/tr')
# links = linkBox.find_elements_by_css_selector('a')
#
# for link in links:
#     linkList.append(link.get_attribute('href'))
#
# print(linkList)

driver.quit()