import numpy as np

def get_predictors(column_names, rows, trait):
    # column_names: list of column names from the table
    # rows: list of tuples, each index within the tuples correlates to the column name at the same index
    # trait: string that matches a column name. This is the trait we are focusing on and looking for predictors of
    curr_trait = [row[column_names.index(trait)] for row in rows]
    predictors = []
    for i in range(len(column_names)):
        column = column_names[i]
        # check that we're not comparing the trait to itself
        if column == trait:
            continue
        curr_col = []
        for row in rows:
            try:
                curr_val = int(row[i])
                curr_col.append(curr_val)
            except ValueError:
                # if the value is NULL, it can't be compared
                if curr_val == None:
                    curr_trait.pop(i)
                elif curr_val == 'Y':
                    curr_val = 1
                    curr_col.append(curr_val)
                elif curr_val == 'N':
                    curr_val = 0
                    curr_col.append(curr_val)
        correlation_coefficient = np.corrcoef(curr_col, curr_trait)[0, 1]
        if abs(correlation_coefficient) > .7:
            predictors.append(f"column")
    return predictors

test_columns = ["obesity", "exercise"]
test_rows = [(10, 2), (2, 7), (3, 5), (3, 6)]
    

print(get_predictors(test_columns, test_rows, "obesity"))
