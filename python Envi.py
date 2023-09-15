import pyodbc
connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
conn = pyodbc.connect(connectionString)
cur = conn.cursor()
result = cur.execute('SELECT * FROM company').fetchall()
conn.close()

def sql_query(sqlvar):
    connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
    conn = pyodbc.connect(connectionString)
    cur = conn.cursor()
    try:
       result = cur.execute(sqlvar)
    except Exception as e:
        print(e)
        result = None
    conn.commit()
    cur.close()
    return result

sqlqueryvar = "INSERT INTO salesperson (emp_no,first_name,last_name,dept_no,salary,sales_target,county,post_code,tel,notes) VALUES   (17, 'Keegan','C',2,30000,12,'Gtr Manchester','M1 1MM','0161616161','TRYYING to learn coding')"

insertresult = sql_query(sqlqueryvar)
print(insertresult)

sqlqueryvar = "UPDATE salesperson SET notes = tryning to learn code, salary = 10"
sql_query(sqlqueryvar) 

sql
CREATE TABLE Student ( StudentID int NOT NULL, FirstName nvarchar(40) NOT NULL, Surname nvarchar(30) NULL, Course nvarchar(30) NULL, City nvarchar(15) NULL )