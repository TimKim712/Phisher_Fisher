from flask import Flask, request, jsonify
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

# Initialize Flask app
app = Flask(__name__)

# Load the model and tokenizer
MODEL_PATH = "../model/saved_model"
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)


@app.route('/test', methods=['POST'])
def test():
    data = request.get_json()
    print(data)
    if data and 'message' in data:
        return jsonify({
            'message': data['message']
        }), 200


@app.route("/predict", methods=["POST"])
def predict():
    # Get input data (JSON payload)
    data = request.json
    if not data or "message" not in data:
        return jsonify({"error": "Invalid input. Please provide 'message' field."}), 400

    input_text = data["message"]

    # Tokenize the input
    inputs = tokenizer(input_text, return_tensors="pt",
                       truncation=True, padding=True)

    # Make prediction
    with torch.no_grad():
        outputs = model(**inputs)
        scores = torch.softmax(outputs.logits, dim=1).tolist()[0]

    # Prepare the result
    predicted_result = "Phishing" if scores[1] > scores[0] else "Innocent"
    confidence = str(round(
        100*scores[1]))+'%' if predicted_result == "Phishing" else str(round(100*scores[0]))+'%'
    return jsonify({
        "input": input_text,
        "result": predicted_result,
        "confidence": confidence,
    })


if __name__ == "__main__":
    app.run(debug=True)
