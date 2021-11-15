# Para poder utilizar Behave
from behave import *

# Para poder utilizar Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

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