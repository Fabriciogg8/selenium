import unittest  
from selenium import webdriver 


class Tables(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver_win32/chromedriver.exe")
        driver=self.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_link_text("Sortable Data Tables").click()
        

    def test_account_link(self):
        driver = self.driver

        # Creamos una lista vacía que es donde vamos almacenar los datos
        # Esta lista estara compuesta por otras sublistas, utilizamos comprehension lists
        table_data = [[] for i in range(5)] # Se usó 5 porque es la cantidad de elementos de la tabla
        print(table_data)

        # Debemos de iterar por cada uno de lo headers y cada uno de los datos
        for i in range(5):
            header = driver.find_element_by_xpath(f'//*[@id="table1"]/thead/tr/th[{i + 1}]/span')
            table_data[i].append(header.text)
             
            # Se usó 4 porque es la cantidad filas
            for j in range(4):
                row_data = driver.find_element_by_xpath(f'//*[@id="table1"]/tbody/tr[{j + 1}]/td[{i + 1}]')
                table_data[i].append(row_data.text)
        
        print(table_data)
        
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()


if __name__=="__main__":       
    unittest.main(verbosity=2)