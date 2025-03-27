import unittest
from selenium import webdriver
from pages.pagina_inlaze import PaginaInlaze

class PruebasInlaze(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.pagina = PaginaInlaze(self.driver)
        self.pagina.abrir()
    
    def test_registrar_usuario_valido(self):
        self.pagina.registrar_usuario("Juan Perez", "juan.perez@example.com", "Contrasena123!")
    
    def test_iniciar_sesion_usuario_valido(self):
        self.pagina.iniciar_sesion("juan.perez@example.com", "Contrasena123!")
    
    def test_cerrar_sesion(self):
        self.pagina.iniciar_sesion("juan.perez@example.com", "Contrasena123!")
        self.pagina.cerrar_sesion()
    
    def tearDown(self):
        self.driver.quit()
