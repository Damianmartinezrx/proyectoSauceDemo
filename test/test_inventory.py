from selenium.webdriver.common.by import By
import pytest   
from pages.inventoryPage import inventory_page
from utils.datos import leer_csv_login
from utils.logger import logger
from pages.loginPage import login_page as login


@pytest.mark.parametrize("usuario, password, debe_funcionar", leer_csv_login("datos/datos_usuarioValido.csv"))
def test_login_validation(login_page, usuario, password, debe_funcionar):
    try:
        driver = login_page
        
        login(driver).login(usuario, password)
        inventory = inventory_page(driver)

        #Validacion del titulo de la pagina y la presencia de productos
        logger.info("Validando el titulo de la pagina y la presencia de productos en el inventario")
        assert driver.title == "Swag Labs", "El título de la página no es correcto"
        
        #Validar que hay productos en el inventario
        productos = inventory.obtener_items_inventario()

        #Validar carrito esta vacio
        logger.info("Validando que el carrito de compras esté vacío al iniciar sesión")
        assert inventory.obtener_cantidad_carrito() == 0, "El carrito no está vacío"
        
        #Validar agregar primer producto al carrito
        inventory.agregar_item_al_carrito()
        logger.info("Validando que el carrito de compras tenga un producto después de agregar un ítem")
        assert inventory.obtener_cantidad_carrito() == 1, "El carrito no tiene producto"
        

    except Exception as e:
        print(f"Error en test_login_validation: {e}")
        raise
    finally:
        driver.quit()

