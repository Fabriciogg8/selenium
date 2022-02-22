import unittest  
from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By 


class SearchTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver_win32/chromedriver.exe")
        driver=self.driver
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get("http://demo-store.seleniumacademy.com/")

    
    def tearDown(self):
        self.driver.quit()

    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        # clear es un metodo que va a limpiar el campo de busqueda en caso de que haya algun texto
        search_field.clear()
        search_field.send_keys('tee')
        search_field.submit()

    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.send_keys('salt shaker')
        search_field.submit()

        products = driver.find_elements_by_xpath('//*[@id="product-collection-image-389"]')
        # Haremos un assert para verificar que la cantidad de productos es 1
        self.assertEqual(1, len(products))

if __name__=="__main__":       
    unittest.main(verbosity=2)