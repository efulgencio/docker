# Jira Software en Docker

Este proyecto utiliza Docker Compose para ejecutar una instancia local de Jira Software con persistencia de datos.

## Prerrequisitos

- Docker
- Docker Compose

## Cómo Iniciar Jira

1.  Navega al directorio `jira_docker` en tu terminal.
2.  Ejecuta el siguiente comando:

    ```bash
    docker-compose up -d
    ```

La primera vez que ejecutes este comando, Docker descargará la imagen de Jira, lo cual puede tardar varios minutos. En los siguientes inicios, será mucho más rápido.

## Configuración Inicial (Solo la primera vez)

Jira es una aplicación grande y puede tardar entre 2 y 5 minutos en arrancar por completo después de que el comando anterior haya terminado.

1.  Abre tu navegador web y ve a **[http://localhost:8080](http://localhost:8080)**.
    *Si ves un error o una página de "Iniciando", espera un minuto más y vuelve a cargar la página.*

2.  Cuando veas la pantalla de configuración de Jira, sigue estos pasos:
    *   **Opción de configuración:** Elige la opción que diga **"Set it up for me"** o "Configurar por mí".
    *   **Licencia:** Te pedirá una clave de licencia. Deberás seleccionar la opción para **generar una licencia de prueba de Jira Software**.
    *   **Sitio de Atlassian:** Serás redirigido al sitio web de Atlassian. Es posible que necesites iniciar sesión o crear una cuenta gratuita de Atlassian para continuar.
    *   **Pegar licencia:** Una vez generada, copia la clave de licencia y pégala de nuevo en la página de configuración de tu Jira local (la de `localhost:8080`).
    *   **Cuenta de administrador:** Sigue los últimos pasos para crear tu cuenta de administrador. ¡Recuerda bien esta contraseña!

## Uso Diario

-   **Para iniciar Jira:**
    ```bash
    docker-compose up -d
    ```
-   **Para detener Jira:**
    ```bash
    docker-compose down
    ```

Gracias al volumen de Docker que hemos configurado (`jiradata`), todos tus proyectos, tareas y configuraciones se guardarán de forma segura aunque detengas el contenedor.

---

## Notas Adicionales

### ¿Qué pasa si ya tengo otro servicio en el puerto 8080?

Si al ejecutar `docker-compose up -d` recibes un error sobre "port is already allocated" (el puerto ya está en uso), significa que ya tienes otro programa (posiblemente otro Jira) usando el puerto 8080 en tu máquina.

Para solucionarlo, abre el archivo `docker-compose.yml` y modifica la sección de `ports`. Cambia el primer número a un puerto que esté libre en tu máquina, por ejemplo, `8081`:

**Cambia esto:**
```yaml
    ports:
      - "8080:8080"
```

**Por esto:**
```yaml
    ports:
      - "8081:8080" # Ahora accederás a Jira en http://localhost:8081
```

Guarda el archivo y vuelve a ejecutar `docker-compose up -d`. Ahora tu nueva instancia de Jira será accesible en `http://localhost:8081`.
