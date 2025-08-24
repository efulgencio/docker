import os
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

# Inicializar Flask
app = Flask(__name__)

# Configurar el directorio de subidas
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Asegurarse de que el directorio de subidas exista
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Cargar el modelo de IA pre-entrenado (MobileNetV2)
# Esto puede tardar un momento la primera vez que se ejecuta,
# ya que necesita descargar los pesos del modelo.
print("Cargando modelo de IA...")
model = MobileNetV2(weights='imagenet')
print("Modelo cargado exitosamente.")

def predict_image(img_path):
    """Carga una imagen, la preprocesa y devuelve la predicción."""
    try:
        # Cargar la imagen con el tamaño que el modelo espera (224x224)
        img = image.load_img(img_path, target_size=(224, 224))
        
        # Convertir la imagen a un array de numpy
        img_array = image.img_to_array(img)
        
        # Añadir una dimensión extra para que coincida con la entrada del modelo
        img_array_expanded = np.expand_dims(img_array, axis=0)
        
        # Preprocesar la imagen (normalización específica para MobileNetV2)
        processed_img = preprocess_input(img_array_expanded)
        
        # Realizar la predicción
        predictions = model.predict(processed_img)
        
        # Decodificar las predicciones en etiquetas legibles (tomamos la más probable)
        decoded_predictions = decode_predictions(predictions, top=1)[0]
        
        # Extraer la etiqueta y la probabilidad
        _, label, probability = decoded_predictions[0]
        return f"{label.replace('_', ' ')} ({probability:.2%})"
    except Exception as e:
        return f"Error al procesar la imagen: {e}"

@app.route('/', methods=['GET'])
def index():
    """Renderiza la página principal."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def upload_and_predict():
    """Maneja la subida de la imagen y muestra la predicción."""
    if 'image' not in request.files:
        return render_template('index.html', error="No se encontró el archivo de imagen.")
    
    file = request.files['image']
    
    if file.filename == '':
        return render_template('index.html', error="No se seleccionó ninguna imagen.")
        
    if file:
        # Usamos un nombre de archivo seguro para evitar problemas de seguridad
        filename = secure_filename(file.filename)
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(img_path)
        
        # Obtener la predicción
        prediction_result = predict_image(img_path)
        
        # Eliminar la imagen después de la predicción para no acumular archivos
        os.remove(img_path)
        
        return render_template('index.html', prediction=prediction_result)

    return redirect(url_for('index'))

if __name__ == '__main__':
    # La aplicación se ejecutará en el puerto 5000
    app.run(host='0.0.0.0', port=5000)
