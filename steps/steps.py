# Para poder utilizar Behave
from behave import *

# Para poder utilizar Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Para poder parar la ejecución de la prueba durante unos segundos
import time

# Para poder poner un valor cambiante en un paso
use_step_matcher("re")

# Pasos para 'demo.feature'
@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False

# Pasos para 'titulo_correcto.feature' (que es la feature asociada a test1_unittest.py)
@given('chrome is up')
def step_impl(context):
    pass

@when('redirect to Python web')
def step_impl(context):
    # Se debe usar context para utilizar la misma ventana durante todo el test
    context.driver.get('https://python.org/')

@then('web title is correct')
def step_impl(context):
    try:
        # Se debe usar context para utilizar la misma ventana durante todo el test
        assert context.driver.title == 'Welcome to Python.org'
    finally:
        pass

# Pasos para 'nuevo_episodio.feature' (que es la feature asociada a test1_selenium.py)
# El bloque de código para 'chrome is up' ya está definido anteriormente
@when('redirect to AnimeFLV web')
def step_impl(context):
    # Se debe usar context para utilizar la misma ventana durante todo el test
    context.driver.get('https://www3.animeflv.net/')

@when('the user clicks One peace link')
def step_impl(context):
    # Se debe usar context para utilizar la misma ventana durante todo el test
    context.driver.maximize_window()
    link_serie = context.driver.find_element(By.CSS_SELECTOR, '#mCSB_1_container > ul > li:nth-child(1) > a')
    link_serie.click()

@then('new episode is not available')
def step_impl(context):
    try:
        # Se debe usar context para utilizar la misma ventana durante todo el test
        link_proximo_episodio = context.driver.find_element(By.CSS_SELECTOR, '#episodeList > li.fa-play-circle.Next > a > h3')
        assert link_proximo_episodio.text == 'PROXIMO EPISODIO'
    finally:
        pass

@then('last episode is (?P<num_ultimo_episodio>.+)')
def step_impl(context, num_ultimo_episodio):
    try:
        # Se debe usar context para utilizar la misma ventana durante todo el test
        link_ultimo_episodio = context.driver.find_element(By.CSS_SELECTOR, '#episodeList > li:nth-child(2) > a > p')
        assert link_ultimo_episodio.text == f'Episodio {num_ultimo_episodio}'
    finally:
        pass

# Pasos para 'inicio_sesion_renfe.feature'
@given('Renfe web is up')
def step_impl(context):
    # Se debe usar context para utilizar la misma ventana durante todo el test
    context.driver.get('https://www.renfe.com/es/es')
    context.driver.maximize_window()
    time.sleep(5)
    cookies = context.driver.find_element(By.ID, 'onetrust-accept-btn-handler')
    while not cookies.is_displayed():
        time.sleep(1)
    cookies.click()

@when('select Madrid as origin')
def step_impl(context):
    # Se debe usar context para utilizar la misma ventana durante todo el test
    origen = context.driver.find_element(By.CSS_SELECTOR, '#origin')
    acciones = ActionChains(context.driver)
    acciones.move_to_element(origen)
    acciones.click(origen)
    acciones.send_keys('Madrid')
    acciones.send_keys(Keys.DOWN)
    acciones.send_keys(Keys.RETURN)
    acciones.perform()

@when('select Barcelona as destination')
def step_impl(context):
    # Se debe usar context para utilizar la misma ventana durante todo el test
    destino = context.driver.find_element(By.CSS_SELECTOR, '#destination')
    acciones = ActionChains(context.driver)
    acciones.move_to_element(destino)
    acciones.click(destino)
    acciones.send_keys('Barcelona')
    acciones.send_keys(Keys.DOWN)
    acciones.send_keys(Keys.RETURN)
    acciones.perform()

@when('select one way')
def step_impl(context):
    # Se debe usar context para utilizar la misma ventana durante todo el test
    tipo_billete_desplegable = context.driver.find_element(By.CSS_SELECTOR, '#tripType > div > button')
    tipo_billete_desplegable.click()
    solo_ida = context.driver.find_element(By.CSS_SELECTOR, '#tripType > div > div > ul > li:nth-child(1) > button')
    solo_ida.click()

@when('select travel date next week')
def step_impl(context):
    # Se debe usar context para utilizar la misma ventana durante todo el test
    dia_desplegable = context.driver.find_element(By.CSS_SELECTOR, '#datepicker > div > input')
    dia_desplegable.click()
    seleccionador_fecha = context.driver.find_element(By.CSS_SELECTOR, '#datepicker > div > div > button:nth-child(2) > i')
    for i in range(1, 8):
        seleccionador_fecha.click()

@when('find tickets')
def step_impl(context):
    # Se debe usar context para utilizar la misma ventana durante todo el test
    buscar_billetes_boton = context.driver.find_element(By.CSS_SELECTOR, '#contentPage > div > div > div:nth-child(1) > div > div > div > div > div > div > rf-header > rf-header-top > div.rf-header__wrap-search.grid > rf-search > div > div.rf-search__filters.rf-search__filters--open > div.rf-search__wrapper-button > div.rf-search__button > form > rf-button > div > button > div.mdc-button__touch')
    buscar_billetes_boton.click()
    
@then('tickets are shown')
def step_impl(context):
    # Se debe usar context para utilizar la misma ventana durante todo el test
    assert (context.driver.find_element(By.CSS_SELECTOR, '#wrapper > section.content.header-user > div:nth-child(1) > section > div:nth-child(1) > ul > li').text == 'ELEGIR TREN')

@when('select one ticket')
def step_impl(context):
    # Se debe usar context para utilizar la misma ventana durante todo el test
    billetes = context.driver.find_elements(By.CSS_SELECTOR, '[class="booking-list-element-price"]')
    time.sleep(5)
    for billete in billetes:
        if billete.is_displayed():
            billete.click()
            break
    seleccionar_billete_boton = context.driver.find_element(By.CSS_SELECTOR, '#buttonBannerContinuar')
    seleccionar_billete_boton.click()
    time.sleep(5)
    entendido_boton = context.driver.find_element(By.CSS_SELECTOR,'#cerrarConfirmacionMaletasAVLO')
    entendido_boton.click()

@then('start session required')
def step_impl(context):
    # Se debe usar context para utilizar la misma ventana durante todo el test
    time.sleep(5)
    assert (context.driver.find_element(By.CSS_SELECTOR, '#modal-login-title').text == 'INICIA SESIÓN PARA PODER REALIZAR TU COMPRA')
