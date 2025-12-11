from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.datos import leer_csv_login
import pytest
from pages.inventoryPage import inventory_page  
from pages.cartPage import cart_Page
from utils.lector_json import leer_json
from utils.logger import logger
from pages.loginPage import login_page as login

ruta_json_productos = "datos/productos.json"


@pytest.mark.parametrize("usuario, password, debe_funcionar", leer_csv_login("datos/datos_usuarioValido.csv"))
@pytest.mark.parametrize("nombre_producto", leer_json(ruta_json_productos))

def test_cart_json(login_page, usuario, password, debe_funcionar,nombre_producto):
    try:
        driver = login_page
        
        login(driver).login(usuario, password)

        inventory = inventory_page(driver)

        #agregar producto al inventario
        inventory.agregar_producto_nombre(nombre_producto)

        #navegar al carrito de compras
        inventory.abrir_carrito()

        #validar que el producto agregado este en el carrito
        cartPage = cart_Page(driver)
        logger.info(f"Validando que el producto {nombre_producto} este en el carrito de compras")
        assert cartPage.obtener_nombres_items_carrito() == nombre_producto, f"El producto {nombre_producto} no se encuentra en el carrito."

        
    except Exception as e:
        print(f"Error en test_carrito_compras : {e}")
        raise

    finally:
        driver.quit()