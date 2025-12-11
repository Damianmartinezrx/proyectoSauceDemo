from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.datos import leer_csv_login
import pytest
from pages.inventoryPage import inventory_page  
from pages.cartPage import cart_Page
from utils.logger import logger

from pages.loginPage import login_page as login

@pytest.mark.parametrize("usuario, password, debe_funcionar", leer_csv_login("datos/datos_usuarioValido.csv"))
def test_cart(login_page, usuario, password, debe_funcionar):
    try:
        driver = login_page
        login(driver).login(usuario, password)
        inventory = inventory_page(driver)

        #agregar producto al inventario
        inventory.agregar_item_al_carrito()

        #navegar al carrito de compras
        inventory.abrir_carrito()

        #validar que el producto agregado este en el carrito
        cartPage = cart_Page(driver)

        productos_carrito = cartPage.obtener_items_carrito()
        logger.info("Validando que el carrito contenga un producto")
        assert len(productos_carrito) == 1, "El carrito debe contener un producto."
        

    except Exception as e:
        print(f"Error en test_carrito_compras : {e}")
        raise

    