from models.product import Product


class Drink(Product):
    def __init__(self, id, name, prod_type, price, alcoholic=False):
        super(Drink, self).__init__(id, name, prod_type=prod_type, price=price)
        self.alcoholic = alcoholic

    def to_dict(self):
        res = super(Drink, self).to_dict()
        res['alcoholic'] = self.alcoholic

        return res