from flask import Flask, request, jsonify
from flask_cors import CORS


from interperet_answers import interperet_answers

app = Flask(__name__)
CORS(app)

questions = [
    {"id": 1, "text": "How confident are you in your problem-solving skills?"},
    {"id": 2, "text": "Rate your communication skills."},
    {"id": 3, "text": "How would you rate your teamwork abilities?"}
]

@app.route('/get-questions', methods=['GET'])
def get_questions():
    return jsonify(questions)


@app.route('/calculate-percentage', methods=['POST'])
def get_answers():
    answers = request.json['answers']
    percentage = interperet_answers(answers)
    return jsonify({"percentage": round(percentage, 2)})


if __name__ == '__main__':
    app.run(debug=True, port=5700)
