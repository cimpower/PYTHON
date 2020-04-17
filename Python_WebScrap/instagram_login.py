from selenium import webdriver
from secrets import pw
import time
class Instabot:
    def __init__(self,usuario,pw):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Entrar')]")\
            .click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(usuario)
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        time.sleep(5)
Instabot('javiemg', pw)