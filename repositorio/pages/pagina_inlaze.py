from selenium import webdriver
from selenium.webdriver.common.by import By

class PaginaInlaze:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://test-qa.inlaze.com/"
    
    def abrir(self):
        self.driver.get(self.url)
    
    def registrar_usuario(self, nombre, correo, contrasena):
        self.driver.find_element(By.ID, "name").send_keys(nombre)
        self.driver.find_element(By.ID, "email").send_keys(correo)
        self.driver.find_element(By.ID, "password").send_keys(contrasena)
        self.driver.find_element(By.ID, "confirm_password").send_keys(contrasena)
        self.driver.find_element(By.ID, "register_button").click()
    
    def iniciar_sesion(self, correo, contrasena):
        self.driver.find_element(By.ID, "login_email").send_keys(correo)
        self.driver.find_element(By.ID, "login_password").send_keys(contrasena)
        self.driver.find_element(By.ID, "login_button").click()
    
    def cerrar_sesion(self):
        self.driver.find_element(By.ID, "logout_button").click()
