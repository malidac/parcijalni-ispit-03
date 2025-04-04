import sqlite3



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

# CREATE
    # CREATE CUSTOMER

    # CREATE OFFER

    # CREATE PRODUCT

    # CREATE PRODUCT_ITEM

# GET
    # GET CUSTOMER

    # GET OFFER

    # GET PRODUCT

    # GET PRODUCT_ITEM

# GET_ALL
    # GET_ALL CUSTOMERS

    # GET_ALL OFFERS

    # GET_ALL PRODUCTS

    # GET_ALL PRODUCT_ITEMS

# UPDATE
    # UPDATE CUSTOMER

    # UPDATE OFFER

    # UPDATE PRODUCT

    # UPDATE PRODUCT_ITEM

# DELETE
    # DELETE CUSTOMER

    # DELETE OFFER

    # DELETE PRODUCT

    # DELETE PRODUCT_ITEM

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
