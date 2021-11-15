# Para poder utilizar Selenium
from selenium import webdriver

# Para poder crear test unitarios
import unittest

class TestCaseTituloWeb(unittest.TestCase):

    def test_titulo(self):
        # Si no estuviera el fichero chromedriver.exe en la carpeta en la que se encuentra este proyecto, 
        # debería colocarse la ruta dentro de los paréntesis de la línea inferior
        driver = webdriver.Chrome()

        # Abrimos un navegador con la url indicada dentro de los paréntesis de la línea inferior
        driver.get('https://python.org/')

        # Comprobamos que el título de la web es el indicado 'Welcome to Python.org'
        self.assertEqual(driver.title, 'Welcome to Python.org')

        # Cerramos la ventana del navegador
        driver.quit()


# Para lanzar el test unitario
if __name__ == '__main__':
    unittest.main()