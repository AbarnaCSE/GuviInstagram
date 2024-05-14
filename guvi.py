from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.common.alert import Alert

class Form:

   def __init__(self, url):
       self.url = url
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


   def boot(self):
       self.driver.get(self.url)
       self.driver.maximize_window()
       self.wait(5)

   def wait(self, secs):
       sleep(secs)

   def quit(self):
       self.driver.quit()

   def acceptAlerts(self):
       try:
           self.boot()
           self.wait(3)
           followers_element =  self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button/span')
           following_element =  self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[3]/button/span')
           self.wait(3)
           followers_count = followers_element.text
           following_count = following_element.text
           self.wait(3)
           print('Followers:', followers_count)
           print('following:', following_count)

       except NoSuchElementException as e:
           print(e)


       finally:
           self.wait(3)
           self.quit()


url = "https://www.instagram.com/guviofficial/"
f = Form(url)
f.acceptAlerts()
