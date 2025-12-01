Proyecto Fullstack: Django + Angular + MySQL con Docker

Desarrollo 100% portable en cualquier computadora

Este proyecto utiliza Docker y Docker Compose para levantar:

Backend Django

Frontend Angular

Base de datos MySQL

Comunicación entre contenedores

De esta forma, puedes descargar el repositorio en cualquier PC y ejecutar TODO sin instalar Python, Node ni MySQL localmente.

📁 Estructura del proyecto
miapp/
│
├── backend/
│     ├── Dockerfile
│     ├── requirements.txt
│     ├── manage.py
│     └── backend/settings.py
│
├── frontend/
│     ├── Dockerfile
│     ├── package.json
│     └── src/…
│
└── docker-compose.yml
└── README.md

🐳 1. Docker — Requisitos

Instala Docker Desktop (solo la primera vez):
https://www.docker.com/products/docker-desktop/

⚙️ 2. Instrucciones para levantar el proyecto
👉 Paso 1: Clonar el repositorio
git clone https://github.com/usuario/miapp.git
cd miapp

👉 Paso 2: Levantar TODO (backend + frontend + mysql)
docker compose up --build


Docker descargará las imágenes, creará contenedores y correrá:

Django API → http://localhost:8000

Angular Frontend → http://localhost:4200

MySQL → puerto 3306

🧱 3. Backend Django — Dockerfile

backend/Dockerfile:

FROM python:3.12

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

🎨 4. Frontend Angular — Dockerfile

frontend/Dockerfile:

FROM node:20

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 4200

CMD ["npm", "start"]


Asegúrate de que en package.json exista:

"start": "ng serve --host 0.0.0.0"

🐬 5. Base de datos MySQL

El contenedor lo creará automáticamente el docker-compose.yml.

🧩 6. docker-compose.yml (la magia del proyecto)

Archivo en raíz del proyecto:

version: '3.9'

services:
  mysql:
    image: mysql:8.0
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: miapp
      MYSQL_USER: user
      MYSQL_PASSWORD: pass
    ports:
      - "3306:3306"
    volumes:
      - mysqldata:/var/lib/mysql

  backend:
    build: ./backend
    restart: always
    volumes:
      - ./backend:/app
    ports:
      - "8000:8000"
    depends_on:
      - mysql
    environment:
      DB_HOST: mysql
      DB_NAME: miapp
      DB_USER: user
      DB_PASS: pass

  frontend:
    build: ./frontend
    restart: always
    volumes:
      - ./frontend:/app
    ports:
      - "4200:4200"
    depends_on:
      - backend

volumes:
  mysqldata:

🔧 7. Configuración de Django para MySQL

En backend/settings.py agrega:

import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}

🧪 8. Comandos útiles
Ver contenedores
docker ps

Apagar todo
docker compose down

Reconstruir solo backend
docker compose build backend

Entrar al backend
docker exec -it miapp-backend-1 bash

🏁 9. Desarrollo en cualquier computadora

Después de clonar el repositorio:

cd miapp
docker compose up --build


Y el sistema corre completamente.

No necesitas:
❌ instalar Python
❌ instalar Node
❌ instalar MySQL
❌ configurar puertos
❌ instalar dependencias

Todo lo hace Docker.

📬 10. Contacto

Proyecto creado por Saps 