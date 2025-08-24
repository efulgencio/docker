# Ejemplo "Hello World" de Docker

Este proyecto es una aplicación web simple "Hello World" creada con Python y el framework Flask. Está containerizada usando Docker.

## Requisitos

- Docker Desktop

## Cómo Usar

1.  **Construir la Imagen de Docker:**

    Abre tu terminal, navega a este directorio y ejecuta el siguiente comando para construir la imagen de Docker. La etiqueta `-t hello-docker` le da un nombre a la imagen para que sea fácil de recordar.

    ```bash
    docker build -t hello-docker .
    ```

2.  **Ejecutar el Contenedor de Docker:**

    Una vez que la imagen esté construida, ejecuta el siguiente comando para iniciar el contenedor. Esto hará que la aplicación web esté disponible en tu máquina local.

    ```bash
    # Ejecutar con el saludo por defecto
    docker run -d -p 5000:5000 hello-docker
    ```

3.  **Acceder a la Aplicación:**

    Abre tu navegador web y visita [http://localhost:5000](http://localhost:5000). Deberías ver el mensaje "Hello, World!".

## Personalizar el Saludo

Puedes personalizar el mensaje de saludo estableciendo la variable de entorno `NAME` al ejecutar el contenedor.

```bash
# Ejecutar con un nombre personalizado (por ejemplo, "Gemini")
docker run -d -p 5000:5000 -e NAME=Gemini hello-docker
```

Ahora, si accedes a [http://localhost:5000](http://localhost:5000), el mensaje será "Hello, Gemini!".

## Detener el Contenedor

Para encontrar el ID de tu contenedor en ejecución, usa:

```bash
docker ps
```

Luego, usa el ID del contenedor para detenerlo:

```bash
docker stop <TU_ID_DE_CONTENEDOR>
```
