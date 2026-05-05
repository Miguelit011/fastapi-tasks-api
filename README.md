# Tasks API

REST API para gestión de tareas construida con FastAPI y SQLAlchemy.

## Stack
- Python 3.10
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn

## Instalación

```bash
git clone https://github.com/TU_USUARIO/fastapi-tasks-api.git
cd fastapi-tasks-api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Arrancar la API

```bash
uvicorn app.main:app --reload
```

Documentación disponible en `http://localhost:8000/docs`

## Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | /tasks | Obtener todas las tareas |
| GET | /tasks/{id} | Obtener una tarea |
| POST | /tasks | Crear una tarea |
| PUT | /tasks/{id} | Actualizar una tarea |
| DELETE | /tasks/{id} | Eliminar una tarea |