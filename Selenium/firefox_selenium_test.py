import time
from selenium import webdriver

driver = webdriver.Chrome('/home/boris/Apps/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/')
#driver.get('https://www.google.com.ua/search?q=selenium+click+button+python&oq=selenium+click+button+&aqs=chrome.2.69i57j0l5.20322j0j7&client=ubuntu&sourceid=chrome&ie=UTF-8')
time.sleep(1) # Let the user actually see something!
search_box = driver.find_element_by_name('q').send_keys('patents brightener copper bath')#\n.click()
#search_box.submit()
time.sleep(2) # Let the user actually see something!
#driver.find_element_by_xpath('/html/body/div/div[3]/form/div[2]/div/div[3]/center/input[1]').click()

# search_box.submit() #Ok
# driver.find_element_by_name('q').submit() #Ok click() - doesn't work
# driver.find_element_by_name('btnK').submit()# Ok

driver.get_screenshot_as_png()
time.sleep(2) # Let the user actually see something!
driver.quit()
'''
#tsf > div:nth-child(2) > div.A8SBwf.emcat > div.FPdoLc.VlcLAe > center > input.gNO89b

//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]

<input class="gNO89b" value="Пошук Google" aria-label="Пошук Google" name="btnK" type="submit" data-ved="0ahUKEwigt52j_dfkAhVEx4sKHcgCBNMQ4dUDCAo">

'''
