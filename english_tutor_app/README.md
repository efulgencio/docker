# English Tutor App

Esta es una simple aplicación de tutor de inglés creada con Flask.

## Cómo levantar el contenedor

### Prerrequisitos

- Docker instalado

### Pasos

1.  **Construir la imagen de Docker:**

    ```bash
    docker build -t english-tutor-app .
    ```

2.  **Correr el contenedor de Docker:**

    ```bash
    docker run -p 5000:5000 english-tutor-app
    ```

3.  **Acceder a la aplicación:**

    Abre tu navegador y ve a `http://localhost:5000`
