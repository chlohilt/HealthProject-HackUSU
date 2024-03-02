import snowflake.connector
import json

# Function to read Snowflake configuration from JSON file
def read_snowflake_config(file_path):
    with open(file_path, 'r') as config_file:
        return json.load(config_file)

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

# Use the specified database
use_database_query = f'USE DATABASE {snowflake_config["database"]}'
cursor.execute(use_database_query)

# Run a SELECT query on the HEALTHWISE360 table
select_query = 'SELECT * FROM your_schema.HEALTHWISE360 LIMIT 100'
cursor.execute(select_query)

# Fetch results
results = cursor.fetchall()

# Print results
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
con.close()
