from converters import CurrencyConverter

class UsdCnyConverter(CurrencyConverter):
    def __init__(self):
        super().__init__()
        self.cny_rate = self.rates['CNY']
    def convert(self, amount):
        return amount * self.cny_rate