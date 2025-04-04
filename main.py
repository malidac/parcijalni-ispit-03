import json
from database import create_db
from services import UserService

from user_interface import (print_menu)


OFFERS_FILE = "offers.json"
PRODUCTS_FILE = "products.json"
CUSTOMERS_FILE = "customers.json"


def load_data(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Error decoding {filename}. Check file format.")
        return []


def main():
    offers = load_data(OFFERS_FILE)
    products = load_data(PRODUCTS_FILE)
    customers = load_data(CUSTOMERS_FILE)

    while True:
        print_menu(offers, products, customers)


if __name__ == "__main__":
    # create_db()
    # user_service = UserService(user_id=5)
    # print(user_service.user.name)
    main()
