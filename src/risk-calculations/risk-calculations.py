def get_diabetes_risk_recommendations(weighted_sums, top_n=5):
    # weighted_sums: a dictionary with column names as keys and their corresponding weighted sums as values
    # top_n: number of top predictors to recommend

    # Get user input for each predictor
    user_input = {}
    for predictor in weighted_sums.keys():
        user_value = float(input(f"Enter the value for {predictor}: "))
        user_input[predictor] = user_value

    # Calculate the impact of user input on diabetes risk
    user_impact = sum(weighted_sums[predictor] * user_input[predictor] for predictor in user_input.keys())

    # Get the top predictors to improve
    sorted_predictors = sorted(weighted_sums, key=lambda x: abs(weighted_sums[x]), reverse=True)
    top_predictors = sorted_predictors[:top_n]

    # Provide recommendations based on the user's input
    recommendations = {}
    for predictor in top_predictors:
        improvement_needed = user_impact / weighted_sums[predictor]
        recommendations[predictor] = improvement_needed

    return recommendations

# Example usage:
# Assuming weighted_sums is a dictionary containing the calculated weighted sums
user_recommendations = get_diabetes_risk_recommendations(weighted_sums)
print("Top 5 predictors to improve and the recommended improvement:")
for predictor, improvement_needed in user_recommendations.items():
    print(f"{predictor}: Improve by {improvement_needed}")