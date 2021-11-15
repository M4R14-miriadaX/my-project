# Para poder utilizar Selenium
from selenium import webdriver

# Este bloque de código se ejecuta antes de cada escenario de prueba
def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()

# Este bloque de código se ejecuta después de cada escenario de prueba
def after_scenario(context, scenario):
    context.driver.quit()