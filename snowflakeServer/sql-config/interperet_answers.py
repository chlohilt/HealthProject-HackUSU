def interperet_answers(answers, correlation_functions, correlation_coefficients):
    sum = 0
    for i in range(len(answers)):
        value = correlation_functions[i](answers[i])
        if value > 100:
            value = 100
        elif value < 0:
            value = 0
        sum += value
    return sum / len(answers)
