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

@pytest.mark.parametrize("usuario, password, debe_funcionar", leer_csv_login("datos/datos_usuarioValido.csv"))
def test_checkout(login_page, usuario, password, debe_funcionar):
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
        checkout.completar_checkout("Damian","Martinez","B1744")
        checkout.boton_continue()
        checkout.boton_finish()
        
        logger.info("Test de checkout completado exitosamente.")
        texto = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))).text
        assert texto == "Thank you for your order!", "El mensaje de confirmacion no es correcto."
        


        

    except Exception as e:
        print(f"Error en test_checkout : {e}")
        raise