class Product(object):
    def __init__(self, id, name, prod_type, price):
        self.id = id
        self.name = name
        self.prod_type = prod_type
        self.price = price

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'prod_type': self.prod_type,
            'price': self.price
        }
