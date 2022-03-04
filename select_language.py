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
        exposed_options = ['English', 'French', 'German']
        # Lista vacia para almacenas las opciones que elijamos cuando las estemos revisando
        active_options = []

        # Variable para seleccionar las opciones
        select_language = Select(self.driver.find_element_by_id('select-language'))

        # Validaremos que el dropdown tenga 3 opciones
        self.assertEqual(3, len(select_language.options))

        # Vamos a iterar por cada una de las opciones
        for option in select_language.options:
            # Las agregaremos a nuestra lista vacia, agregaremos solo el texto
            active_options.append(option.text)

        # Vamos a verificar que la lista de las opciones expuestas y activas sean identicas
        self.assertListEqual(exposed_options, active_options)

        # Seleccionaremos un idioma por defecto de los que estan disponibles
        self.assertEqual('English', select_language.first_selected_option.text)

        # Indicaremos a Selenium que seleccione el idioma aleman
        select_language.select_by_visible_text('German')

        # Verificamos que se haya seleccionado el aleman, para esto lo comparamos con el titulo del sitio 
        self.assertTrue('store=german' in self.driver.current_url)

        # Otra opcion para elegir un idioma es a través del indice
        select_language = Select(self.driver.find_element_by_id('select-language'))
        select_language.select_by_index(0) # Volverá al ingles ya que es el valor cero de la lista


    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()


if __name__=="__main__":       
    unittest.main(verbosity=2)