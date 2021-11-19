# Para poder utilizar Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Para poder parar la ejecución de la prueba durante unos segundos
import time

# Si no estuviera el fichero chromedriver.exe en la carpeta en la que se encuentra este proyecto, 
# debería colocarse la ruta dentro de los paréntesis de la línea inferior
driver = webdriver.Chrome()

try:
    # Abrimos un navegador con la url indicada dentro de los paréntesis de la línea inferior
    driver.get('https://the-internet.herokuapp.com/windows')

    # Maximizamos la ventana del navegador (por si tiene elementos que aparecen y desaparecen 
    # en función del tamaño de la ventana)
    driver.maximize_window()

    # Buscamos el elemento de la página cuyo texto es 'Click Here'
    link_pulsar = driver.find_element(By.CSS_SELECTOR, '#content > div > a')
    # Hacemos click en el elemento anterior
    link_pulsar.click()

    # Ponemos el foco en la segunda ventana que se abre
    driver.switch_to.window(driver.window_handles[1])

    # Comprobamos que el texto que se muestra en la segunda ventana abierta es correcto
    assert driver.find_element(By.CSS_SELECTOR, 'body > div > h3').text == 'New Window'

    # Paramos la ejecución 3 segundos
    time.sleep(3)

    # Cerramos la segunda ventana abierta
    driver.close()

    # Volvemos a poner el foco en la primera ventana que se abrió
    driver.switch_to.window(driver.window_handles[0])

    # Paramos la ejecución 3 segundos
    time.sleep(3)
finally:
    # Cerramos la ventana del navegador
    driver.quit()