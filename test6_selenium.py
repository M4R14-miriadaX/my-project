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
    driver.get('https://the-internet.herokuapp.com/hovers')

    # Maximizamos la ventana del navegador (por si tiene elementos que aparecen y desaparecen 
    # en función del tamaño de la ventana)
    driver.maximize_window()

    # Buscamos el elemento de la página que tiene una imagen y está en el último lugar
    imagen_perfil = driver.find_element(By.CSS_SELECTOR, '#content > div > div:nth-child(5) > img')
    # Nos colocamos encima del elemento anterior
    hover = ActionChains(driver).move_to_element(imagen_perfil)
    hover.perform()

    # Paramos la ejecución 3 segundos
    time.sleep(3)

    # Buscamos el elemento de la página cuyo texto es 'View profile'
    link_ver_perfil = driver.find_element(By.CSS_SELECTOR, '#content > div > div:nth-child(5) > div > a')
    # Hacemos click en el elemento anterior
    link_ver_perfil.click()

    # Paramos la ejecución 3 segundos
    time.sleep(3)

    # Comprobamos que el contenido de la página a la que nos redirige es correcto
    assert driver.find_element(By.CSS_SELECTOR, 'body > h1').text == 'Not Found'
finally:
    # Cerramos la ventana del navegador
    driver.quit()