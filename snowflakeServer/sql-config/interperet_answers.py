def interperet_answers(answers, correlation_functions, correlation_coefficients):
    sum = 0
    for i in range(len(answers)):
        sum += correlation_functions[i](answers[i])
    return sum / len(answers)
