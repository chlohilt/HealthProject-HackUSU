def interpret_answers(responses, correlation_functions, correlation_coefficients):
    sum = 0
    answers = []
    questions = []
    for question, answer in responses.items():
        answers.append(answer)
        questions.append(question)

    weighted_values = []
    for i in range(len(answers)):
        value = correlation_functions[i](int(answers[i]))
        if value > 100:
            value = 100
        elif value < 0:
            value = 0
        sum += value
        weighted_values.append(correlation_coefficients[i] * value)

    sorted_list = sorted(weighted_values, reverse=True)
    top_3_values = sorted_list[:3]
    top_3_answers = [questions[weighted_values.index(value)] for value in top_3_values]
    top_3_answers = [x.replace(',', ' ').replace("STAR", "") for x in top_3_answers]
    
    print(top_3_answers)

    return (sum / len(answers), top_3_answers)
