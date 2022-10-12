from db_functions import read_from_db, execute_query, insert_product

# my_query = """
#             SELECT * FROM products
#         """

# result = read_from_db(my_query)
# for row in result:
#     print("product price:", float(row['price']),)





# my_insert_query = """
#     INSERT INTO products (name, price)
#     VALUES 
#         ("Pepsi", 1.1),
#         ("Coke Zero", 1.2);
# """

# execute_query(my_insert_query)





product_name = "Sushi"
product_price = 10.8

insert_product(product_name, product_price)
