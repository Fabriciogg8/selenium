import unittest  
from selenium import webdriver 
from selenium.webdriver.support.ui import Select 
from time import sleep 

class NavigationTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver_win32/chromedriver.exe")
        driver=self.driver
        driver.get("https://google.com/")
        driver.implicitly_wait(30)
        driver.maximize_window()


    def test_browser_navigation(self):
       driver = self.driver

       search_field = driver.find_element_by_name('q')
       search_field.clear()

       # Buscamos la palabra que queremos
       search_field.send_keys('platzi')
       search_field.submit()

       driver.back()
       sleep(4) # Agregamos esperas, no es recomendable
       driver.forward()
       sleep(6)
       driver.refresh()
       sleep(2) 

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()


if __name__=="__main__":       
    unittest.main(verbosity=2)