import numpy as np

bad_columns = ["HWD_WELLTH_GENERATION_CODE_V7", "HWD_WELLTH_ABILITY_TO_PAY_V7", "HWD_WELLTH_V7"]

def get_predictors(column_names, rows, trait):
    # column_names: list of column names from the table
    # rows: list of tuples, each index within the tuples correlates to the column name at the same index
    # trait: string that matches a column name. This is the trait we are focusing on and looking for predictors of
    predictors = []
    weighted_sums = {}

    for i in range(len(column_names)):
        curr_trait = [row[column_names.index(trait)] for row in rows]
        values_popped = 0
        column = column_names[i]
        if column in bad_columns:
            continue
        # check that we're not comparing the trait to itself
        if column == trait or column == "PID":
            continue
        curr_col = []
        for j in range(len(rows)):
            curr_val = rows[j][i]
            if curr_val is None:
                curr_trait.pop(j - values_popped)
                values_popped += 1
                continue
            elif curr_val == 'Y':
                curr_val = 1
                curr_col.append(curr_val)
            elif curr_val == 'N':
                curr_val = 0
                curr_col.append(curr_val)
            else:
                curr_val = int(curr_val)
                curr_col.append(curr_val)
        if len(curr_col) <= 1 or np.std(curr_trait) == 0:
            bad_columns.append(column)
            continue
        correlation_coefficient = np.corrcoef(curr_col, curr_trait)[0, 1]
        if np.isnan(correlation_coefficient):
            print("nan", i, j)
        if abs(correlation_coefficient) > .9:
            predictors.append(column)
            # weight = abs(correlation_coefficient)
            # weighted_sum = weight * np.corrcoef(curr_col, curr_trait)[0, 1]
            # weighted_sums[column] = weighted_sum
    return predictors

def main():
    test_columns = ["obesity", "exercise"]
    test_rows = [(10, 2), (2, 7), (3, 5), (3, 6)]
    print(get_predictors(test_columns, test_rows, "obesity"))

if __name__ == "__main__":
    main()
