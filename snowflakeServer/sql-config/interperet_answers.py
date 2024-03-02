def interperet_answers(answers, correlation_functions, correlation_coefficients):
    weighted_sum = 0
    for i in range(len(answers)):
        weighted_sum += correlation_functions[i](answers[i]) * correlation_coefficients[i]
    return weighted_sum