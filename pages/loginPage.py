from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class login_page:
    
    url = "https://www.saucedemo.com/"
    _userinput_id = (By.ID, "user-name")
    _passwordinput_id = (By.ID, "password")
    _loginbutton_id = (By.ID, "login-button")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir_pagina(self):
        self.driver.get(self.url)
        return self

    def ingresar_usuario(self, usuario):
        user_input = self.wait.until(EC.visibility_of_element_located(self._userinput_id))
        user_input.clear()
        user_input.send_keys(usuario)
        return self
    
    def ingresar_pass(self, contraseña):
        password_input = self.wait.until(EC.visibility_of_element_located(self._passwordinput_id))
        password_input.clear()
        password_input.send_keys(contraseña)
        return self
    
    def hacer_clic_en_login(self):
        login_button = self.wait.until(EC.element_to_be_clickable(self._loginbutton_id))
        login_button.click()
        return self 
    
    def login(self, usuario, contraseña):
        self.ingresar_usuario(usuario)
        self.ingresar_pass(contraseña)
        self.hacer_clic_en_login()
        return self
    
    def obtener_error(self):
        div_error = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".error-message-container h3")))
        return div_error.text
    
