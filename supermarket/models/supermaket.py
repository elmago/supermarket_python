class Supermarket(object):
    def __init__(self, id, name, address="Not given"):
        self.id = id
        self.name = name
        self.address = address
        self.products = []

    def add_products(self, *args):
        for prod in args:
            self.products.append(prod)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address
        }