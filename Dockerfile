# Imagen base
FROM python:3.10-slim

# Establecer variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Crear directorios y usuario no root
RUN mkdir -p /app && useradd -m pcatia_user

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias de Python
COPY requirements-production.txt /app/
RUN pip install --no-cache-dir -r requirements-production.txt

# Copiar el código del proyecto
COPY . /app/

# Asegurar que el entrypoint sea ejecutable
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Asignar permisos al usuario no root
RUN chown -R pcatia_user:pcatia_user /app

# Cambiar al usuario no root
USER pcatia_user

# Configurar el entrypoint
ENTRYPOINT ["/entrypoint.sh"]

# Comando por defecto
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "pcatia.wsgi:application"]
