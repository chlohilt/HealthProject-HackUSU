from flask import Flask, request, jsonify
from flask_cors import CORS
from get_predictors import get_predictors
from get_data import connect_to_snowflake
from interpret_answers import interpret_answers

app = Flask(__name__)
CORS(app, origins="*")

predictors, functions, correlation_coefficients = get_predictors(*connect_to_snowflake())

questions = []
for x in predictors:
    x = x.split('_')
    x.pop()
    x.pop(0)
    items_before_last = x[:-1]
    result = " ".join(items_before_last)
    if "STAR" in result:
        result = result.replace("STAR", "")

    question = ''
    type = ''
    if x[len(x)-1] == 'CENTILE' or x[len(x)-1] == 'METRIC':
        question = 'Rate your ' + result.lower() + ' on a scale from 1 to 100'
        type = 'centile'
    else:
        if x[len(x) - 1] == 'RANK':
            continue
        else:
            question = 'Do you experience ' + result.lower() + '? (Y/N)'
            type = 'yesOrNo'

    if question != '':
        questions.append({"id": items_before_last, "text": question, "type": type})


@app.route('/get-questions', methods=['GET'])
def get_questions():
    return jsonify(questions)


@app.route('/calculate-percentage', methods=['POST'])
def calculate_percentage():
    answers = request.json['answers']
    percentage, top_3_answers = interpret_answers(answers, functions, correlation_coefficients)
    for answer in top_3_answers:
        answer.lower()
    return jsonify({"percentage": round(percentage, 2), "top_3_list": top_3_answers})

if __name__ == '__main__':
    app.run(debug=True, port=5700)
