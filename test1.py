from selenium import webdriver
from selenium.webdriver.common.by import By
import win32api
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www3.animeflv.net/")
    driver.maximize_window()
    link_serie = driver.find_element(By.CSS_SELECTOR, '#mCSB_1_container > ul > li:nth-child(1) > a')
    link_serie.click()
    link_episodio = driver.find_element(By.CSS_SELECTOR, '#episodeList > li.fa-play-circle.Next > a > h3')
    if link_episodio.text == 'PROXIMO EPISODIO':
        win32api.MessageBox(0, 'No hay nuevo episodio', 'Alerta')
finally:
    driver.quit()