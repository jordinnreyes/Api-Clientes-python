# Usa una imagen base de Python
FROM python:3-slim


# Establece el directorio de trabajo en el contenedor
WORKDIR /apiClientes

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copia el resto de los archivos
COPY . .

RUN python3 db.py
# Comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]
