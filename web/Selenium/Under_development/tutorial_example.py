from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from subprocess import Popen
from subprocess import run

def terminate(process):
    '''Terminate video recording'''
    if process.poll() is None:
        run('taskkill /F /T /PID ' + str(process.pid))


# from pyvirtualdisplay import Display
# display = Display(visible=0, size=(800, 800))
# display.start()
cmd = 'ffmpeg -y -rtbufsize 2000M -f dshow  -i video="screen-capture-recorder" -s 1920x1080 -b:v 512k -r 20 -vcodec libx264 test.avi'
videoRecording = run(cmd + "&") #Popen(cmd) # start recording

driver = webdriver.Chrome('/home/stable/Apps/chromedriver')
driver.get("http://www.google.com")
input_element = driver.find_element_by_name("q")
input_element.send_keys("python")
input_element.submit()
# driver.implicitly_wait(10)

RESULTS_LOCATOR = "//div[1]/a[1]/h3"
# //*[@id="rso"]/div[1]/div/div/div/div/div[1]/a[1]/h3
WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.XPATH, RESULTS_LOCATOR)))
page1_results = driver.find_elements(By.XPATH, RESULTS_LOCATOR)
for item in page1_results:
    if item != None: print(item.text)

terminate(videoRecording)   # terminates recording
driver.quit()
