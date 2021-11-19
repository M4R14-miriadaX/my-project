# Para poder utilizar Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Si no estuviera el fichero chromedriver.exe en la carpeta en la que se encuentra este proyecto, 
# debería colocarse la ruta dentro de los paréntesis de la línea inferior
driver = webdriver.Chrome()

try:
    # Abrimos un navegador con la url indicada dentro de los paréntesis de la línea inferior
    driver.get('https://the-internet.herokuapp.com/add_remove_elements/')

    # Maximizamos la ventana del navegador (por si tiene elementos que aparecen y desaparecen 
    # en función del tamaño de la ventana)
    driver.maximize_window()

    # Buscamos el elemento de la página cuyo texto es 'Add Element'
    boton_add_element = driver.find_element(By.CSS_SELECTOR, '#content > div > button')
    # Hacemos click en el elemento anterior 10 veces
    for i in range(0, 10):
        boton_add_element.click()

    # Vamos borrando uno a uno los elementos desde el último al primero
    for j in range(10, 0, -1):
        # Buscamos el elemento de la página cuyo texto es 'Delete' (en realidad son 10)
        boton_delete = driver.find_element(By.CSS_SELECTOR, '#elements > button:nth-child(' + str(j) + ')')
        # Hacemos click en el elemento anterior
        boton_delete.click()
finally:
    # Cerramos la ventana del navegador
    driver.quit()