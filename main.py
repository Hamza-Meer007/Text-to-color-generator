# app.py
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import numpy as np
from tensorflow import keras
from tensorflow.keras.utils import to_categorical
import json
from tensorflow.keras.preprocessing.text import tokenizer_from_json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


# Load the tokenizer from JSON
with open('tokenizer.json', 'r') as f:
    tokenizer_config = json.load(f)
t = tokenizer_from_json(tokenizer_config)


max_len = 25
num_classes = len(t.word_index)+1


model = keras.models.Sequential([
    keras.layers.LSTM(256,return_sequences=True,input_shape = (max_len,num_classes)),
    keras.layers.LSTM(512),
    keras.layers.Dense(64,activation='relu'),
    keras.layers.Dense(32,activation='relu'),
    keras.layers.Dense(3,activation='sigmoid')]
)
model.load_weights('model.h5', by_name=True)

def scale(n):
    return int(n * 255)

@app.route('/generate_color', methods=['POST'])
def generate_color():
    try:
        # Get input from request
        
        data = request.get_json()
        name = data['text'].lower()
        
        # Preprocess input (same as original)
     
        name = name.lower()
        tokenized = t.texts_to_sequences([name])
        padded = keras.preprocessing.sequence.pad_sequences(tokenized, maxlen=max_len)
        one_hot = to_categorical(padded, num_classes=num_classes)
        pred = model.predict(np.array(one_hot))[0]
        r, g, b = scale(pred[0]), scale(pred[1]), scale(pred[2])
        print(name + ',', 'R,G,B:', r,g,b)
        
        # Convert to HEX
        hex_color = f"#{r:02x}{g:02x}{b:02x}".upper()
        
        return jsonify({
            "r": r,
            "g": g,
            "b": b,
            "hex": hex_color,
            "status": "success"
        }), 200
        
    except Exception as e:
        print(e)
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

# Serve frontend
@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)