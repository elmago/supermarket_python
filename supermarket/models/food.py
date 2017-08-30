from models.product import Product


class Food(Product):
    def __init__(self, id, name, prod_type, price, quantity=0):
        super(Food, self).__init__(id, name, prod_type=prod_type, price=price)
        self.quantity = quantity

    def to_dict(self):
        res = super(Food, self).to_dict()
        res['quantity'] = self.quantity

        return res
