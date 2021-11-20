# Para poder utilizar Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Para poder parar la ejecución de la prueba durante unos segundos
import time

# Si no estuviera el fichero chromedriver.exe en la carpeta en la que se encuentra este proyecto, 
# debería colocarse la ruta dentro de los paréntesis de la línea inferior
driver = webdriver.Chrome()

try:
    # Abrimos un navegador con la url indicada dentro de los paréntesis de la línea inferior
    driver.get('https://the-internet.herokuapp.com/javascript_alerts')

    # Maximizamos la ventana del navegador (por si tiene elementos que aparecen y desaparecen 
    # en función del tamaño de la ventana)
    driver.maximize_window()

    # Buscamos el elemento de la página cuyo texto es 'Click for JS Alert'
    boton_alerta = driver.find_element(By.CSS_SELECTOR, '#content > div > ul > li:nth-child(1) > button')
    # Hacemos click en el elemento anterior
    boton_alerta.click()

    # Pulsar en el botón Aceptar del pop up de aviso
    driver.switch_to.alert.accept()

    # Comprobamos que se ha pulsado en el botón Aceptar del pop up de aviso anterior
    assert driver.find_element(By.CSS_SELECTOR, '#result').text == 'You successfully clicked an alert'

    # Paramos la ejecución 3 segundos
    time.sleep(3)

    # Buscamos el elemento de la página cuyo texto es 'Click for JS Confirm'
    boton_confirmacion = driver.find_element(By.CSS_SELECTOR, '#content > div > ul > li:nth-child(2) > button')
    # Hacemos click en el elemento anterior
    boton_confirmacion.click()

    # Pulsar en el botón Aceptar del pop up de aviso
    driver.switch_to.alert.accept()

    # Comprobamos que se ha pulsado en el botón Aceptar del pop up de aviso anterior
    assert driver.find_element(By.CSS_SELECTOR, '#result').text == 'You clicked: Ok'

    # Paramos la ejecución 3 segundos
    time.sleep(3)

    # Hacemos click en el elemento anterior de nuevo
    boton_confirmacion.click()

    # Pulsar en el botón Cancelar del pop up de aviso
    driver.switch_to.alert.dismiss()

    # Comprobamos que se ha pulsado en el botón Cancelar del pop up de aviso anterior
    assert driver.find_element(By.CSS_SELECTOR, '#result').text == 'You clicked: Cancel'

    # Paramos la ejecución 3 segundos
    time.sleep(3)

    # Buscamos el elemento de la página cuyo texto es 'Click for JS Prompt'
    boton_prompt = driver.find_element(By.CSS_SELECTOR, '#content > div > ul > li:nth-child(3) > button')
    # Hacemos click en el elemento anterior
    boton_prompt.click()

    # Escribir 'Texto' y pulsar en el botón Aceptar del pop up de aviso
    driver.switch_to.alert.send_keys('Texto')
    driver.switch_to.alert.accept()

    # Comprobamos que se ha pulsado en el botón Aceptar del pop up de aviso anterior tras escribir 'Texto'
    assert driver.find_element(By.CSS_SELECTOR, '#result').text == 'You entered: Texto'

    # Paramos la ejecución 3 segundos
    time.sleep(3)

    # Hacemos click en el elemento anterior de nuevo
    boton_prompt.click()

    # Escribir 'Texto' y pulsar en el botón Cancelar del pop up de aviso
    driver.switch_to.alert.send_keys('Texto')
    driver.switch_to.alert.dismiss()

    # Comprobamos que se ha pulsado en el botón Cancelar del pop up de aviso anterior tras escribir 'Texto'
    assert driver.find_element(By.CSS_SELECTOR, '#result').text == 'You entered: null'

    # Paramos la ejecución 3 segundos
    time.sleep(3)
finally:
    # Cerramos la ventana del navegador
    driver.quit()
