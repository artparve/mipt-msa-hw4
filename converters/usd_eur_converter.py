from converters import CurrencyConverter

class UsdEurConverter(CurrencyConverter):
    def __init__(self):
        super().__init__()
        self.eur_rate = self.rates['EUR']
    def convert(self, amount):
        return amount * self.eur_rate