from db_config import get_connection
def create_database():
    c=get_connection()
    try:
        cu=c.cursor()
        cu.execute("create database if not exists user_p")
        print('database created.')
    except Exception as e:
        c.rollback()
        print('error database',e)
    finally:
        cu.close()
        c.close()

def create_table():
    c=get_connection()
    try:
        cu=c.cursor()
        cu.execute("create table if not exists product(id int auto_increment primary key, product_name varchar(50), number int, price decimal(10,2))")
        print('table created.')
    except Exception as e:
        c.rollback()
        print('table error',e)
    finally:
        cu.close()
        c.close()



