# Para poder utilizar Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Para poder crear test unitarios
import unittest

class TestCaseTemperaturaBarcelona(unittest.TestCase):

    def test_titulo(self):
        # Si no estuviera el fichero chromedriver.exe en la carpeta en la que se encuentra este proyecto, 
        # debería colocarse la ruta dentro de los paréntesis de la línea inferior
        driver = webdriver.Chrome()

        # Abrimos un navegador con la url indicada dentro de los paréntesis de la línea inferior
        driver.get('https://weather.com/es-ES/tiempo/hoy/l/0ce8d487db0a25631ee2017ddbe068bfba0de2b24de23f0b82c95863724f3a86')

        # Buscamos el elemento de la página que tiene la temperatura de la ciudad
        temperatura = driver.find_element(By.CSS_SELECTOR, '#WxuSavedLocations-header-9aea3e61-fbf8-4da4-9e07-f96abf18cdf1 > div > div > div > div.styles--cards--2hNpO.styles--cardCarousel--3xhQl > div > div > div > a.styles--weatherData--5tCnE.Button--default--3zkvy > span')

        # Comprobamos que la temperatura está entre 0 y 100 grados
        self.assertGreaterEqual(int(temperatura.text[0:-1]), 0)
        self.assertLessEqual(int(temperatura.text[0:-1]), 100)

        # Cerramos la ventana del navegador
        driver.quit()


# Para lanzar el test unitario
if __name__ == '__main__':
    unittest.main()