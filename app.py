
from flask import Flask, render_template, request, jsonify
from utils.chat_handler import ask_ai
from utils.image_gen import generate_image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    response = ask_ai(user_input)
    return jsonify({'response': response})

@app.route('/generate-image', methods=['POST'])
def image():
    prompt = request.json['prompt']
    url = generate_image(prompt)
    return jsonify({'image_url': url})

if __name__ == '__main__':
    app.run(debug=True)
