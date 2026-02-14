import mysql.connector
import pandas as pd
# connect to MySQL
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="world",
    port=3306
)

print(pd.read_sql_query("SELECT * FROM countrylanguage",conn))
