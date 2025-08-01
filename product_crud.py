from db_config import get_connection
def add_product(product,number,price):
    c=get_connection()
    try:
        cu=c.cursor()
        query='insert into product(product_name,number,price)values(%s,%s,%s)'
        prod=(product,number,price)
        cu1.execute(query,prod)
        print(f'product added with id {cu1.lastrowid}')
        c.commit()
    except Exception as e:
        c.rollback()
        print('product added error',e)
    finally:
        cu.close()
        c.close()

def delete_product(idd):
    c=get_connection()
    try:
        cu=c.cursor()
        cu.execute('delete from product where id=%s',(idd,))
        print(f'product deleted with id {idd}')
        c.commit()
    except Exception as e:
        c.rollback()
        print('product deleted error',e)
    finally:
        cu.close()
        c.close

def update_product(idd,newprice):
    c=get_connection()
    try:
        cu=c.cursor()
        cu.execute('update product set price=%s where id=%s',(newprice,idd,))
        print(f'product updated with id {idd}')
        c.commit()
    except Exception as e:
        c.rollback()
        print('product updated error',e)
    finally:
        cu.close()
        c.close()





