# 🚀 FastAPI Tasks API -- Production Style Backend

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Modern-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Pytest](https://img.shields.io/badge/Tests-Pytest-yellow)

------------------------------------------------------------------------

API REST para la gestión de tareas desarrollada con **FastAPI**,
**PostgreSQL**, **SQLAlchemy**, **Docker** y **pytest**.\
Proyecto diseñado siguiendo buenas prácticas profesionales y
arquitectura moderna orientada a backend.

------------------------------------------------------------------------

## 📌 Características

✔ API REST completa (CRUD de tareas)\
✔ Arquitectura desacoplada (schemas, models, database, routers)\
✔ PostgreSQL como base de datos relacional\
✔ Docker Compose con múltiples servicios\
✔ Tests automatizados con pytest\
✔ Healthchecks entre servicios\
✔ Configuración mediante variables de entorno\
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
    ├── docker-compose.yml
    ├── .env.example
    ├── .env.test
    └── README.md

------------------------------------------------------------------------

## ⚙️ Requisitos

-   Docker
-   Docker Compose
-   Python 3.12 (opcional para ejecución local)

------------------------------------------------------------------------

## 🔐 Configuración

### 1️⃣ Copiar variables de entorno

    cp .env.example .env

Editar `.env` si es necesario.

------------------------------------------------------------------------

## 🐳 Ejecución con Docker

### Levantar servicios

    docker compose up -d --build

------------------------------------------------------------------------

## 🌐 Acceso a la aplicación

### API

👉 http://localhost:8000

### Swagger

👉 http://localhost:8000/docs

### ReDoc

👉 http://localhost:8000/redoc

### PgAdmin

👉 http://localhost:5050

------------------------------------------------------------------------

## 🧪 Tests automatizados

Ejecutar:

    python -m pytest -q

Los tests:

-   Usan una base de datos aislada
-   Crean tablas automáticamente
-   Limpian datos tras cada ejecución

------------------------------------------------------------------------

## 📡 Endpoints principales

  Método   Endpoint      Descripción
  -------- ------------- ------------------
  GET      /tasks        Obtener tareas
  POST     /tasks        Crear tarea
  GET      /tasks/{id}   Obtener tarea
  PUT      /tasks/{id}   Actualizar tarea
  DELETE   /tasks/{id}   Eliminar tarea

------------------------------------------------------------------------

## 🛠 Tecnologías utilizadas

-   FastAPI
-   SQLAlchemy
-   PostgreSQL
-   Docker
-   Pytest
-   Pydantic

------------------------------------------------------------------------

## 🧪 Ejemplo de request

### Crear tarea

    POST /tasks
    {
      "title": "Aprender Docker",
      "completed": false
    }

------------------------------------------------------------------------

## 📈 Posibles mejoras

-   Autenticación JWT
-   Migraciones con Alembic
-   CI/CD
-   Logging estructurado
-   Cobertura de tests
-   Separación por capas (Clean Architecture)

------------------------------------------------------------------------

## 👨‍💻 Autor

Marcial Godes

Proyecto educativo orientado a portfolio profesional backend.

------------------------------------------------------------------------

## ⭐ Licencia

Uso educativo y demostrativo.
