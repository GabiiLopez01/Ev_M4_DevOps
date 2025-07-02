import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # Nueva sintaxis para headless
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)  # Espera implícita global
    yield driver
    driver.quit()

def test_complete_user_flow(driver):
    # 1. Navegar a la aplicación
    driver.get("http://localhost:5000")
    
    # 2. Verificar que la página cargó correctamente
    assert "HealthTrack" in driver.title
    
    # 3. Registrar nuevo usuario
    nombre_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "nombre"))
    )
    nombre_input.send_keys("TestUser")
    
    peso_input = driver.find_element(By.ID, "peso")
    peso_input.send_keys("70")
    
    registrar_btn = driver.find_element(By.ID, "btn-registrar")
    registrar_btn.click()
    
    # 4. Verificar registro exitoso
    peso_actual = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "peso-actual"))
    )
    assert "70 kg" in peso_actual.text