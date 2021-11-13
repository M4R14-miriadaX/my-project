# Para poder utilizar Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Para poder crear una ventana de alerta
import win32api

# Si no estuviera el fichero chromedriver.exe en la carpeta en la que se encuentra este proyecto, 
# debería colocarse la ruta dentro de los paréntesis de la línea inferior
driver = webdriver.Chrome()

try:
    # Abrimos un navegador con la url indicada dentro de los paréntesis de la línea inferior
    driver.get('https://www3.animeflv.net/')

    # Maximizamos la ventana del navegador (por si tiene elementos que aparecen y desaparecen 
    # en función del tamaño de la ventana)
    driver.maximize_window()

    # Buscamos el elemento de la página cuyo texto es 'One Piece'
    link_serie = driver.find_element(By.CSS_SELECTOR, '#mCSB_1_container > ul > li:nth-child(1) > a')
    # Hacemos click en el elemento anterior
    link_serie.click()

    # Buscamos el elemento de la página cuyo texto es 'PROXIMO EPISODIO'
    link_episodio = driver.find_element(By.CSS_SELECTOR, '#episodeList > li.fa-play-circle.Next > a > h3')
    # Si exite el elemento anterior, creamos una ventana de alerta indicando que aún hay que esperar para
    # el nuevo episodio
    if link_episodio.text == 'PROXIMO EPISODIO':
        win32api.MessageBox(0, 'Aún hay que esperar para el nuevo episodio', 'Alerta')
finally:
    # Cerramos la ventana del navegador
    driver.quit()