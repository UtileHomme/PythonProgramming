
import pyodbc

def connection():
   conn = pyodbc.connect('Driver={SQL Server};'
                         'Server=INPC0STGBC\MSSQL2017;'
                         'Database=SIRISK;'
                         'Trusted_Connection=yes;')

   cursor = conn.cursor()
   cursor.execute("SELECT RequestID from Trans_RequestTracker_local")
   while 1:
       row = cursor.fetchone()
       if not row:
           break
       print(row.RequestID)
   cursor.close()

connection()