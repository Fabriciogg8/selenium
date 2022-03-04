import unittest  
from selenium import webdriver 
# By nos ayuda hacer referencia a un elemento del sitio web a través de sus selectores
from selenium.webdriver.common.by import By
# Nos ayudara hacer uso de las expected conditions junto con las esperas explcitas
from selenium.webdriver.support.ui import WebDriverWait
# Atado al anterior debemos importar las esperas explicitas. Le colocamos EC para reducir el nombre al usarlas
from selenium.webdriver.support import expected_conditions as EC


class DynamicControls(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver_win32/chromedriver.exe")
        driver=self.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_link_text("Dynamic Controls").click()
        

    def test_account_link(self):
        driver = self.driver

        checkbox = driver.find_element_by_css_selector("#checkbox")
        checkbox.click()

        remove_add_button = driver.find_element_by_css_selector("#checkbox-example > button")
        remove_add_button.click()

        # Al hacer click debemos de esperar para volver hacer click()
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox-example > button'))
            )
        remove_add_button.click()

        enable_disable_button = driver.find_element_by_css_selector("#input-example > button")
        enable_disable_button.click()

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example > button"))
            )

        text_area = driver.find_element_by_css_selector("#input-example > input[type=text]")
        text_area.send_keys('Platzi')

        enable_disable_button.click()

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()


if __name__=="__main__":       
    unittest.main(verbosity=2)