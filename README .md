# Proyecto: nombre-pro-clientes

## Datos del desarrollador

| Campo     | Detalle                        |
|-----------|--------------------------------|
| Nombre    | [Tu nombre aquí]               |
| Correo    | [tucorreo@email.com]           |
| Ciudad    | Medellín, Colombia             |
| Curso     | Desarrollo de APIs con Python  |
| Fecha     | Mayo 2026                      |

---

## Descripción

API REST construida con **Python** y **FastAPI** que expone dos endpoints:

- `GET /` — Retorna un mensaje de bienvenida del proyecto.
- `GET /clientes` — Retorna una lista de clientes registrados.

---

## Requisitos previos

Tener instalado:

- [Python](https://www.python.org/) v3.8 o superior

---

## Paso a paso de ejecución

### 1. Crear la carpeta del proyecto

```bash
mkdir nombre-pro-clientes
```

Crea una nueva carpeta llamada `nombre-pro-clientes` donde vivirá todo el proyecto.

---

### 2. Entrar a la carpeta

```bash
cd nombre-pro-clientes
```

Navega dentro de la carpeta recién creada.

---

### 3. Crear el entorno virtual

```bash
python -m venv venv
```

Crea un entorno virtual llamado `venv` dentro del proyecto. Esto aísla las librerías del proyecto del resto del sistema.

---

### 4. Activar el entorno virtual

**En Mac / Linux:**
```bash
source venv/bin/activate
```

**En Windows:**
```bash
venv\Scripts\activate
```

Cuando el entorno está activo, verás `(venv)` al inicio de tu terminal.

---

### 5. Instalar las dependencias

```bash
pip install fastapi uvicorn
```

Instala dos librerías:
- **fastapi** — framework para crear la API REST.
- **uvicorn** — servidor que ejecuta la aplicación FastAPI.

---

### 6. Crear el archivo principal

```bash
touch main.py
```

Crea el archivo `main.py` donde se define toda la lógica del servidor y los endpoints.

---

### 7. Ejecutar el servidor

```bash
uvicorn main:app --reload
```

Inicia el servidor en el puerto **8000**. El flag `--reload` hace que el servidor se reinicie automáticamente al detectar cambios en el código.

Deberías ver en consola:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

---

### 8. Probar los endpoints

Abre el navegador o una herramienta como **Postman** y prueba:

| Método | URL                               | Descripción           |
|--------|-----------------------------------|-----------------------|
| GET    | http://localhost:8000/            | Mensaje de bienvenida |
| GET    | http://localhost:8000/clientes    | Lista de clientes     |

FastAPI también genera documentación automática en:
- http://localhost:8000/docs ← interfaz interactiva (Swagger)
- http://localhost:8000/redoc

---

## Respuestas de ejemplo

### GET /

```json
{
  "mensaje": "este es el proyecto de clientes a desarrollar"
}
```

### GET /clientes

```json
{
  "status": "success",
  "total": 7,
  "data": [
    { "id": 1, "nombre": "Andrés Morales", "email": "andres.morales@email.com", "ciudad": "Bogotá", "telefono": "300-111-2233" },
    { "id": 2, "nombre": "Laura Gómez",    "email": "laura.gomez@email.com",    "ciudad": "Medellín", "telefono": "311-222-3344" }
  ]
}
```

---

## Estructura del proyecto

```
nombre-pro-clientes/
├── main.py          ← Servidor y endpoints
├── README.md        ← Este archivo
└── venv/            ← Entorno virtual (no subir a Git)
```

---

## Tecnologías usadas

- **Python** — Lenguaje de programación
- **FastAPI** — Framework para crear APIs REST modernas
- **Uvicorn** — Servidor ASGI para ejecutar FastAPI
