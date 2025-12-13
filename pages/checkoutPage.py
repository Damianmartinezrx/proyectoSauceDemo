from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC    
from selenium import webdriver
import pytest

class checkout_page:

    _FIRT_NAME = (By.ID,"first-name")
    _LAST_NAME = (By.ID,"last-name")
    _POSTAL = (By.ID,"postal-code")

    _NOMBRE = "Damian"
    _APELLIDO = "Martinez"
    _POSTAL = "B1744"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def ingresar_nombre(self,_NOMBRE):
        nombre = self.wait.until(EC.visibility_of_element_located(self._FIRT_NAME))
        nombre.clear()
        nombre.send_keys(_NOMBRE)
        return self
    
    def ingresar_apellido(self,_APELLIDO):
        apellido = self.wait.until(EC.visibility_of_element_located(self._LAST_NAME))
        apellido.clear()
        apellido.send_keys(_APELLIDO)
        return self
    
    def ingresar_postal(self,_POSTAL):
        postal = self.wait.until(EC.visibility_of_element_located(self._POSTAL))
        postal.clear()
        postal.send_keys(_POSTAL)
        return self

    
    def completar_checkout(self,_NOMBRE,_APELLIDO,_POSTAL):
        self.ingresar_nombre(_NOMBRE)
        self.ingresar_apellido(_APELLIDO)
        self.ingresar_postal(_POSTAL)
        return self
    

    