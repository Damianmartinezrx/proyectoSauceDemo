from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC    
from selenium import webdriver
import pytest

class cart_Page:

    _CART_ITEMS = (By.CLASS_NAME, "cart_item")
    _CART_ITEMS_NAME = (By.CLASS_NAME, "inventory_item_name")
    

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_items_carrito(self):
        productos = self.wait.until(EC.visibility_of_all_elements_located(self._CART_ITEMS))
        return productos

    def obtener_nombres_items_carrito(self):
        nombre_producto = self.wait.until(EC.visibility_of_element_located(self._CART_ITEMS_NAME))
        return nombre_producto.text