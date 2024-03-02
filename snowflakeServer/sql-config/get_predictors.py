import numpy as np
from scipy.stats import pearsonr

bad_columns = ["HWD_WELLTH_GENERATION_CODE_V7", "HWD_WELLTH_ABILITY_TO_PAY_V7", "HWD_WELLTH_V7"]

def get_predictors(column_names, rows, trait):
    # column_names: list of column names from the table
    # rows: list of tuples, each index within the tuples correlates to the column name at the same index
    # trait: string that matches a column name. This is the trait we are focusing on and looking for predictors of
    predictors = []
    correlation_functions = []
    correlation_coefficients = []

    for i in range(len(column_names)):
        curr_trait = [row[column_names.index(trait)] for row in rows]
        values_popped = 0
        column = column_names[i]
        if column == "AGE":
            pass
        if column in bad_columns:
            continue
        # check that we're not comparing the trait to itself
        if column == trait or column == "PID":
            continue
        curr_col = []
        for j in range(len(rows)):
            if j == 93:
                pass
            curr_val = rows[j][i]
            if curr_val is None or curr_val == "X":
                curr_trait.pop(j - values_popped)
                values_popped += 1
                continue
            elif curr_val == 'Y' or curr_val == "F":
                curr_val = 1
                curr_col.append(curr_val)
            elif curr_val == 'N' or curr_val == "M":
                curr_val = 0
                curr_col.append(curr_val)
            else:
                curr_val = int(curr_val)
                curr_col.append(curr_val)
        if len(curr_col) <= 1 or np.std(curr_trait) == 0:
            bad_columns.append(column)
            continue
        correlation_coefficient, p_value = pearsonr(curr_col, curr_trait)
        if abs(correlation_coefficient) > .8 and p_value < 0.05:
            predictors.append(column)
            correlation_coefficients.append(correlation_coefficient)
            line_of_best_fit = np.polyfit(curr_col, curr_trait, 1)
            correlation_function = np.poly1d(line_of_best_fit)
            correlation_functions.append(correlation_function)
    for predictor in predictors:
        if "QUINTILE" in predictor:
            predictors.remove(predictor)
    return predictors, correlation_functions, correlation_coefficients

def main():
    test_columns = ["obesity", "exercise"]
    test_rows = [(10, 2), (2, 5), (3, 5), (3, 4)]
    predictors, functions, ccs = get_predictors(test_columns, test_rows, "obesity")
    print(predictors)
    print(functions[0](2))
if __name__ == "__main__":
    main()
