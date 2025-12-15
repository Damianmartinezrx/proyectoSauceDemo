from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.datos import leer_csv_login
import pytest
from pages.inventoryPage import inventory_page  
from pages.cartPage import cart_Page
from utils.logger import logger
from pages.checkoutPage import checkout_page
import time

from pages.loginPage import login_page as login

@pytest.mark.parametrize("nombre, apellido, codigo_postal",
    [
    ("", "Martinez", "B1744"), 
    ("Damian","","B1744"),
    ("Damian","Martinez",""),
    ])

@pytest.mark.parametrize("usuario, password, debe_funcionar", leer_csv_login("datos/datos_usuarioValido.csv"))
def test_checkout(login_page, usuario, password,nombre, apellido, codigo_postal, debe_funcionar):
    try:
        driver = login_page
        login(driver).login(usuario, password)
        inventory = inventory_page(driver)

        #agregar producto al inventario
        inventory.agregar_item_al_carrito()

        #navegar al carrito de compras
        inventory.abrir_carrito()

        inventory = cart_Page(driver)
        inventory.boton_checkout()

        logger.info("Test de pagina checkout")
        checkout = checkout_page(driver)    
        checkout.completar_checkout(nombre,apellido,codigo_postal)
        checkout.boton_continue()
        
        
        logger.info("Test de checkout campos vacios.")
        texto = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"h3"))).text
        assert texto == "Error: First Name is required" or texto == "Error: Last Name is required" or texto == "Error: Postal Code is required", "El mensaje de error no es correcto."
    
        
        
    except Exception as e:
        print(f"Error en test_checkout invalidos: {e}")
        raise