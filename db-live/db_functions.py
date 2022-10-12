import pymysql
from pymysql.constants import CLIENT
import os
from dotenv import load_dotenv


load_dotenv()

host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")


def create_connection():
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        cursorclass=pymysql.cursors.DictCursor,
        # autocommit=True # False
    )
    
    return connection


def read_from_db(query):
    conn = create_connection()

    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return result


def execute_query(query):
    conn = create_connection()

    with conn.cursor() as cursor:
        cursor.execute(query)
        conn.commit()


def insert_product(product_name, product_price):
    query = f"""
        INSERT INTO products (name, price)
        VALUES  ('{product_name}', {product_price}) 
    """
    execute_query(query)
