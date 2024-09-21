# FastAPI REST API Tutorial

Este repositorio es un ejemplo de una API RESTful implementada con FastAPI. Incluye conceptos como DDD, Vertical Slices, Inyección de Dependencias, Seguridad, Swagger y más.


## Características

- **FastAPI**: Framework web moderno y de alto rendimiento para construir APIs con Python 3.7+ basado en estándares como OpenAPI y JSON Schema.
- **RESTful API**: Diseño de la API siguiendo los principios REST.
- **Domain-Driven Design (DDD)**: Separación clara de las responsabilidades y lógica del dominio.
- **Vertical Slices**: Organización del código por características en lugar de por capas técnicas.
- **Inyección de Dependencias**: Gestión e inyección de dependencias con FastAPI.
- **Seguridad**: Implementación de autenticación y autorización.
- **Swagger**: Documentación interactiva de la API.

## Estructura del Proyecto

```
qna_api/
│
├── auth/
│   ├── models.py
│   ├── routes.py
│   └── service.py
│
├── core/
│   ├── base_repository.py
│   ├── config.py
│   ├── constants.py
│   ├── database.py
│   └── logging.py
│
├── domain/
│   ├── answer.py
│   ├── question.py
│   └── user.py
│
│
└── user/
    ├── controller.py
    ├── models.py
    ├── repository.py
    └── service.py
```

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/Kennethbrandonduenas/pythonprueba
    ```

2. Navega al directorio del proyecto:
    ```bash
    cd pythonprueba
    ```

3. Crea un entorno virtual y activa:
    ```bash
    python -m venv .venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

4. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

5. Configura las variables de entorno:
   Antes de iniciar la aplicación, necesitas configurar las variables de entorno. Sigue estos pasos:

    1. Copia el archivo `.env.example` a `.env`:
    ```sh
    cp .env.example .env
    ```

    2. Rellena las variables de entorno en el archivo `.env` con tus propios valores:
    ```
    SECRET_KEY=your_secret_key
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    DATABASE_URL=sqlite:///./sql_app.db
    INITIAL_ADMIN_USERNAME=admin
    INITIAL_ADMIN_EMAIL=admin@example.com
    INITIAL_ADMIN_PASSWORD=admin
    ```

6. Inicia la aplicación:
    Desde vscode selecciona la opción local o docker y ejecútalo.

## Uso

1. Visita `http://127.0.0.1:8000` y te redirigirá a /doc para ver la documentación interactiva de la API (swagger).
2. Visita `http://127.0.0.1:8000/redoc` para ver la documentación alternativa de la API.

## Enlaces útiles

- [Documentación de FastAPI](https://fastapi.tiangolo.com/)

