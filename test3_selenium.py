# Para poder utilizar Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Para poder parar la ejecución de la prueba durante unos segundos
import time


def mostrar_datos(dueMinimo):
    # Si no estuviera el fichero chromedriver.exe en la carpeta en la que se encuentra este proyecto,
    # debería colocarse la ruta dentro de los paréntesis de la línea inferior
    driver = webdriver.Chrome()

    try:
        # Abrimos un navegador con la url indicada dentro de los paréntesis de la línea inferior
        driver.get('https://the-internet.herokuapp.com')

        # Maximizamos la ventana del navegador (por si tiene elementos que aparecen y desaparecen
        # en función del tamaño de la ventana)
        driver.maximize_window()

        # Buscamos el elemento de la página cuyo texto es 'Sortable Data Tables'
        link_dataTables = driver.find_element(By.CSS_SELECTOR, '#content > ul > li:nth-child(41) > a')
        # Hacemos click en el elemento anterior
        link_dataTables.click()

        # Buscamos los elementos de la página que están en la tabla 'Example 1' y que aparecen en la columna 'Due'
        dueValues = [
            driver.find_element(By.CSS_SELECTOR, '#table1 > tbody > tr:nth-child(1) > td:nth-child(4)'),
            driver.find_element(By.CSS_SELECTOR, '#table1 > tbody > tr:nth-child(2) > td:nth-child(4)'),
            driver.find_element(By.CSS_SELECTOR, '#table1 > tbody > tr:nth-child(3) > td:nth-child(4)'),
            driver.find_element(By.CSS_SELECTOR, '#table1 > tbody > tr:nth-child(4) > td:nth-child(4)')
        ]

        # Paramos la ejecución 3 segundos
        time.sleep(3)

        # Mostramos por pantalla sólo los datos de aquellas personas que tienen el campo 'Due' mayor que un cierto valor
        print(f'Datos personas con Due > {dueMinimo}')
        print('----------------------------')
        for i in range(0, 4):
            if float(dueValues[i].text[1:]) > dueMinimo:
                # Buscamos los elementos de la página que están en la tabla 'Example 1' y que tienen el campo 'Due' mayor que un cierto valor
                lastName = driver.find_element(
                    By.CSS_SELECTOR, '#table1 > tbody > tr:nth-child(' + str(i + 1) + ') > td:nth-child(1)')
                firstName = driver.find_element(
                    By.CSS_SELECTOR, '#table1 > tbody > tr:nth-child(' + str(i + 1) + ') > td:nth-child(2)')
                email = driver.find_element(
                    By.CSS_SELECTOR, '#table1 > tbody > tr:nth-child(' + str(i + 1) + ') > td:nth-child(3)')
                webSite = driver.find_element(
                    By.CSS_SELECTOR, '#table1 > tbody > tr:nth-child(' + str(i + 1) + ') > td:nth-child(5)')
                print(
                    f'First Name: {firstName.text} | Last name: {lastName.text} | Email: {email.text} | Due: {dueValues[i].text} | Web site: {webSite.text}')
        print('----------------------------')
    finally:
        # Cerramos la ventana del navegador
        driver.quit()


mostrar_datos(49)
mostrar_datos(50)
mostrar_datos(99)
mostrar_datos(100)