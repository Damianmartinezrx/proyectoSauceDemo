from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from pages.loginPage import login_page 
from faker import Faker
from utils.datos import leer_csv_login
from utils.logger import logger

faker = Faker()

# Obtener un usuario y contraseña válidos para las pruebas de login fallidas
correct_user,correct_pass = leer_csv_login("datos/datos_usuarioValido.csv")[0][:2] 

# Parametrización de pruebas para login fallido
@pytest.mark.parametrize("usuario, password, debe_funcionar",
[(faker.user_name(), faker.password(), False),
(faker.user_name(), correct_pass, False),
(correct_user, faker.password(), False), 
("", faker.password(), False),
(faker.user_name(), "", False),
("", "", False)])

def test_login_validation(login_page, usuario, password, debe_funcionar):
    driver = login_page

    
    if debe_funcionar:
        logger.info("Verificando que el login fue exitoso")
        assert "/inventory.html" in driver.current_url, "No se redirgio al inventario"
    elif debe_funcionar:
        mensaje_error = login_page(driver).obtener_error()
        logger.info("Verificando que el mensaje de error se muestra correctamente")
        assert "Epic sadface" in mensaje_error, "el mensaje de error no se esta mostrando"
        print(mensaje_error)