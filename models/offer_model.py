from typing import List
from datetime import datetime as dt

from models.customer_model import Customer
from models.product_model import ProductItem


class Offer:
    def __init__(self,
                 offer_number: int,
                 date_str: str = dt.today().strftime('%Y-%m-%d %H:%M'),
                 customer: Customer = None,
                 items: List[ProductItem] = [],
                 tax: float = 25.0):
        self.offer_number = offer_number
        self.date_str = date_str
        self.date = None
        self.customer = customer
        self.items = items
        self.sub_total = 0.0
        self.tax = tax
        self.tax_value = 0.0
        self.total = 0.0

        self.update_offer_date()
        self.update_totals()

    def update_totals(self):
        if len(self.items) > 0:
            # for item in self.items:
            #     self.sub_total += item.item_total
            self.sub_total = sum([item.item_total for item in self.items])
        self.tax_value = self.sub_total * (self.tax / 100)
        self.total = self.tax_value + self.sub_total

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
