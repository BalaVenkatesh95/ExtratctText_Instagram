import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class ExtractClass:
   def __init__(self, url):
       self.url = url
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))





   # browser initiation and url navigation
   def initiation_function(self):
       try:
           self.driver.maximize_window()
           self.driver.get(self.url)
           return True
       except:
           print("ERROR : URL is incorrect/Network Error")
           return False


   # Quit browser
   def shutdown(self):
       if self.initiation_function():
           return self.driver.quit()
       else:
           return False

   def fetch_url(self):
       if self.initiation_function():
           return self.driver.current_url
       else:
           return False

   # Function to extract text using XPATH of Webelement
   def extract_text(self):
       if self.initiation_function():
           wait_time = 15
           element = WebDriverWait(self.driver, wait_time).until(
               EC.presence_of_element_located((By.XPATH, "//button[ contains(., 'followers')]")))
           total_followers = self.driver.find_element(By.XPATH, "//button[ contains(., 'followers')]").text
           print("Followers of GUVI:", total_followers)
           total_following = self.driver.find_element(By.XPATH, "//button[ contains(., 'following')]").text
           print("Number of pages or people followed by GUVI:", total_following)
       else:
           return False
