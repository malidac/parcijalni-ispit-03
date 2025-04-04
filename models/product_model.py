class Product:
    def __init__(self,
                 id: int,
                 name: str,
                 description: str,
                 price: float):
        self.id = id
        self.name = name
        self.description = description
        self.price = price

    def create_customer(self):
        pass

    def get_customer(self):
        pass

    def update_customer(self):
        pass

    def delete_customer(self):
        pass


class ProductItem:
    def __init__(self,
                 product: Product = None,
                 quantity: float = 1):
        self.product = product
        self.quantity = quantity
        self.item_total = 0.00

        self.calculate_item_total()

    def calculate_item_total(self):
        if self.product != None:
            self.item_total = self.product.price * self.quantity

    def create_customer(self):
        pass

    def get_customer(self):
        pass

    def update_customer(self):
        pass

    def delete_customer(self):
        pass
