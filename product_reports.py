from db_config import get_connection
import pandas as pd 
import matplotlib.pyplot as plt 
def product_pd():
    c=get_connection()
    df=pd.read_sql('select * from product',c)
    df['total_value']=df['number']*df['price']
    total_value_cal=df['total_value']
    print(f'total valuevcal:{total_value_cal}')

def product_bar():
    c=get_connection()
    df=pd.read_sql('select * from product',c)
    df['total_value']=df['number']*df['price']
    plt.bar(df['product_name'],df['price'])
    plt.show()

def product_pie():
    c=get_connection()
    df=pd.read_sql('select * from product',c)
    df['total_value']=df['number']*df['price']
    plt.pie(x=df['total_value'],labels=df['product_name'],autopct='%1.1f%%')
    plt.show()