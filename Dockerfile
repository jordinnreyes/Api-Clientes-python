# Usa una imagen base de Python
FROM python:3-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /apiClientes

# Copia el archivo de requisitos y instala las dependencias
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copia el resto de los archivos
COPY . .

# Espera a que MySQL esté disponible antes de ejecutar db.py
# Reemplaza "mysql" con el nombre del servicio en docker-compose.yml
RUN apt-get update && apt-get install -y netcat && \
    while ! nc -z mysql 3306; do echo "Esperando a que MySQL esté disponible..."; sleep 5; done; \
    python3 db.py

# Comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]
