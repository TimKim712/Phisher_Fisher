from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_restx import Api, Resource
from sympy import content
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline


app = Flask(__name__)
CORS(app)
# model_path = 'test'
# model = AutoModelForSequenceClassification.from_pretrained(model_path)
# tokenizer = AutoTokenizer.from_pretrained(model_path)
# model_pipeline = pipeline('text-classification', model=model, tokenizer=tokenizer)

@app.route('/test', methods = ['POST'])
def test():
    data = request.get_json()
    print(data)
    if data and 'message' in data:
        return jsonify({
            'message': data['message']
        }),200


# @app.route('/predict', methods=['GET'])
# def predict():
#     data = request.json
#     if not data or 'text' not in data:
#         return jsonify({'error': 'Invalid input'}),400
    
#     text = data['text']
#     result = model_pipeline(text)[0]
#     return jsonify({'result':result['label'],
#                     'confidence':result['score']
#                     })
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)