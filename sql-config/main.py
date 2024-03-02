from snowflake.snowpark.session import Session

def snowflake_connector():
    try:
        session = Session.builder.configs(connection_parameters).create()
        print("connection successful!")
    except:
        raise ValueError("error while connecting with db")
    return session

#define a session
session = snowflake_connector()