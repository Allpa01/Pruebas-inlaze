# Reporte de Bugs - Inlaze QA Test Front

## Bug #001: Validación incorrecta del campo Nombre
- **Severidad**: Alta  
- **Prioridad**: Alta  
- **Estado**: Abierto  
- **Módulo**: Registro de Usuario  

### Descripción  
El formulario de registro permite enviar el campo Nombre con una sola palabra, cuando debería requerir al menos dos palabras (nombre y apellido).  

### Pasos para Reproducir  
1. Ingresar a la página de registro: `httpstest-qa.inlaze.com`.  
2. Ingresar un solo nombre en el campo Nombre (ejemplo: "Juan").  
3. Completar los demás campos con datos válidos.  
4. Intentar enviar el formulario.  

### Resultado Esperado  
El sistema debe mostrar un mensaje de error indicando que el nombre debe contener al menos dos palabras.  

### Resultado Actual  
El sistema permite el registro con un solo nombre.  

---

## Bug #002: Validación de email duplicado no funciona correctamente
- **Severidad**: Alta  
- **Prioridad**: Alta  
- **Estado**: Abierto  
- **Módulo**: Registro de Usuario  

### Descripción  
El sistema permite registrar múltiples usuarios con la misma dirección de correo electrónico, lo cual no cumple con los requisitos establecidos.  

### Pasos para Reproducir  
1. Registrar un usuario con un email válido.  
2. Intentar registrar otro usuario con el mismo email.  
3. Completar los demás campos correctamente y enviar el formulario.  

### Resultado Esperado  
El sistema debe mostrar un mensaje de error indicando que el email ya está registrado.  

### Resultado Actual  
El sistema permite el registro con un email duplicado.  

---

## Bug #003: Mensaje de error incorrecto cuando las contraseñas no coinciden
- **Severidad**: Media  
- **Prioridad**: Media  
- **Estado**: Abierto  
- **Módulo**: Registro de Usuario  

### Descripción  
Si las contraseñas ingresadas en los dos campos no coinciden, el mensaje de error no es claro.  

### Pasos para Reproducir  
1. Ingresar datos válidos en los campos Nombre y Email.  
2. Ingresar una contraseña en el campo Contraseña.  
3. Ingresar una contraseña diferente en el campo Confirmar Contraseña.  
4. Intentar enviar el formulario.  

### Resultado Esperado  
El sistema debe mostrar un mensaje claro como: "Las contraseñas ingresadas no coinciden".  

### Resultado Actual  
El sistema muestra un mensaje genérico que no especifica el problema.  

---

## Bug #004: El botón Iniciar sesión permite envío con campos vacíos
- **Severidad**: Alta  
- **Prioridad**: Alta  
- **Estado**: Abierto  
- **Módulo**: Login de Usuario  

### Descripción  
El formulario de login permite hacer clic en el botón Iniciar sesión sin completar los campos obligatorios.  

### Pasos para Reproducir  
1. Ingresar a la página de login: `httpstest-qa.inlaze.com`.  
2. Dejar los campos de Email y Contraseña vacíos.  
3. Hacer clic en el botón Iniciar sesión.  

### Resultado Esperado  
El sistema debe evitar el envío del formulario y mostrar un mensaje indicando que los campos son obligatorios.  

### Resultado Actual  
El formulario se envía, generando un error inesperado en la plataforma.  

---

## Bug #005: No se muestra el nombre del usuario después del login
- **Severidad**: Media  
- **Prioridad**: Media  
- **Estado**: Abierto  
- **Módulo**: Login de Usuario  

### Descripción  
Tras iniciar sesión con credenciales válidas, el sistema no muestra el nombre del usuario en la interfaz.  

### Pasos para Reproducir  
1. Ingresar a la página de login.  
2. Ingresar credenciales válidas.  
3. Hacer clic en Iniciar sesión.  

### Resultado Esperado  
El sistema debe mostrar un mensaje de bienvenida con el nombre del usuario.  

### Resultado Actual  
El sistema redirige a la página de inicio sin mostrar el nombre del usuario.  

---

### Información Adicional  
- **Fecha de reporte**: [Fecha de ejecución de la prueba]  
- **Reportado por**: [Tu Nombre]  
- **Entorno de pruebas**:  
  - Navegador: Google Chrome 134.0.0.0  
  - Sistema Operativo: Windows 11  
  - Resolución de pantalla: 1920x1080  
