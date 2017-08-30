from mocks.data import supermakets_mock, products_mock


class SupermarketService(object):
    @staticmethod
    def get_supermarkets(name):
        return [
            supermkt.to_dict()
            for supermkt in supermakets_mock
            if not name or supermkt.name == name
        ]

    @staticmethod
    def get_supermarket_products(name):
        try:
            smkt = (
                supermkt
                for supermkt in supermakets_mock
                if supermkt.name == name
            ).next()
        except StopIteration:
            return []

        return [
            prod.to_dict()
            for prod in smkt.products
        ]


class ProductService(object):
    @staticmethod
    def get_products(name):
        return [
            prod.to_dict()
            for prod in products_mock
            if not name or prod.name == name
        ]