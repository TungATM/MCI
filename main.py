import pandas as pd
import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ADMIN\SQLEXPRESS;'
                      'Database=DeThiThu;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

sql_query = pd.read_sql_query('SELECT * FROM DeThiThu.dbo.DeTai',conn)
print(sql_query)
print(type(sql_query))
sql_query.info()
