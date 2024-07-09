from snowflake.snowpark.session import Session
from snowflake.snowpark.dataframe import col, DataFrame
from snowflake.snowpark.functions import udf
from src import functions

def run(snowpark_session: Session) -> DataFrame:
    """
    A sample stored procedure which creates a small DataFrame, prints it to the
    console, and returns the number of rows in the table.
    """
    snowpark_session.sql("use database CBA_CODECHALLENGE")
    df_table = session.table("public.ELECTRIC_CHARGEPOINTS_2017")

    df_sql = session.sql("""SELECT a.* from public.ELECTRIC_CHARGEPOINTS_2017 a
                            WHERE a.PLUGINDURATION = (select max(b.PLUGINDURATION) from public.ELECTRIC_CHARGEPOINTS_2017 b )
                         """)
    
    return df_sql 

if __name__ == "__main__":
    # This entrypoint is used for local development (`$ python src/procs/app.py`)

    from src.util.local import get_env_var_config

    print("Creating session...")
    session = Session.builder.configs(get_env_var_config()).create()
    session.add_import(functions.__file__, 'src.functions')
    
    
    print("Running stored procedure...")
    result = run(session)

    print("Stored procedure complete:")
    result.show()
    
    result.write.mode("overwrite").save_as_table("public.max_pluginduration")
