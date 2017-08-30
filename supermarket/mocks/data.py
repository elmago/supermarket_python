from models.drink import Drink
from models.food import Food
from models.supermaket import Supermarket

supermakets_mock = []
products_mock = []
prod_types = ('fast food', 'healthy food', 'alcoholic drink', 'soda')

supermarket_new_id = 0
product_new_id = 0


def generate_id(return_supermarket_id=False):
    """
    This function simulates a database autoincremental id generation
    """
    global supermarket_new_id, product_new_id
    while True:
        if return_supermarket_id:
            supermarket_new_id += 1
            yield supermarket_new_id
        else:
            product_new_id += 1
            yield product_new_id


def load_data():
    # Load products
    products_mock.append(Food(generate_id().next(), 'hamburger', prod_types[0],
                              5, 1))
    products_mock.append(Food(generate_id().next(), 'french fries',
                              prod_types[0], 3, 50))
    products_mock.append(Food(generate_id().next(), 'pizza', prod_types[0], 5,
                              1))
    products_mock.append(Food(generate_id().next(), 'soup', prod_types[1], 1,
                              1))
    products_mock.append(Drink(generate_id().next(), 'whisky', prod_types[2],
                               50, True))
    products_mock.append(Drink(generate_id().next(), 'wine', prod_types[2], 40,
                               True))
    products_mock.append(Drink(generate_id().next(), 'coke', prod_types[3], 1))
    products_mock.append(Drink(generate_id().next(), 'pepsi', prod_types[3], 1))

    # Load supermarkets
    supermakets_mock.append(Supermarket(
        generate_id(True).next(), 'SimpsonMarket', '742 Evergreen Terrace'))
    supermakets_mock.append(Supermarket(
        generate_id(True).next(), 'Kwik-E-Mart', '1203 Evergreen Terrace'))

    supermakets_mock[0].add_products(
        products_mock[0], products_mock[1], products_mock[2], products_mock[3])
    supermakets_mock[1].add_products(
        products_mock[4], products_mock[5], products_mock[6], products_mock[7])


load_data()