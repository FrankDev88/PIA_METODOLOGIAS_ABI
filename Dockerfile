# Usa una imagen oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos
COPY requirements.txt .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el proyecto
COPY . .

# Expone el puerto del contenedor
EXPOSE 8000

# Ejecuta las migraciones y crea el superuser automáticamente
RUN python manage.py migrate && python create_superuser.py

# Comando por defecto
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

