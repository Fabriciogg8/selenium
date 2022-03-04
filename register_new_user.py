import unittest  
from selenium import webdriver 


class RegisterNewUser(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver_win32/chromedriver.exe")
        driver=self.driver
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get("http://demo-store.seleniumacademy.com/")


    def test_new_user(self):
        driver = self.driver
        # Le colocamos click para que se despliegue
        driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        driver.find_element_by_link_text('Log In').click()

        create_account_button = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
        # Validar que el boton este habilitado con assert
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        # Después de validar hacemos click
        create_account_button.click()

        # Vamos a comparar si el titulo de la pagina es igual
        self.assertEqual('Create New Customer Account', driver.title)

        # Escribiremos en cada uno de los campos de texto
        # Crearemos variables para colocar el selector correspondiente
        first_name = driver.find_element_by_id('firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button/span/span')

        # Verificamos con un assertion que los campos estén habilitados
        self.assertTrue(first_name.is_enabled() and 
                        middle_name.is_enabled() and 
                        last_name.is_enabled() and 
                        email_address.is_enabled() and
                        password.is_enabled() and
                        confirm_password.is_enabled() and
                        submit_button.is_enabled())

        # Enviamos los datos a cada uno de los campos con el metodo send_keys()
        first_name.send_keys('Earth')
        driver.implicitly_wait(1) # Para observar como llena los campos
        middle_name.send_keys('Planet')
        driver.implicitly_wait(1)
        last_name.send_keys('Help')
        driver.implicitly_wait(1)
        email_address.send_keys('earthelp@earthelp.com')
        password.send_keys('123456789')
        confirm_password.send_keys('123456789')
        submit_button.click()


    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()


if __name__=="__main__":       
    unittest.main(verbosity=2)