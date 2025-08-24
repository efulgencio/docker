# Usa una imagen oficial de Python como imagen padre
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /usr/src/app

# Copia el archivo de requisitos al contenedor
COPY requirements.txt ./

# Instala los paquetes necesarios especificados en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
COPY . .

# Expone el puerto 5000 para que sea accesible desde fuera del contenedor
EXPOSE 5000

# Ejecuta app.py cuando se inicie el contenedor
CMD ["python", "./app.py"]
