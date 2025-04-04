from typing import List
from datetime import datetime as dt

from models.customer_model import Customer
from models.product_model import Product


class Offer:
    def __init__(self,
                 offer_number: int,
                 date_str: str = dt.today().strftime('%Y-%m-%d %H:%M'),
                 customer: Customer = None,
                 items: List[Product] = []):
        self.offer_number = offer_number
        self.date_str = date_str
        self.date = None
        self.customer = customer
        self.items = items

        self.update_offer_date()

    def update_offer_date(self):
        self.date = dt.strptime(self.date_str, '%Y-%m-%d %H:%M')

    def create_customer(self):
        pass

    def get_customer(self):
        pass

    def update_customer(self):
        pass

    def delete_customer(self):
        pass
