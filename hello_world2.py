from unittest.runner import TextTestRunner
import unittest  #nos servira para traer todas nuestras pruebas
from pyunitreport import HTMLTestRunner #nos ayudara a orquestar cada una de las pruebas que estemos ejecutando
from selenium import webdriver #para poder comunicarnos con el navegador


class HelloWorld(unittest.TestCase):
    #metodo de test fixture, ejecuta todo lo necesario antes de hacer una prueba
    #prepara el entorno de la prueba misma
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver_win32/chromedriver.exe")
        driver=self.driver #colocamos self.driver en la variable driver para no tener que poner self.driver todas las veces
        driver.implicitly_wait(10) #para que espere 10seg antes de realizar la siguiente accion(las acciones estan en nuestro caso de prueba unitaria)

    #nuestro modulo de prueba o prueba unitaria, debe iniciar con test para que la identifique el test runner
    #vamos a realizar una serie de acciones para que el navegador las automatice
    def test_hello_world(self):
        driver=self.driver
        driver.get('https://www.platzi.com')

    # Visitamos una segunda página web
    def test_visit_wikipedi(self):
        self.driver.get('https://www.wikipedia.org')

    #test fixture que va dar la salida a lo que estemos escribiendo.
    #para finalizar lo que queremos generalmente es cerrar la ventana del navegador, para no generar fugas
    #o que nuestro equipo pueda vovlerse lento
    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":       #genera los reportes correspondientes, nombre de la carpeta, y nombre del archivo
    unittest.main(verbosity=2, testRunner= HTMLTestRunner(output="reportes",report_name="Hello-world-report"))
