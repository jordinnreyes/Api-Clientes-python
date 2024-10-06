# Usa una imagen base de Python
FROM python:3-slim


# Establece el directorio de trabajo en el contenedor
WORKDIR /apiClientes

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copia el resto de los archivos
COPY . .

# Instala netcat-openbsd para esperar a MySQL
RUN apt-get update && apt-get install -y netcat-openbsd

# Comando para ejecutar la aplicación Flask y crear la base de datos
CMD ["sh", "-c", "while ! nc -z mysql 3306; do echo 'Esperando a que MySQL esté disponible...'; sleep 5; done; python app.py"]
