from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Esta función simula una llamada a un Modelo de Lenguaje Grande (LLM).
# En una aplicación real, esto haría una petición a una API de un servicio de IA.
# Para este ejemplo, la respuesta se genera directamente aquí para simplificar.
def get_llm_response(prompt):
    """
    Simula una llamada a un LLM y devuelve una respuesta JSON estructurada.
    """
    # Un "router" simple basado en palabras clave en el prompt
    if "generar un cuestionario" in prompt.lower() or "generate a quiz" in prompt.lower():
        # Simula la respuesta JSON para un examen
        topic_start = prompt.find("sobre") + 6
        topic = prompt[topic_start:].strip()
        
        quiz_data = {
            "type": "quiz",
            "title": f"Examen sobre: {topic.capitalize()}",
            "questions": [
                {
                    "question": "Which of the following is a personal pronoun?",
                    "options": ["Run", "She", "Quickly", "The"],
                    "answer": "She"
                },
                {
                    "question": "What is the possessive pronoun for 'they'?",
                    "options": ["Them", "Their", "Theirs", "Those"],
                    "answer": "Theirs"
                },
                {
                    "question": "Choose the correct sentence:",
                    "options": ["Her drives a car.", "She drive a car.", "She drives a car.", "Her drive a car."],
                    "answer": "She drives a car."
                },
                {
                    "question": "Which word is an article?",
                    "options": ["Under", "An", "Is", "Happy"],
                    "answer": "An"
                }
            ]
        }
        # Un LLM real generaría 10 preguntas. Aquí usamos un ejemplo más corto.
        return jsonify(quiz_data)

    else:
        # Simula la respuesta JSON para una explicación gramatical
        topic = "".join(prompt.split("'")[1::2]) # Extrae el tema del prompt
        explanation_data = {
            "type": "explanation",
            "title": f"Ejemplos de: {topic.capitalize()}",
            "content": [
                {"en": "I", "es": "Yo"},
                {"en": "You", "es": "Tú / Usted"},
                {"en": "He", "es": "Él"},
                {"en": "She", "es": "Ella"},
                {"en": "It", "es": "Ello (para cosas/animales)"},
                {"en": "We", "es": "Nosotros/as"},
                {"en": "They", "es": "Ellos/as"}
            ]
        }
        return jsonify(explanation_data)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_query = request.json.get('query', '')
    if not user_query:
        return jsonify({"error": "No query provided"}), 400
    
    prompt = f"El usuario quiere aprender sobre gramática inglesa. Su pregunta es: '{user_query}'. Proporciona una lista simple de ejemplos en inglés y sus traducciones al español."
    
    response = get_llm_response(prompt)
    return response

@app.route('/quiz', methods=['POST'])
def quiz():
    topic = request.json.get('topic', '')
    if not topic:
        return jsonify({"error": "No topic provided"}), 400

    prompt = f"Generar un cuestionario de 10 preguntas de opción múltiple sobre el tema de gramática inglesa: '{topic}'. Indica la respuesta correcta."

    response = get_llm_response(prompt)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
