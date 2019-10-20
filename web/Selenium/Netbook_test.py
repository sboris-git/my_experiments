import time
from selenium import webdriver

# pass
string = 'beautiful places in the world' # 'search phrase'
url = 'https://www.google.com/'
driver = webdriver.Firefox('/home/dad/bin/')

driver.get(url)
search_box = driver.find_element_by_name('q').send_keys(string)#\n.click()
driver.find_element_by_name('btnK').submit()

time.sleep(2)
elems = driver.find_elements_by_xpath('.//a')
target_link = driver.find_element_by_partial_link_text(string)  # Ok
print(target_link.get_attribute("href"))
time.sleep(1)

target_link.click()
# driver.execute_script("window.scrollTo(0, 800)")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # to scroll to the bottom of the page.
# time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(2)
driver.execute_script("window.scrollTo(0, 0);") # to scroll back to the top of the page.

# time.sleep(2)
class_name = 'dtviD'
content = driver.find_elements_by_xpath('//span[contains(@class, "dtviD")]') # Ok
[print(item.text) for item in content]

wonder = driver.find_element_by_xpath('//*[@id="rg_s"]/div[2]/a[2]/div[1]')
link_to_go = driver.find_element_by_partial_link_text(wonder.text)
print(wonder.text, link_to_go.get_attribute('href'))
link_to_go.click()
time.sleep(5)
# open in new tab
body = driver.find_element_by_tag_name("body")
body.send_keys(Keys.CONTROL + '2')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # to scroll to the bottom of the page.
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, 0);") # to scroll back to the top of the page.

time.sleep(5)

driver.quit()