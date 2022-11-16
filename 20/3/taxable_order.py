class TaxableOrder:
    def __init__(self, name, price, tax):
        self._name = name
        self._price = price
        self._tax = tax

    def __str__(self):
        return "Item: {}, price: {}".format(self._name, self.price())

    def __lt__(self, other):
        return self.price() < other.price()

    def __gt__(self, other):
        return self.price() > other.price()

    def price(self):
        return round(self._price * (1 + self._tax), 1)

    def item(self):
        return self._name
