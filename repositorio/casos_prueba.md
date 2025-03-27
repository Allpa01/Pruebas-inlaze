# Casos de Prueba - Inlaze QA

## 1. Registro de Usuario

### CP-001: Registro exitoso de usuario
**Descripción**: Verificar que un usuario pueda registrarse con datos válidos.  
**Precondiciones**: El usuario no debe estar registrado previamente.  

**Pasos**:  
1. Ingresar a la página de registro.  
2. Completar los campos con datos válidos: nombre, email y contraseña.  
3. Confirmar la contraseña.  
4. Hacer clic en "Registrar".  

**Datos de prueba**:  
- Nombre: "Juan Pérez"  
- Email: "juan.perez@example.com"  
- Contraseña: "Pass@1234"  

**Resultado esperado**: El sistema debe registrar exitosamente al usuario y mostrar un mensaje de confirmación.  

---

### CP-002: Validación del campo Nombre
**Descripción**: Verificar que el campo Nombre no acepte menos de dos palabras.  
**Precondiciones**: Ninguna.  

**Pasos**:  
1. Ingresar a la página de registro.  
2. Introducir un nombre con una sola palabra (ej. "Juan").  
3. Completar el resto de los campos con datos válidos.  
4. Intentar registrar el usuario.  

**Datos de prueba**:  
- Nombre: "Juan"  

**Resultado esperado**: El sistema debe mostrar un mensaje de error indicando que el nombre debe contener al menos dos palabras.  

---

### CP-003: Validación del formato de email
**Descripción**: Verificar que el sistema no permita registrar un usuario con un email inválido.  
**Precondiciones**: Ninguna.  

**Pasos**:  
1. Ingresar a la página de registro.  
2. Introducir un email inválido (ej. "juan.perez@com").  
3. Completar los demás campos con datos válidos.  
4. Intentar registrar el usuario.  

**Datos de prueba**:  
- Email: "juan.perez@com"  

**Resultado esperado**: El sistema debe mostrar un mensaje de error indicando que el email no es válido.  

---

### CP-004: Validación de contraseña
**Descripción**: Verificar que el sistema no permita registrar una contraseña que no cumpla con los requisitos.  
**Precondiciones**: Ninguna.  

**Pasos**:  
1. Ingresar a la página de registro.  
2. Introducir una contraseña sin caracteres especiales ni números (ej. "Password").  
3. Completar los demás campos con datos válidos.  
4. Intentar registrar el usuario.  

**Datos de prueba**:  
- Contraseña: "Password"  

**Resultado esperado**: El sistema debe mostrar un mensaje de error indicando que la contraseña debe cumplir con los requisitos de seguridad.  

---

### CP-005: Validación de contraseñas coincidentes
**Descripción**: Verificar que el sistema valide si las contraseñas ingresadas coinciden.  
**Precondiciones**: Ninguna.  

**Pasos**:  
1. Ingresar a la página de registro.  
2. Introducir una contraseña en el campo "Contraseña" y una diferente en "Confirmar Contraseña".  
3. Completar los demás campos con datos válidos.  
4. Intentar registrar el usuario.  

**Datos de prueba**:  
- Contraseña: "Pass@1234"  
- Confirmar Contraseña: "Pass@5678"  

**Resultado esperado**: El sistema debe mostrar un mensaje de error indicando que las contraseñas no coinciden.  

---

## 2. Login de Usuario

### CP-006: Inicio de sesión exitoso
**Descripción**: Verificar que un usuario registrado pueda iniciar sesión correctamente.  
**Precondiciones**: El usuario debe estar registrado.  

**Pasos**:  
1. Ingresar a la página de login.  
2. Introducir un email y contraseña válidos.  
3. Hacer clic en "Iniciar sesión".  

**Datos de prueba**:  
- Email: "juan.perez@example.com"  
- Contraseña: "Pass@1234"  

**Resultado esperado**: El sistema permite el acceso y muestra el nombre del usuario.  

---

### CP-007: Validación de campos vacíos en login
**Descripción**: Verificar que el formulario de login no se envíe si hay campos vacíos.  
**Precondiciones**: Ninguna.  

**Pasos**:  
1. Ingresar a la página de login.  
2. Dejar uno o ambos campos vacíos.  
3. Intentar iniciar sesión.  

**Datos de prueba**:  
- Email: ""  
- Contraseña: "Pass@1234"  

**Resultado esperado**: El sistema debe mostrar un mensaje de error indicando que los campos son obligatorios.  

---

### CP-008: Inicio de sesión con credenciales incorrectas
**Descripción**: Verificar que el sistema no permita el acceso con credenciales incorrectas.  
**Precondiciones**: Ninguna.  

**Pasos**:  
1. Ingresar a la página de login.  
2. Introducir un email válido y una contraseña incorrecta.  
3. Intentar iniciar sesión.  

**Datos de prueba**:  
- Email: "juan.perez@example.com"  
- Contraseña: "Incorrecta123"  

**Resultado esperado**: El sistema debe mostrar un mensaje de error indicando que las credenciales son incorrectas.  

---

### CP-009: Cierre de sesión
**Descripción**: Verificar que el usuario pueda cerrar sesión correctamente.  
**Precondiciones**: El usuario debe haber iniciado sesión.  

**Pasos**:  
1. Hacer clic en el botón de "Cerrar sesión".  
2. Confirmar la acción si es necesario.  

**Resultado esperado**: El usuario es redirigido a la página de login y su sesión es cerrada correctamente.  