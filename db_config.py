import mysql.connector as sql
def get_connection():
    return sql.connect(user='root',host='localhost',passwd='',database='user_p')