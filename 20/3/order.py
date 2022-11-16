class Order:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return "Item: {}, price: {}".format(self._name, self.price())

    def __lt__(self, other):
        return self.price() < other.price()

    def __gt__(self, other):
        return self.price() > other.price()

    def __add__(self, other):
        return Order("{}+{}".format(self.item(), other.item()), self.price() + other.price())

    def price(self):
        return self._price

    def item(self):
        return self._name
