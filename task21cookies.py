import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC






class SauceDemo:


   def __init__(self):
       self.chrome_options = Options()
       self.chrome_options.add_argument("--incognito")
       self.driver = webdriver.Chrome(options=self.chrome_options)
       self.url = "https://www.saucedemo.com/"


   def boot(self):
       self.driver.maximize_window()
       self.driver.get(self.url)


   def quit(self):
       self.driver.quit()


   def getCookies(self):
       return self.driver.get_cookies()


   def login(self):
       try:
           username_field = WebDriverWait(self.driver, 20).until(
               EC.visibility_of_element_located((By.ID, "user-name"))
           )
           password_field = self.driver.find_element(By.ID, "password")
           login_button = self.driver.find_element(By.ID, "login-button")


           username_field.send_keys("standard_user")
           password_field.send_keys("secret_sauce")
           login_button.click()


           WebDriverWait(self.driver, 20).until(
               EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
           )
       except Exception as e:
           print(f"An error occurred: {str(e)}")


   def logout(self):
       try:
           menu_button = self.driver.find_element(By.ID, "react-burger-menu-btn")
           menu_button.click()


           logout_link = WebDriverWait(self.driver, 20).until(
               EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
           )
           logout_link.click()


           WebDriverWait(self.driver, 20).until(
               EC.visibility_of_element_located((By.ID, "login-button"))
           )
       except Exception as e:
           print(f"An error occurred: {str(e)}")
       finally:
           self.quit()




obj = SauceDemo()
obj.boot()
print("Cookies before login:    ")
for cookie in obj.getCookies():
   print(cookie)


obj.login()


print("Cookies after login:    ")
for cookie in obj.getCookies():
   print(cookie)


obj.logout()


print("Cookies After logout:    ")
for cookie in obj.getCookies():
   print(cookie)
