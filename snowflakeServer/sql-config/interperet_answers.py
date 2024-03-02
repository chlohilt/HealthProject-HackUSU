def interperet_answers(answers, correlation_functions, correlation_coefficients):
    sum = 0
    values = [answer for _key, answer in answers.items()]
    for i in range(len(answers)):
        value = correlation_functions[i](values[i])
        if value > 100:
            value = 100
        elif value < 0:
            value = 0
        sum += value
    return sum / len(answers)
