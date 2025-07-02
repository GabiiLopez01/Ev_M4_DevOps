import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Elimina para ver el navegador
    options.add_argument("--no-sandbox")
    
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )
    yield driver
    driver.quit()