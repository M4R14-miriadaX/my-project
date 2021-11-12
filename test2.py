from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def marcar_checks(check1, check2):
    driver = webdriver.Chrome()

    try:
        driver.get("https://the-internet.herokuapp.com")
        driver.maximize_window()
        link_checkboxes = driver.find_element(By.CSS_SELECTOR, '#content > ul > li:nth-child(6) > a')
        link_checkboxes.click()
        link_checkbox1 = driver.find_element(By.CSS_SELECTOR, '#checkboxes > input[type=checkbox]:nth-child(1)')
        link_checkbox2 = driver.find_element(By.CSS_SELECTOR, '#checkboxes > input[type=checkbox]:nth-child(3)')
        if check1 and not link_checkbox1.is_selected():
            link_checkbox1.click()
            time.sleep(3)
        elif not check1 and link_checkbox1.is_selected():
            link_checkbox1.click()
            time.sleep(3)
        if check2 and not link_checkbox2.is_selected():
            link_checkbox2.click()
            time.sleep(3)
        elif not check2 and link_checkbox2.is_selected():
            link_checkbox2.click()
            time.sleep(3)
        time.sleep(3)
    finally:
        driver.quit()


marcar_checks(True, True)
marcar_checks(True, False)
marcar_checks(False, True)
marcar_checks(False, False)