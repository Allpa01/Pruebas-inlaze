# Preguntas Frecuentes (FAQ) - Proyecto Inlaze

## 1. ¿Qué es este proyecto?
Este es un framework de pruebas automatizadas para la plataforma Inlaze, desarrollado con **Selenium y Python** en **Visual Studio Code**. Utiliza el modelo **Page Object Model (POM)** para organizar las pruebas de manera eficiente.

## 2. ¿Qué herramientas necesito instalar?
Antes de ejecutar el proyecto, asegúrate de tener instaladas las siguientes herramientas:
- **Python** (preferiblemente la versión más reciente)
- **Visual Studio Code**
- **Selenium** (administrado mediante `pip` en `requirements.txt`)
- **ChromeDriver** (para ejecutar las pruebas en Google Chrome)
- **Git** (si deseas clonar el repositorio desde GitHub)

## 3. ¿Cómo instalo las dependencias?
Ejecuta el siguiente comando en la terminal dentro del directorio del proyecto:
```sh
pip install -r requirements.txt
```
Esto instalará Selenium y cualquier otra librería necesaria para la ejecución de las pruebas.

## 4. ¿Cómo ejecuto las pruebas?
Para ejecutar las pruebas, usa el siguiente comando en la terminal dentro del directorio del proyecto:
```sh
python -m unittest discover tests
```
Esto buscará y ejecutará todas las pruebas dentro de la carpeta `tests`.

## 5. ¿Dónde se encuentran los archivos de prueba y páginas?
El proyecto sigue la estructura **POM (Page Object Model)**:
```
repo-inlaze/
│── pages/              # Clases que representan las páginas web
│   ├── pagina_inlaze.py
│── tests/              # Casos de prueba automatizados
│   ├── test_inlaze.py
│── requirements.txt    # Dependencias del proyecto
│── README.md           # Documentación principal
```

## 6. ¿Cómo puedo reportar un bug o un error en las pruebas?
Si encuentras un bug, puedes documentarlo en el archivo `reporte_bugs.md`. Asegúrate de incluir:
- Una descripción clara del problema
- Los pasos para reproducirlo
- El resultado esperado y el resultado obtenido
- Capturas de pantalla si es necesario

## 7. ¿Cómo puedo contribuir a este proyecto?
Si deseas contribuir:
1. **Clona el repositorio:**
   ```sh
   git clone https://github.com/tuusuario/tu-repositorio.git
   ```
2. **Crea una rama para tu cambio:**
   ```sh
   git checkout -b mi-nueva-funcionalidad
   ```
3. **Haz tus cambios y confírmalos:**
   ```sh
   git add .
   git commit -m "Descripción de mi cambio"
   ```
4. **Sube tu rama y crea un Pull Request:**
   ```sh
   git push origin mi-nueva-funcionalidad
   ```

## 8. ¿Qué hacer si tengo problemas al ejecutar las pruebas?
Si las pruebas no se ejecutan correctamente, revisa:
- Que tengas instalada la versión correcta de **ChromeDriver**.
- Que las dependencias estén instaladas correctamente (`pip install -r requirements.txt`).
- Que el navegador no tenga bloqueadores o extensiones que interfieran.
- Que los selectores de los elementos en **pagina_inlaze.py** sean correctos.

## 9. ¿Este proyecto es compatible con otros navegadores?
Por defecto, el proyecto está configurado para ejecutarse en **Google Chrome**. Sin embargo, puedes modificar el `webdriver` en `test_inlaze.py` para usar **Firefox (GeckoDriver)** o **Edge**.

## 10. ¿A quién puedo contactar si tengo dudas?
Puedes abrir un **Issue en GitHub** o contactar al equipo de QA en caso de necesitar ayuda adicional.
