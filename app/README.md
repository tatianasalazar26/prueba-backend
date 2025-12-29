# Prueba Técnica Backend – FastAPI

API REST desarrollada con **FastAPI** para la gestión de usuarios y tareas.  
Incluye autenticación mediante **JWT**, endpoints protegidos y paginación.

El proyecto está estructurado siguiendo buenas prácticas de separación por capas
(models, schemas, routers, core, db).

---

## Tecnologías usadas

- Python 3.11
- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT (python-jose)
- Passlib (hash de contraseñas)
- Uvicorn

---

## Requisitos

- Python 3.11+
- PostgreSQL en ejecución
- Git (opcional)

---

## Instalación

Clonar el repositorio y ubicarse en la carpeta raíz del proyecto:

```bash
git clone <url-del-repositorio>
cd prueba-backend
```

Crear y activar entorno virtual:

```bash
python -m venv venv
venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Ejecución

Levantar la aplicación con:

```bash
python -m uvicorn app.main:app --reload
```

La API estará disponible en:

- http://127.0.0.1:8000  
- Swagger UI: http://127.0.0.1:8000/docs

---

## Autenticación

La API utiliza autenticación **JWT (Bearer Token)**.

### Login

**Endpoint:**
```
POST /auth/login
```

**Credenciales de prueba:**
```
username: admin
password: admin123
```

Devuelve un token JWT que debe usarse para acceder a los endpoints protegidos.

En Swagger:
1. Clic en **Authorize**
2. Ingresar usuario y contraseña
3. Swagger gestionará automáticamente el token

---

## Endpoints principales

### Usuarios
- `POST /users` → Crear usuario

### Autenticación
- `POST /auth/login` → Obtener JWT

### Tareas (protegidos con JWT)
- `POST /tasks` → Crear tarea
- `GET /tasks` → Listar tareas con paginación

#### Parámetros de paginación
- `page`: número de página (por defecto 1)
- `size`: cantidad de registros por página (por defecto 10)

---

## Estructura del proyecto

```
prueba-backend/
│
├── app/
│   ├── api/
│   │   ├── auth/
│   │   ├── users.py
│   │   └── tasks.py
│   ├── core/
│   │   ├── auth.py
│   │   ├── jwt.py
│   │   └── security.py
│   ├── db/
│   ├── models/
│   ├── schemas/
│   └── main.py
│
├── requirements.txt
├── README.md
└── venv/
```

---

## Notas finales

- Los endpoints de tareas están protegidos con JWT.
- Las contraseñas se almacenan de forma segura usando hashing.
- El proyecto es completamente funcional y reproducible usando `requirements.txt`.

---

## Autor

Angie Tatiana Salazar Muñetón
