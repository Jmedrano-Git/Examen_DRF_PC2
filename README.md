# 🎮 API de Juegos y Compañías - Tecsup

## 🏫 Información del Proyecto

**Institución:** Tecsup  
**Docente:** Elliot Leo Garamendi Sarmiento  
**Curso:** Desarrollo de Aplicaciones Empresariales  
**Alumno:** Julio César Medrano Yupanqui  

---

## 🧩 Descripción del Proyecto

Este proyecto implementa una **API REST** desarrollada con **Django REST Framework**, que permite gestionar información sobre **juegos y compañías**.  
Cada compañía puede tener varios juegos asociados, y la API cuenta con operaciones crud, así como búsqueda y documentación automática con Swagger.

---

## 🛠️ Tecnologías Usadas

- **Python 3.13**
- **Django 5**
- **Django REST Framework**
- **drf-spectacular** (para la documentación Swagger)
- **SQLite3** (por defecto la DB)

---

## 🚀 Instrucciones para Ejecutar el Servidor

1. Clonar el repositorio o copiar el proyecto:
   ```bash
   git clone <URL-del-repositorio>
   cd Examen_DRF2

2. Crear y activar el entorno virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # En Windows
   # o
   source venv/bin/activate   # En Linux/Mac

3. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt

4. Aplicar las migraciones:
   ```bash
   python manage.py migrate

5. Ejecutar el servidor:
   ```bash
   python manage.py runserver

6. Abrir en el navegador:
   ```bash
   http://127.0.0.1:8000/api/docs/ #para la documentación
   http://127.0.0.1:8000/api/v1 #la app

## 📍 Endpoints "Companies and Games"

Companies ✅:

- **GET - /api/v1/companies/**
- **POST - /api/v1/companies/** 
- **GET - /api/v1/companies/{id}/** #Para la búsqueda unitaria
- **PUT - /api/v1/companies/{id}/**
- **DELETE - /api/v1/companies/{id}/**

Games ✅:

- **GET - /api/v1/games/**
- **POST - /api/v1/games/** 
- **GET - /api/v1/games/{id}/** #Para la búsqueda unitaria
- **PUT - /api/v1/games/{id}/{id}/**
- **DELETE - /api/v1/games/{id}//**

# Ejemplos:

```bash
🎯 COMPANIES:

   # Listar compañías
   curl -X GET http://127.0.0.1:8000/api/v1/companies/

   # Crear compañía
   curl -X POST http://127.0.0.1:8000/api/v1/companies/ \
     -H "Content-Type: application/json" \
     -d '{"name": "Nintendo", "country": "Japón"}'
   
   # Ver una compañía por ID
   curl -X GET http://127.0.0.1:8000/api/v1/companies/1/
   
   # Actualizar una compañía
   curl -X PATCH http://127.0.0.1:8000/api/v1/companies/1/ \
     -H "Content-Type: application/json" \
     -d '{"country": "EE.UU."}'
   
   # Eliminar una compañía
   curl -X DELETE http://127.0.0.1:8000/api/v1/companies/1/

🎯 GAMES:

   # Listar juegos
   curl -X GET http://127.0.0.1:8000/api/v1/games/
   
   # Crear juego
   curl -X POST http://127.0.0.1:8000/api/v1/games/ \
     -H "Content-Type: application/json" \
     -d '{"title": "Zelda: Breath of the Wild", "genre": "Aventura", "company": 1}'
   
   # Buscar juego por título o género
   curl -X GET "http://127.0.0.1:8000/api/v1/games/?search=Zelda"
   
   # Ver un juego por ID
   curl -X GET http://127.0.0.1:8000/api/v1/games/1/
   
   # Actualizar un juego
   curl -X PATCH http://127.0.0.1:8000/api/v1/games/1/ \
     -H "Content-Type: application/json" \
     -d '{"genre": "Acción"}'
   
   # Eliminar un juego
   curl -X DELETE http://127.0.0.1:8000/api/v1/games/1/

