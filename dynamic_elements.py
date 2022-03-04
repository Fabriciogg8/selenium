import unittest  
from selenium import webdriver 
from selenium.webdriver.support.ui import Select 
from time import sleep 

class DymamicElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver_win32/chromedriver.exe")
        driver=self.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_link_text("Disappearing Elements").click()


    def test_name_elements(self):
        driver = self.driver
        # Creamos una lista vacía que contendra las opciones del menu
        options = []
        # Creamos una variable con el valor de la cantidad de opciones
        menu = 5
        # Variable que contara cuantos intentos le tomó a selenium
        tries = 1
        # Indicaremos con un ciclo while que mientras sea menor a 5 se estará repitiendo el ciclo 
        while len(options) < 5:
            # Vamos a limpiar las opciones por si llegamos al valor de 5 sin encontrar el botoón de Gallery
            options.clear()

            for i in range(menu):
                try:
                    option_name = driver.find_element_by_xpath(f'//*[@id="content"]/div/ul/li[{i + 1}]/a')
                    # Agregamos a la lista de opciones, el valor que hayamos encontrado con este valor
                    options.append(option_name.text)
                    print(options)
                # Vamos a incluir la iteración que pueda ocurrir cuando estamos haciendo la iteración de cada
                # uno de nuestros elementos
                except:
                    print(f"Option number {i+1} is NOT FOUND")
                    tries += 1
                    # Como no lo encontró refrescamos el navegador, para que lo siga buscando
                    driver.refresh()
        # En caso de encontrar el botón que aparece en forma aleatoria, lo mostramos en pantalla
        print(f"Finished in {tries} tries")


    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()


if __name__=="__main__":       
    unittest.main(verbosity=2)