import unittest  
from selenium import webdriver 
from selenium.webdriver.support.ui import Select 

class LanguageOptions(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver_win32/chromedriver.exe")
        driver=self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.implicitly_wait(30)
        driver.maximize_window()


    def test_select_language(self):
        driver = self.driver
        # Primero seleccionamos el input
        search_field = driver.find_element_by_name('q')
        # Como buena practica limpiamos el texto que haya en las barras de búsqueda
        search_field.clear()

        # En la barra de busqueda debemos colocar el termino que queremos encontrar
        search_field.send_keys('tee')
        search_field.submit()

        # Buscamos el elemento que queremos comparar y le hacemos click
        driver.find_element_by_class_name('link-compare').click()

        # Debemos de hacer click en limpiar la lista para disparar el alert, lo buscamos por el texto del link
        driver.find_element_by_link_text('Clear All').click()

        # Le decimos al driver que haga un cambio de foco al alert
        alert = driver.switch_to.alert
        # Extraemos el texto que nos muesta en una variable
        alert_text = alert.text

        # Verificamos por medio de un assert que el texto que se muestra es igual al que queremos
        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)

        alert.accept()

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()


if __name__=="__main__":       
    unittest.main(verbosity=2)