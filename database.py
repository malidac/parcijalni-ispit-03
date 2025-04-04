import sqlite3
from typing import Tuple



#region SQL Queries

create_customer_table = '''
CREATE TABLE IF NOT EXISTS customers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    vat_id TEXT NOT NULL
);
'''
create_product_table = '''
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NULL,
    price FLOAT NOT NULL
);
'''
create_product_item_table = '''
CREATE TABLE IF NOT EXISTS product_items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NULL,
    quantity FLOAT NOT NULL,

    offer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,

    FOREIGN KEY (offer_id) REFERENCES offers (id),
    FOREIGN KEY (product_id) REFERENCES products (id)
);
'''
create_offer_table = '''
CREATE TABLE IF NOT EXISTS offers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    offer_number INTEGER NOT NULL,
    date TEXT NOT NULL,
    tax FLOAT NOT NULL
);
'''


def commit_in_db(query: str, params: Tuple = ()):
    try:
        with sqlite3.connect('db.sqlite3') as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
    except Exception as ex:
        print(f'Dogodila se greska {ex}')

def fetchall_from_db(query: str, params: Tuple = ()):
    try:
        with sqlite3.connect('db.sqlite3') as conn:
            cursor = conn.cursor()
            # params -> ako ima samo jednu vrijednost (npr id) -> (1,)
            # params -> ako ima vise vrijednosti (npr objekt) -> (1, 2, 3) ili (1, 2, 3,)
            cursor.execute(query, params)
            return cursor.fetchall()
    except Exception as ex:
        print(f'Dogodila se greska {ex}')


# CREATE
# CREATE CUSTOMER
create_customer_str = '''
INSERT INTO customers(offer_number, email, vat_id) VALUES(?, ?, ?)
'''
def create_customer(customer: Tuple):
    commit_in_db(create_customer_str, customer)

# CREATE OFFER
create_offer_str = '''
INSERT INTO offers(name, date, tax) VALUES(?, ?, ?)
'''
def create_offer(offer: Tuple):
    commit_in_db(create_offer_str, offer)

# CREATE PRODUCT
create_product_str = '''
INSERT INTO products(name, description, price) VALUES(?, ?, ?)
'''
def create_offer(product: Tuple):
    commit_in_db(create_product_str, product)

# CREATE PRODUCT_ITEM
create_product_item_str = '''
INSERT INTO product_items(name, description, quantity, offer_id, product_id) VALUES(?, ?, ?, ?, ?)
'''
def create_product_item(product_item: Tuple):
    commit_in_db(create_product_item_str, product_item)


# GET
# GET CUSTOMER
get_customer_str = '''
SELECT * FROM customers WHERE id = ?
'''
def get_customer(customer_id: Tuple):
    fetchall_from_db(get_customer_str, customer_id)

# GET OFFER
get_offer_str = '''
SELECT * FROM offers WHERE id = ?
'''
def get_offer(offer_id: Tuple): # (1,) - offer s id = 1
    fetchall_from_db(get_offer_str, offer_id)

# GET PRODUCT
get_product_str = '''
SELECT * FROM products WHERE id = ?
'''
def get_product(product_id: Tuple):
    fetchall_from_db(get_product_str, product_id)

# GET PRODUCT_ITEM
get_product_item_str = '''
SELECT * FROM product_items WHERE id = ?
'''
def get_product_item(product_item_id: Tuple):
    fetchall_from_db(get_product_item_str, product_item_id)


# GET_ALL
# GET_ALL CUSTOMERS
get_customers_str = '''
SELECT * FROM customers
'''
def get_customers():
    fetchall_from_db(get_customers_str)

# GET_ALL OFFERS
get_offers_str = '''
SELECT * FROM offers
'''
def get_offers():
    fetchall_from_db(get_offers_str)

# GET_ALL PRODUCTS
get_products_str = '''
SELECT * FROM products
'''
def get_products():
    fetchall_from_db(get_products_str)

# GET_ALL PRODUCT_ITEMS
get_product_items_str = '''
SELECT * FROM product_items
'''
def get_product_items():
    fetchall_from_db(get_product_items_str)


# UPDATE
# UPDATE CUSTOMER
update_customer_str = '''
UPDATE customers
SET offer_number = ?,
SET email = ?,
SET vat_id = ?

WHERE id = ?
'''
def update_customer(customer: Tuple):
    commit_in_db(update_customer_str, customer)

# UPDATE OFFER
update_offer_str = '''
UPDATE offers
SET name = ?,
SET date = ?,
SET tax = ?

WHERE id = ?
'''
def update_offer(offer: Tuple):
    commit_in_db(update_offer_str, offer)

# UPDATE PRODUCT
update_product_str = '''
UPDATE products
SET name = ?,
SET description = ?,
SET price = ?

WHERE id = ?
'''
def update_product(product: Tuple):
    commit_in_db(update_product_str, product)

# UPDATE PRODUCT_ITEM
update_product_item_str = '''
UPDATE products
SET name = ?,
SET description = ?,
SET quantity = ?,
SET offer_id = ?,
SET product_id = ?

WHERE id = ?
'''
def update_product_item(product_item: Tuple):
    commit_in_db(update_product_item_str, product_item)

# DELETE
# DELETE CUSTOMER
delete_customer_str = '''
DELETE customers WHERE id = ?
'''
def delete_customer(customer_id: Tuple):
    commit_in_db(delete_customer_str, customer_id)

# DELETE OFFER
delete_offer_str = '''
DELETE offers WHERE id = ?
'''
def delete_offer(offer_id: Tuple):
    commit_in_db(delete_offer_str, offer_id)

# DELETE PRODUCT
delete_product_str = '''
DELETE products WHERE id = ?
'''
def delete_product(product_id: Tuple):
    commit_in_db(delete_product_str, product_id)

# DELETE PRODUCT_ITEM
delete_product_item_str = '''
DELETE product_items WHERE id = ?
'''
def delete_product_item(product_item_id: Tuple):
    commit_in_db(delete_product_item_str, product_item_id)

#endregion


# conn = sqlite3.connect('db.sqlite3')
# conn.close()
def create_db():
    try:
        with sqlite3.connect('db.sqlite3') as conn:
            cursor = conn.cursor()

            cursor.execute(create_customer_table)
            cursor.execute(create_product_table)
            cursor.execute(create_offer_table)
            cursor.execute(create_product_item_table)

            conn.commit()
    except Exception as ex:
        print(f'Dogodila se greska {ex}')

