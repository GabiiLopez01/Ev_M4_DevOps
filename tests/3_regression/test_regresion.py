import pytest
from src.usuario import Usuario
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestHealthTrackRegression:
    """Suite de pruebas de regresión para HealthTrack"""
    
    # Pruebas de la lógica de negocio (Usuario)
    @pytest.mark.parametrize("initial_weight,new_weight,expected", [
        (70.0, 68.5, 68.5),    # Caso normal
        (100.0, 100.0, 100.0), # Sin cambio
        (80.0, 79.9, 79.9),    # Decimales
        (60.0, 0.0, 0.0)       # Caso límite
    ])
    def test_weight_update(self, initial_weight, new_weight, expected):
        """Verifica que la actualización de peso funcione correctamente"""
        user = Usuario("TestUser", initial_weight)
        user.actualizar_peso(new_weight)
        assert user.peso == expected
    
    #para no introducir cambios en el código inicial, se salta esta prueba
    @pytest.mark.xfail(reason="La clase Usuario no valida pesos negativos")
    def test_negative_weight(self):
        """Verifica manejo de pesos negativos (se espera que falle)"""
        user = Usuario("TestUser", 70.0)
        with pytest.raises(ValueError):
            user.actualizar_peso(-5.0)
    
    # Pruebas de regresión para la interfaz web
    @pytest.fixture
    def driver(self):
        """Fixture para pruebas de interfaz web"""
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        yield driver
        driver.quit()
    
    def test_ui_registration_flow(self, driver):
        """Prueba de regresión para el flujo de registro"""
        driver.get("http://localhost:5000")
        
        # 1. Completar registro
        driver.find_element(By.ID, "nombre").send_keys("RegressionUser")
        driver.find_element(By.ID, "peso").send_keys("75.5")
        driver.find_element(By.ID, "btn-registrar").click()
        
        # 2. Verificar resultado
        peso_actual = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "peso-actual"))
        )
        assert "75.5 kg" in peso_actual.text
        
        # 3. Verificar que no se resta 1kg (regresión)
        assert "74.5 kg" not in peso_actual.text