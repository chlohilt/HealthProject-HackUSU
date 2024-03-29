import snowflake.connector
import json


def read_snowflake_config(file_path):
    with open(file_path, 'r') as config_file:
        return json.load(config_file)


def connect_to_snowflake():
    # Snowflake configuration file path
    config_file_path = 'connection.json'

    # Read Snowflake connection parameters from the JSON file
    snowflake_config = read_snowflake_config(config_file_path)

    # Create a connection
    con = snowflake.connector.connect(
        user=snowflake_config['user'],
        password=snowflake_config['password'],
        account=snowflake_config['account'],
        warehouse=snowflake_config['warehouse'],
        database=snowflake_config['database'],
        schema=snowflake_config['schema'],
        role=snowflake_config['role']
    )

    # Create a cursor
    cursor = con.cursor()

    # Dynamically select the database name from snowflake_config
    database_name = snowflake_config['database']
    table1_name = snowflake_config['table']

    trait_column = "HWD_DIABETES_TYPE_2_CENTILE_V7"

    # Execute SQL queries with the dynamically selected database name
    cursor.execute(f"SHOW COLUMNS IN TABLE {database_name}.{table1_name}")
    columns = cursor.fetchall()
    column_names = [column[2] for column in columns]
    cursor.execute(f"SELECT * FROM {database_name}.{table1_name} WHERE {trait_column} IS NOT NULL;")
    # Fetch results
    results = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    con.close()

    return column_names, results, "HWD_DIABETES_TYPE_2_CENTILE_V7"
