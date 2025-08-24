# Usar una imagen base de Python que sea relativamente ligera
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requisitos primero para aprovechar el cache de Docker
COPY requirements.txt .

# Instalar las dependencias
# La descarga de Tensorflow puede tardar varios minutos
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos de la aplicación
COPY . .

# El puerto que la aplicación Flask usará
EXPOSE 5000

# Comando para ejecutar la aplicación cuando se inicie el contenedor
# El modelo de IA se descargará la primera vez que se inicie el contenedor
CMD ["python", "app.py"]
