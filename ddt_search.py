import unittest  
from ddt import ddt, data, unpack
from selenium import webdriver 

@ddt
class SearchDDT(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver_win32/chromedriver.exe")
        driver=self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(30)

    # Antes de nuestro metodo de prueba, colocamos un decorador, que incluye tuplas con los terminos a buscar
    @data(('dress',5),('music',5))
    # Decorador unoack para desempaquetar esas tuplas y consultarlas de manera manual
    @unpack
    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys(search_value)  
        search_field.submit()

        products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')  
        print(f'Found {len(products)} products')

        for product in products:
            print(product.text)
        
        self.assertEqual(expected_count, len(products))
   
        
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()


if __name__=="__main__":       
    unittest.main(verbosity=2)