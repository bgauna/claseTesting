from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
import os
from datetime import datetime

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--incognito')
    driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_login(driver):
    driver.get("https://www.saucedemo.com")
    WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located((By.ID, "user-name")))

    #Localizo Elementos
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    #Interaccion con elementos
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()

    #Espera explicita
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    #Validacion
    assert "inventory" in driver.current_url
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"
    assert driver.find_element(By.CLASS_NAME, "inventory_item").is_displayed()
    assert len(driver.find_elements(By.CLASS_NAME, "inventory_item")) == 6
    assert driver.find_element(By.CLASS_NAME, "shopping_cart_link").is_displayed()
    assert driver.find_element(By.ID, "react-burger-menu-btn").is_displayed()
    assert driver.find_element(By.CLASS_NAME, "footer_copy").is_displayed()
    assert "Sauce Labs" in driver.find_element(By.CLASS_NAME, "footer_copy").text
    assert driver.find_element(By.CLASS_NAME, "app_logo").is_displayed()
    assert driver.find_element(By.CLASS_NAME, "app_logo").text == "Swag Labs"
    assert driver.find_element(By.CLASS_NAME, "bm-burger-button").is_displayed()
    assert driver.find_element(By.CLASS_NAME, "bm-burger-button").is_enabled()


    time.sleep(10)


def test_login_error(driver):
    driver.get("https://www.saucedemo.com")
    WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located((By.ID, "user-name")))

    #Localizo Elementos
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    #Interaccion con elementos
    username.send_keys("standard_user")
    password.send_keys("wrong_password")
    login_button.click()

    #Espera explicita
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))
    )

    #Validacion
    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']")
    assert error_message.is_displayed()
    assert error_message.text == "Epic sadface: Username and password do not match any user in this service"
    
    time.sleep(5)

def test_capture_screenshot(driver):
    driver.get("https://www.saucedemo.com")
    WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located((By.ID, "user-name")))

    #Localizo Elementos
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    #Interaccion con elementos
    username.send_keys("standard_user")
    password.send_keys("wrong_password")
    login_button.click()

    #Espera explicita
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))
    )

    #Validacion
    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']")
    assert error_message.is_displayed()
    assert error_message.text == "Epic sadface: Username and password do not match any user in this service"

    #Captura de pantalla
    driver.save_screenshot("screenshot_error_login.png")
    
    time.sleep(5)

def test_capture_screenshot_success(driver):
    driver.get("https://www.saucedemo.com")
    WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located((By.ID, "user-name")))

    #Localizo Elementos
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    #Interaccion con elementos
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()

    #Espera explicita
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    #Validacion
    assert "inventory" in driver.current_url
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"

    #Captura de pantalla
    driver.save_screenshot("screenshot_success_login.png")
    
    time.sleep(5)

def test_con_try(driver):
    try:
        driver.get("https://www.saucedemo.com")
        WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located((By.ID, "usr-name")))

        #Localizo Elementos
        username = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        #Interaccion con elementos
        username.send_keys("standard_user")
        password.send_keys("wrong_password")
        login_button.click()

        #Espera explicita
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))
        )

        #Validacion
        error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']")
        assert error_message.is_displayed()
        assert error_message.text == "Epic sadface: Username and password do not match any user in this service"
    except Exception as e:
        print(f"An error occurred: {e}")
        carpeta="screenshots"
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
        ruta_archivo=f"{carpeta}/screenshot_exception_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png"
        driver.save_screenshot(ruta_archivo)
        raise
    finally:
        time.sleep(5)

def test_login_logout(driver):
    driver.get("https://www.saucedemo.com")
    WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located((By.ID, "user-name")))

    #Localizo Elementos
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    #Interaccion con elementos
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()

    #Espera explicita
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    #Validacion
    assert "inventory" in driver.current_url
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"

    #Abrir menu
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    menu_button.click()
    time.sleep(2)
    #Esperar que el menu se abra
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "logout_sidebar_link"))
    )

    #Hacer click en logout
    logout_link = driver.find_element(By.ID, "logout_sidebar_link")
    logout_link.click()

    #Esperar que regrese a la pagina de login
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "login-button"))
    )

    #Validar que estamos en la pagina de login
    assert driver.find_element(By.ID, "login-button").is_displayed()
    
    time.sleep(5)


def test_demoqa_alert(driver):
    driver.get("https://demoqa.com/alerts")
    WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located((By.ID, "alertButton")))

    #Localizo Elementos
    alert_button = driver.find_element(By.ID, "alertButton")
    timer_alert_button = driver.find_element(By.ID, "timerAlertButton")
    confirm_button = driver.find_element(By.ID, "confirmButton")
    prompt_button = driver.find_element(By.ID, "promtButton")

    #Interaccion con elementos
    driver.execute_script("arguments[0].scrollIntoView();", alert_button)
    alert_button.click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert alert.text == "You clicked a button"
    alert.accept()
    time.sleep(5)

    driver.execute_script("arguments[0].scrollIntoView();", timer_alert_button)
    timer_alert_button.click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert alert.text == "This alert appeared after 5 seconds"
    alert.accept()
    time.sleep(5)

    driver.execute_script("arguments[0].scrollIntoView();", confirm_button)
    confirm_button.click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert alert.text == "Do you confirm action?"
    alert.dismiss()
    assert driver.find_element(By.ID, "confirmResult").text == "You selected Cancel"
    time.sleep(5)

    driver.execute_script("arguments[0].scrollIntoView();", confirm_button)
    confirm_button.click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert alert.text == "Do you confirm action?"
    alert.accept()
    assert driver.find_element(By.ID, "confirmResult").text == "You selected Ok"
    time.sleep(5)

    driver.execute_script("arguments[0].scrollIntoView();", prompt_button)
    prompt_button.click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert alert.text == "Please enter your name"
    alert.send_keys("John Doe")
    alert.accept()
    assert driver.find_element(By.ID, "promptResult").text == "You entered John Doe"
    
    time.sleep(5)