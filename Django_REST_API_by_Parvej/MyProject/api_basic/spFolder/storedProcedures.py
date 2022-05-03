from django.db import connection
import pyodbc


def databaseConnection():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=INPC0STGBC\MSSQL2017;'
                          'Database=apiParvezDB;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()

    return cursor


def Insert_Article_Comment(id, comments):
    cursor = databaseConnection()
    savedid = str(id)

    sql = "EXEC [dbo].[Insert_Article_Comment] @articleId=?, @comments=?"
    params = (savedid, comments)
    cursor.execute(sql, params)

    cursor.commit()
