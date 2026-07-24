#  Proyecto Universitario - MUUCHO OINK

## Descripción

Este proyecto académico fue desarrollado como parte de las asignaturas de **Programación Orientada a Objetos (POO)**, **Bases de Datos** y **Tópicos de Software**.

El objetivo es implementar una solución tecnológica para la empresa **MUUCHO OINK**, integrando conceptos de programación orientada a objetos, persistencia de datos y desarrollo de software con una arquitectura organizada bajo el patrón **Modelo–Vista–Controlador (MVC)**.

---

## Objetivos

- Aplicar los principios de **Programación Orientada a Objetos (POO)**.
- Diseñar e implementar una **base de datos** para la gestión de la información.
- Desarrollar una aplicación utilizando una arquitectura **MVC**.
- Implementar un sistema de autenticación de usuarios.
- Generar comprobantes de venta en formato PDF.

---

## Funcionalidades

- Inicio de sesión de usuarios.
- Gestión de productos.
- Registro de ventas.
- Cálculo automático de subtotal, IGV y total.
- Generación de comprobantes en PDF.
- Conexión con base de datos.

---

## Modificaciones realizadas

El proyecto tomó como referencia un repositorio público, el cual fue adaptado y mejorado para cumplir con los requerimientos académicos y de la empresa **MUUCHO OINK**.

Entre las principales modificaciones se encuentran:

- Incorporación de un sistema de autenticación de usuarios.
- Reestructuración del proyecto bajo el patrón MVC.
- Personalización de recursos gráficos (assets).
- Implementación del módulo de ventas.
- Generación automática de comprobantes en PDF.
- Adaptación de la base de datos.

---

## Tecnologías utilizadas

- Python
- SQLite
- Programación Orientada a Objetos (POO)
- Arquitectura MVC

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd PROYECTOOINK
```

### 2. Crear un entorno virtual

```bash
python -m venv .env
```

### 3. Activar el entorno virtual

**Windows**

```bash
.env\Scripts\activate
```

**Linux / macOS**

```bash
source .env/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Ejecutar la aplicación

```bash
python main.py
```

---

## Estructura de carpetas 

```text
PROYECTOOINK/
│
├── assets/
│   ├── icons/
│   ├── images/
│   └── styles/
│
├── controllers/
│   ├── producto_controller.py
│   ├── usuario_controller.py
│   └── venta_controller.py
│
├── database/
│   ├── data/
│   ├── db_connection.py
│   └── schema.sql
│
├── models/
│
├── ventas_pdf/
│
├── views/
│   ├── login_view.py
│   ├── main_view.py
│   ├── producto_view.py
│   ├── usuario_view.py
│   └── venta_view.py
│
├── config.py
├── main.py
├── requirements.txt
└── .gitignore
```

---

## Arquitectura

El proyecto utiliza el patrón **Modelo–Vista–Controlador (MVC)**:

- **Models:** representan la lógica de negocio y el acceso a los datos.
- **Views:** contienen la interfaz gráfica de usuario.
- **Controllers:** coordinan la comunicación entre las vistas y los modelos.
- **Database:** administra la conexión y el esquema de la base de datos.

---

## Créditos

Proyecto desarrollado por estudiantes universitarios como parte de las asignaturas de:

- Programación Orientada a Objetos
- Bases de Datos
- Tópicos de Software

El sistema fue adaptado y personalizado para la empresa **MUUCHO OINK** con fines académicos.
