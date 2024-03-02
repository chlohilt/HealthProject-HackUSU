from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample questions; in practice, these might come from a database or another data source.
questions = [
    {"id": 1, "text": "How confident are you in your problem-solving skills?"},
    {"id": 2, "text": "Rate your communication skills."},
    {"id": 3, "text": "How would you rate your teamwork abilities?"}
]

@app.route('/get-questions', methods=['GET'])
def get_questions():
    return jsonify(questions)

@app.route('/calculate-percentage', methods=['POST'])
def calculate_percentage():
    answers = request.json['answers']
    total_score = sum(answers.values())
    max_score = len(answers) * 10
    percentage = (total_score / max_score) * 100
    return jsonify({"percentage": round(percentage, 2)})

if __name__ == '__main__':
    app.run(debug=True, port=5700)