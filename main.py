from db_utils import create_database, create_table
from product_crud import add_product, delete_product, update_product
from product_reports import product_pd, product_bar, product_pie
def main():
    while True:
        user=int(input('c_database=1 or c_table=2 or add_prod=3 or delete_prod=4 or update_prod=5 or prod_pd=6 or prod_bar=7 or prod_pie=8 or exit=0:'))
        if user==0:
            break
        elif user==1:
            create_database()
        elif user==2:
            create_table()
        elif user==3:
            product=input('enter product name:')
            number=int(input('enter product number:'))
            price=int(input('enter product price:'))
            add_product(product,number,price)
        elif user==4:
            idd=int(input('enter user id:'))
            delete_product(idd)
        elif user==5:
            idd=int(input('enter product id:'))
            newprice=int(input('enter product newprice:'))
            update_product(idd,newprice)
        elif user==6:
            product_pd()
        elif user==7:
            product_bar()
        elif user==8:
            product_pie()
if __name__=="__main__":
    main()
