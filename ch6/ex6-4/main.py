class Element():
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

    def __str__(self):
        return f"name={self.name}, symbol={self.symbol}, number={self.number}"


h = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}

hydrogen = Element(**h)
print(hydrogen)
