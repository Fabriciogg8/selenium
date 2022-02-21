import unittest  
from selenium import webdriver 


class HomePageTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver_win32/chromedriver.exe")
        driver=self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        #Maximizamos la ventana, porque puede haber elementos responsive que cambien la ubicación segun
        #el tamano de la venatana
        driver.maximize_window()
        #Anadimos una pausa, el número está en segundos
        driver.implicitly_wait(15)


    def test_search_test_field(self):
        ''' Finding an element by its id'''
        search_field = self.driver.find_element_by_id("search")


    def test_search_test_field_by_name(self):
        ''' Finding an element by its name'''
        search_field_by_name = self.driver.find_element_by_name("q")


    def test_search_test_field_by_class_name(self):
        ''' Finding an element by its class name'''
        search_field_by_class_name = self.driver.find_element_by_class_name("input-text")    


    def test_search_button_enabled(self):
        ''' Checking the disponibility of a button '''
        button = self.driver.find_element_by_class_name("button")


    # Queremos identificar una lista de imagenes, las cuales no tenemos mucha información para obtenerlas (no hay id, ni clase, etc.)
    def test_count_of_promo_banner_images(self):
        # Vamos a buscar por la clase del <ul> donde están los <li> que contienen las <img>
        banner_list = self.driver.find_element_by_class_name("promos")
        banners = banner_list.find_elements_by_tag_name("img")
        # Con un assertion vamos a comprobar que la cantidad de imagenes sea 3
        self.assertEqual(3, len(banners))


    # Buscar por el xpath
    def test_vip_promo(self):
        ''' Finding an element by xpath'''
        vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')


    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":       
    unittest.main(verbosity=2)