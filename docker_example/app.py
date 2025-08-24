from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Lee la variable de entorno NAME, con 'World' como valor por defecto
    name = os.environ.get('NAME', 'World')
    return f'Hello, {name}!'

if __name__ == '__main__':
    # Escucha en todas las IPs disponibles (0.0.0.0) en el puerto 5000
    app.run(debug=True, host='0.0.0.0', port=5000)
