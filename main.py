from selenium import webdriver
import time
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get('https://www.youlikehits.com') 
time.sleep(6)
login_button = driver.find_element(By.XPATH,"/html/body/table[1]/tbody/tr/td/table/tbody/tr/td[2]/a[2]/div").click()
time.sleep(3)
username = driver.find_element(By.XPATH,'''//*[@id="username"]''').send_keys('gauambisht709')
password = driver.find_element(By.XPATH,'''//*[@id="password"]''').send_keys('e8c2cadf2149')
submit = driver.find_element(By.XPATH,'''/html/body/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/center/form/table/tbody/tr[3]/td/span/input''').click()
print('logged in')
time.sleep(8)
earn = driver.find_element(By.XPATH,'''/html/body/div/table[1]/tbody/tr[2]/td/table/tbody/tr/td/nav/ul/li[2]/a''').click()
time.sleep(2)
youtube = driver.find_element(By.XPATH,'''/html/body/div/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/center/div[7]/div''').click()
time.sleep(3)
print('earning')
while True:
    click = 1
    view_button = driver.find_element(By.XPATH,'//*[@id="listall"]/center/a[1]').click()
    print(click)
    time.sleep(120)
    driver.refresh()
    click+=1
   
