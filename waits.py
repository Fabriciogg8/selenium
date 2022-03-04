import unittest  
from selenium import webdriver 
# By nos ayuda hacer referencia a un elemento del sitio web a través de sus selectores
from selenium.webdriver.common.by import By
# Nos ayudara hacer uso de las expected conditions junto con las esperas explcitas
from selenium.webdriver.support.ui import WebDriverWait
# Atado al anterior debemos importar las esperas explicitas. Le colocamos EC para reducir el nombre al usarlas
from selenium.webdriver.support import expected_conditions as EC


class ExplicitWaitTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver_win32/chromedriver.exe")
        driver=self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        

    def test_account_link(self):
        WebDriverWait(self.driver, 10).until(lambda s:s.find_element_by_id('select-language').get_attribute('length') == '3')

        # Haremos una refrencia al enlace donde están las cuentas
        # Esperara maximo 10 seg hasta que se cumpla la condicion esperada, el cual será la visibilidad del elemento que se está ubicando
        account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))
        account.click()

    def test_crate_new_customer(self):
        self.driver.find_element_by_link_text('ACCOUNT').click()

        # Le diremos que espere hasta que un elemento este visible
        my_account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Account')))
        my_account.click()

        create_account_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT')))
        create_account_button.click()

        WebDriverWait(self.driver, 10).until(EC.title_contains('Create New Customer Account'))

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()


if __name__=="__main__":       
    unittest.main(verbosity=2)