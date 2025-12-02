# Imagen base de Python
FROM python:3.12-slim

# Evitar preguntas interactivas
ENV PYTHONUNBUFFERED=1

# Crear directorio de trabajo
WORKDIR /app
# --- SE AGREGO ESTO ---
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*
# ----------------------
# Copiar requirements e instalarlos
COPY ../requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el backend
COPY . .

# Puerto que expone Django
EXPOSE 8000

# Comando por defecto
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
