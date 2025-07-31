# Reunion Rest API

API REST para la gestión de reuniones y salas de conferencias, construida con **FastAPI** siguiendo principios de **Clean Architecture**.

## 🚀 Características

- Gestión de usuarios con autenticación JWT
- Programación y administración de reuniones
- Control de salas y disponibilidad
- Sistema de participantes en reuniones
- Filtros avanzados por múltiples criterios
- Documentación automática con OpenAPI

## 🛠️ Stack Tecnológico

- **Framework**: FastAPI
- **Base de Datos**: PostgreSQL
- **ORM**: SQLAlchemy
- **Autenticación**: JWT + bcrypt
- **Validación**: Pydantic

## 📚 Documentación

La API incluye documentación automática disponible en:
- Swagger UI: `/docs`

## 🔒 Seguridad

- Autenticación basada en JWT
- Hash de contraseñas con bcrypt
- Validación de entrada con Pydantic
- Variables sensibles en archivo .env
