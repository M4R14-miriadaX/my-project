# Para poder utilizar Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Para poder parar la ejecución de la prueba durante unos segundos
import time

def marcar_checks(check1, check2):
    # Si no estuviera el fichero chromedriver.exe en la carpeta en la que se encuentra este proyecto, 
    # debería colocarse la ruta dentro de los paréntesis de la línea inferior
    driver = webdriver.Chrome()

    try:
        # Abrimos un navegador con la url indicada dentro de los paréntesis de la línea inferior
        driver.get('https://the-internet.herokuapp.com')

        # Maximizamos la ventana del navegador (por si tiene elementos que aparecen y desaparecen 
        # en función del tamaño de la ventana)
        driver.maximize_window()

        # Buscamos el elemento de la página cuyo texto es 'Checkboxes'
        link_checkboxes = driver.find_element(By.CSS_SELECTOR, '#content > ul > li:nth-child(6) > a')
        # Hacemos click en el elemento anterior
        link_checkboxes.click()

        # Buscamos los elementos de la página cuyos textos son 'checkbox 1' y 'checkbox 2', respectivamente
        link_checkbox1 = driver.find_element(By.CSS_SELECTOR, '#checkboxes > input[type=checkbox]:nth-child(1)')
        link_checkbox2 = driver.find_element(By.CSS_SELECTOR, '#checkboxes > input[type=checkbox]:nth-child(3)')
        
        # Si queremos que el primer checkbox esté marcado hay que comprobar si no está marcado ya para marcarle
        # Si queremos que el primer checkbox no esté marcado hay que comprobar si estaba marcado ya para desmarcarle
        # Si queremos que el segundo checkbox esté marcado hay que comprobar si no está marcado ya para marcarle
        # Si queremos que el segundo checkbox no esté marcado hay que comprobar si estaba marcado ya para desmarcarle
        if check1 and not link_checkbox1.is_selected():
            # Hacemos click en el primer checkbox para marcarle
            link_checkbox1.click()
        elif not check1 and link_checkbox1.is_selected():
            # Hacemos click en el primer checkbox para desmarcarle
            link_checkbox1.click()
        if check2 and not link_checkbox2.is_selected():
            # Hacemos click en el segundo checkbox para marcarle
            link_checkbox2.click()
            # Paramos la ejecución 3 segundos
            time.sleep(3)
        elif not check2 and link_checkbox2.is_selected():
            # Hacemos click en el segundo checkbox para desmarcarle
            link_checkbox2.click()
            # Paramos la ejecución 3 segundos
            time.sleep(3)
        else:
            # Paramos la ejecución 3 segundos
            time.sleep(3)
    finally:
        # Cerramos la ventana del navegador
        driver.quit()


marcar_checks(True, True)
marcar_checks(True, False)
marcar_checks(False, True)
marcar_checks(False, False)