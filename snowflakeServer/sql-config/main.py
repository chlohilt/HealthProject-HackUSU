from get_predictors import get_predictors
from get_data import connect_to_snowflake
def main():
    predictors, functions, correlation_coefficients = get_predictors(*connect_to_snowflake())
    print(predictors)
    print(functions[0](1))

if __name__ == "__main__":
    main()