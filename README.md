# Proyecto de Automatización con Selenium y Python en Visual Studio Code

Este repositorio contiene la automatización de pruebas utilizando **Selenium**, **Python** y el patrón de diseño **Page Object Model (POM)** en **Visual Studio Code**.

---

## 📂 Estructura del Proyecto

```
repositorio_pom/
│   .gitignore           # Archivos a ignorar en Git
│   README.md           # Documentación del proyecto
│   requirements.txt    # Dependencias del proyecto
│
├── pages/              # Clases que representan las páginas web
│   │   __init__.py
│   │   pagina_inlaze.py
│
├── tests/              # Casos de prueba automatizados
│   │   __init__.py
│   │   test_inlaze.py
│
└── drivers/            # (Opcional) WebDrivers necesarios
```

---

## 📌 Requisitos Previos

Antes de ejecutar las pruebas, asegúrate de tener instalado:

1. **Python 3.x**: Descárgalo e instálalo desde [python.org](https://www.python.org/).
2. **Google Chrome**: Necesario para la ejecución de pruebas en este navegador.
3. **ChromeDriver**: Debe coincidir con la versión de tu Google Chrome.
   - Descarga la versión correspondiente desde: [ChromeDriver](https://sites.google.com/chromium.org/driver/)
   - Agrega el `chromedriver.exe` al **PATH** del sistema o colócalo en la carpeta `drivers/` del proyecto.
4. **Visual Studio Code**: Editor recomendado para trabajar con este repositorio.
   - Descárgalo desde [VS Code](https://code.visualstudio.com/).

### 🔹 Instalación de Dependencias

Una vez clonado el repositorio, abre una terminal en la carpeta del proyecto y ejecuta:

```
pip install -r requirements.txt
```

Esto instalará las siguientes dependencias:

```
selenium
unittest
webdriver-manager
```

- **`selenium`**: Para interactuar con el navegador.
- **`unittest`**: Framework de pruebas de Python.
- **`webdriver-manager`**: Administra automáticamente los WebDrivers (opcional).

---

## 🚀 Cómo Ejecutar el Proyecto

### 🔹 Paso 1: Abrir el Repositorio en Visual Studio Code
1. Abre **Visual Studio Code**.
2. En la barra superior, selecciona **File > Open Folder...** y elige la carpeta del repositorio.

### 🔹 Paso 2: Ejecutar las Pruebas

#### Opción 1: Desde la Terminal
1. Abre una terminal en VS Code (**View > Terminal** o `Ctrl + ñ`).
2. Ejecuta el siguiente comando:
   ```
   python -m unittest discover tests
   ```

#### Opción 2: Ejecutando un Archivo Específico
Para correr un test en específico, usa:
```
python -m unittest tests.test_inlaze

#### Opción 3: Ejecutando un Archivo Específico
Tambien se puede usar este codigo
```
pytest tests/
---

## 📜 Explicación del Código

### `pagina_inlaze.py`
Este archivo contiene la clase `PaginaInlaze`, que representa la página de prueba. Implementa métodos como:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

class PaginaInlaze:
    def __init__(self, driver):
        self.driver = driver  # Inicializa el driver de Selenium
        self.url = "https://test-qa.inlaze.com/"  # URL de la página a probar
    
    def abrir(self):
        self.driver.get(self.url)  # Abre la página en el navegador
    
    def registrar_usuario(self, nombre, correo, contrasena):
        self.driver.find_element(By.ID, "name").send_keys(nombre)  # Campo de nombre
        self.driver.find_element(By.ID, "email").send_keys(correo)  # Campo de email
        self.driver.find_element(By.ID, "password").send_keys(contrasena)  # Campo de contraseña
        self.driver.find_element(By.ID, "confirm_password").send_keys(contrasena)  # Confirmación de contraseña
        self.driver.find_element(By.ID, "register_button").click()  # Botón de registro
```

### `test_inlaze.py`
Este archivo contiene los casos de prueba con **unittest**:

```python
import unittest
from selenium import webdriver
from pages.pagina_inlaze import PaginaInlaze

class PruebasInlaze(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Inicializa el navegador Chrome
        self.driver.maximize_window()  # Maximiza la ventana
        self.pagina = PaginaInlaze(self.driver)  # Instancia la página de prueba
        self.pagina.abrir()  # Abre la página en el navegador
    
    def test_registrar_usuario_valido(self):
        # Prueba el registro de un usuario válido
        self.pagina.registrar_usuario("Juan Perez", "juan.perez@example.com", "Contrasena123!")  
    
    def test_iniciar_sesion_usuario_valido(self):
        # Prueba el inicio de sesión con credenciales válidas
        self.pagina.iniciar_sesion("juan.perez@example.com", "Contrasena123!")  
    
    def test_cerrar_sesion(self):
        # Prueba el cierre de sesión
        self.pagina.iniciar_sesion("juan.perez@example.com", "Contrasena123!")  
        self.pagina.cerrar_sesion()  
    
    def tearDown(self):
        self.driver.quit()  # Cierra el navegador después de la prueba
```

¡Listo! Ahora puedes comenzar con la automatización de pruebas 
