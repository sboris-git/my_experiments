import time
from selenium import webdriver
# import urllib.parse as urlparse
from selenium.webdriver.common.by import By

username = 'boris.v.skip@gmail.com' # login
paswd = "*******"
url = 'https://www.linkedin.com/login'
pause = 2 # sec
driver = webdriver.Chrome(r'/home/stable/Apps/chromedriver')

# driver.get('http://www.google.com/')
# search_box = driver.find_element_by_name('q').send_keys(string)#\n.click()
# #search_box.submit()
# #time.sleep(2) #

driver.get(url)
search_box = driver.find_element_by_id('username')  # .send_keys(string)
# https://dzone.com/articles/selenium-java-tutorial-how-to-test-login-process
# driver.findElement(By.id(“password”));
# WebElement password=driver.findElement(By.id(“password”));
# driver.findElement(By.xpath(“//button[text()=’Sign in’]”));
# import org.openqa.selenium.WebElement;
# https://crossbrowsertesting.com/blog/test-automation/automate-login-with-selenium/

# WebElement login= driver.findElement(By.xpath(“//button[text()=’Sign in’]”));
# username.sendKeys(“xyz@gmail.com”);
# password.sendKeys(“exampleAboutSelenium123”);
# login.click();
# actualUrl="https://www.linkedin.com/feed/";
#   String expectedUrl= driver.getCurrentUrl();
#   Assert.assertEquals(expectedUrl,actualUrl);

driver.find_element_by_name('btnK').submit()
target_link = driver.find_element_by_partial_link_text(string) # Ok
print(target_link.get_attribute("href"))
time.sleep(pause)


driver.quit()