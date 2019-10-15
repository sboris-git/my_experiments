import time
from selenium import webdriver
from selenium.webdriver.common.by import By


pause = 2  # sec. Necessary in order to see what is happening with browser context
print('Init web browser')
orig_string = 'beautiful places in the world'  # 'search phrase'
url = 'https://www.google.com/'
driver = webdriver.Chrome(r'/home/stable/Apps/chromedriver')  # Optional argument, if not specified will search path.
# driver = webdriver.Chrome('/home/boris/Apps/chromedriver')  # Optional argument, if not specified will search path.
driver.get(url)

print('Typing search string and submit')
search_box = driver.find_element_by_name('q').send_keys(orig_string)
driver.find_element_by_name('btnK').submit()
print('Waiting a moment')
driver.implicitly_wait(pause)  # wait for action

target_link = driver.find_element_by_partial_link_text(orig_string)
print(target_link.get_attribute("href"))

time.sleep(pause)
print('Clicking target link')
target_link.click()
time.sleep(pause)

for n in range(0,4):
    print('Scrolling down screen by height')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # to scroll to the bottom of the page.
    time.sleep(pause)
print('Scrolling up screen to start of the page')
driver.execute_script("window.scrollTo(0, 0);")  # to scroll back to the top of the page.
driver.implicitly_wait(pause+3)  # wait for action
print('Selecting a category element')
class_name = 'dtviD'
content = driver.find_elements_by_xpath('//span[contains(@class, "{}")]'.format(class_name))  # Ok
target = [item.text for item in content]
print('Retrieved categories: ', target)
# Next jump
print("Let's choose the 4th in the list: {}".format(target[3]))  # //*[@id="isr_chc"]/div[1]/div/a[4]/div/span
link_to_go = driver.find_element_by_partial_link_text(target[3])
print("Clicking the chosen link", link_to_go.get_attribute("href"))
# open link_to_go in a new tab
href_link = link_to_go.click()  # get_attribute("href")

time.sleep(pause*2)
print("Let's select links from google search results")
RESULTS_LOCATOR = '''//div[3]/a[2]/div[1]'''
# //*[@id="rg_s"]/div[3]/a[2]/div[1]
# /html/body/div[5]/div[3]/div[3]/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div[3]/a[2]
# <a class="iKjWAf irc-nic isr-rtc a-no-hover-decoration" href="https://vacationidea.com/getaways/most-beautiful-places-in-the-world.html" jsaction="mouseover:m8Yy5c;mousedown:QEDpme;focus:QEDpme;" rel="noopener" target="_blank"><div class="mVDMnf nJGrxf">25 Most Beautiful Places in the World</div><div class="nJGrxf FnqxG"><span>vacationidea.com</span></div></a>
page_results = driver.find_elements(By.XPATH, RESULTS_LOCATOR)
print('Page results number', len(page_results))

for item in page_results: print(item.text, item.get_attribute("href"))
print("Change the view of google's results")
link_to_go = driver.find_element_by_partial_link_text('Усі')
print("Clicking the chosen link", link_to_go.get_attribute("href"))
link_to_go.click()

RESULTS_LOCATOR = '''//div[1]/a[1]/h3'''  # Locator - headers <h3>
page_results = driver.find_elements(By.XPATH, RESULTS_LOCATOR)
print('Page results number', len(page_results))
target_key = '30'
for item in page_results:
    element = item.text
    print(element, item.get_attribute("href"))
    if element.find(target_key) != -1:
        item.click()
        print('There is a match with {}'.format(target_key))
        break

time.sleep(pause*2)
start_position = 0
scrolldown = 400
for n in range(0, 6):
    print('Scrolling down screen by height')
    driver.execute_script("window.scrollTo({}, {})".format(start_position, scrolldown))
    start_position += 400
    scrolldown += scrolldown
    time.sleep(pause)

time.sleep(pause)
print("That's all Folks! I love this stuff!")
driver.quit()
