from unittest.runner import TextTestRunner
import unittest  
from pyunitreport import HTMLTestRunner 
from selenium import webdriver 


class HelloWorld(unittest.TestCase):
    
    @classmethod # Para que corran las pruebas en una sola ventana 
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="./chromedriver_win32/chromedriver.exe")
        driver=cls.driver 
        driver.implicitly_wait(10) 

    def test_hello_world(self):
        driver=self.driver
        driver.get('https://www.platzi.com')

    def test_visit_wikipedi(self):
        self.driver.get('https://www.wikipedia.org')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__=="__main__":       
    unittest.main(verbosity=2, testRunner= HTMLTestRunner(output="reportes",report_name="Hello-world-report3"))
