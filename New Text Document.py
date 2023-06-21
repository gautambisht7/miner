from selenium import webdriver
from pynput.keyboard import Key, Controller
keyboard = Controller()
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get('https://miner.eo.finance/')  # Replace with the actual EO Miner website URL
login_button = driver.find_element("id",'login_button').click()
login_click = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[1]/div/form/div[5]/span").click()
username_input = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[1]/div/form/label[1]/input")
password_input = driver.find_element(By.XPATH,'//*[@id="page-view"]/div[2]/div/div[1]/div/form/label[2]/div/input')  # Replace with the actual name of the password input field

username_input.send_keys('gautambisht709@gmail.com')  # Replace 'your_username' with your actual username
password_input.send_keys('e8c2cadf2149')  # Replace 'your_password' with your actual password
enter = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[1]/div/form/button[2]").click()

driver.implicitly_wait(10)
while 1 == 1:
    print("hello")
