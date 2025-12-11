from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

from utils.datos import leer_csv_login
from pages.loginPage import login_page 

from utils.logger import logger
from pages.loginPage import login_page as login

@pytest.mark.parametrize("usuario, password, debe_funcionar", leer_csv_login("datos/datos_usuarioValido.csv"))
def test_login_validation(login_page, usuario, password, debe_funcionar):
    logger.info("completando con los datos de usario")
    driver = login_page
    login(driver).login(usuario, password)
    
    if debe_funcionar:
        logger.info("Verificando que el login fue exitoso")
        assert "/inventory.html" in driver.current_url, "No se redirgio al inventario"
        logger.info("El login fue exitoso") 
    elif debe_funcionar:
        logger.info("Verificando que el mensaje de error se muestra correctamente")
        mensaje_error = login_page(driver).obtener_error()
        assert "Epic sadface" in mensaje_error, "el mensaje de error no se esta mostrando"
        print(mensaje_error)