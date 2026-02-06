# 🚀 FastAPI Tasks API --- Production Style Backend

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Modern-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Pytest](https://img.shields.io/badge/Tests-Pytest-yellow)

API REST para la gestión de tareas desarrollada con **FastAPI**,
**PostgreSQL**, **SQLAlchemy**, **Docker** y **pytest**.

Proyecto diseñado siguiendo buenas prácticas profesionales de desarrollo
backend, con enfoque en reproducibilidad, testing automatizado y
arquitectura desacoplada.

------------------------------------------------------------------------

## 📌 Características

✔ API REST completa (CRUD de tareas)  
✔ Arquitectura desacoplada (schemas, models, database)  
✔ PostgreSQL como base de datos relacional  
✔ Docker Compose con múltiples servicios  
✔ Tests automatizados con pytest  
✔ Configuración reproducible con `pytest.ini`  
✔ Healthchecks entre servicios  
✔ Variables de entorno para configuración flexible  
✔ Documentación automática con Swagger y ReDoc  

------------------------------------------------------------------------

## 🧱 Arquitectura

    FastAPI
       │
       ├── SQLAlchemy (ORM)
       │
       ├── PostgreSQL
       │
       └── Docker Compose
              ├── fastapi_api
              ├── postgres_db
              └── pgadmin

------------------------------------------------------------------------

## 📂 Estructura del proyecto

    docker-fastapi-postgres/
    │
    ├── app/
    │   ├── __init__.py
    │   ├── main.py
    │   ├── database.py
    │   ├── models.py
    │   ├── schemas.py
    │   └── requirements.txt
    │
    ├── tests/
    │   ├── conftest.py
    │   └── test_tasks.py
    │
    ├── db/
    │   └── init/
    │       └── 01_create_test_db.sql
    │
    ├── docker-compose.yml
    ├── Dockerfile
    ├── pytest.ini
    ├── .env.example
    ├── .env.test
    └── README.md

------------------------------------------------------------------------

## ⚙️ Requisitos

- Docker
- Docker Compose
- Python 3.12 (opcional para ejecución local)

------------------------------------------------------------------------

## 🔐 Configuración

### 1️⃣ Copiar variables de entorno

Linux / Mac:

```bash
cp .env.example .env
```

Windows (PowerShell):

```powershell
copy .env.example .env
```

📌 **Nota:** Para PgAdmin se incluyen credenciales por defecto en `.env.example`.

Editar `.env` si es necesario.

------------------------------------------------------------------------

## 🐳 Ejecución con Docker

### Levantar servicios

```bash
docker compose up -d --build
```

------------------------------------------------------------------------

### Ver logs de la API

```bash
docker compose logs -f fastapi_api
```

------------------------------------------------------------------------

### Detener servicios

```bash
docker compose down
```

------------------------------------------------------------------------

## 🌐 Acceso a la aplicación

### API
👉 http://localhost:8000

### Swagger UI
👉 http://localhost:8000/docs

### ReDoc
👉 http://localhost:8000/redoc

### PgAdmin
👉 http://localhost:5050

------------------------------------------------------------------------

## 🧪 Tests automatizados

Ejecutar:

```bash
python -m pytest -q
```

------------------------------------------------------------------------

## 👨‍💻 Autor

Marcial Godes  
LinkedIn: https://www.linkedin.com/in/marcial-godes-alameda-91093b194/

⭐ Proyecto educativo orientado a portfolio profesional backend
