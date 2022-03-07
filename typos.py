import unittest  
from selenium import webdriver 


class Typos(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver_win32/chromedriver.exe")
        driver=self.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_link_text("Typos").click()
        

    def test_account_link(self):
        driver = self.driver
        paragraph_to_check = driver.find_element_by_css_selector("#content > div > p:nth-child(3)")
        # Validaremos el párrafo
        text_to_check = paragraph_to_check.text
        # Lo mostramos en pantalla
        print(text_to_check) 

        # Creamos una variable que nos indique cuantos intentos nos toma
        tries = 1
        # Creamos otra variable para que nos indique cuando encuentra el texto correctamente
        found = False
        # Tenemos que poner en una variable el texto correcto
        correct_text = "Sometimes you'll see a typo, other times you won't."      

        # Mediante un while indicamos que sucede si found es Falso
        while not found:
            # Si el texto es igual debe de cambiar la variable found a True
            if text_to_check == correct_text:
                driver.refresh()
                found = True
            # Mientras sea falso debe de continuar el ciclo
            else: 
                paragraph_to_check = driver.find_element_by_css_selector('#content > div > p:nth-child(3)')
                text_to_check = paragraph_to_check.text
                tries +=1
                driver.refresh()
        
        # Con un assertion colocamos un mensaje si se encuentra el texto
        self.assertEqual(found, True)
        print(f'It tooks {tries} tries to find the typo')

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()


if __name__=="__main__":       
    unittest.main(verbosity=2)