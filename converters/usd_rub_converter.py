from converters import CurrencyConverter

class UsdRubConverter(CurrencyConverter):
    def __init__(self):
        super().__init__()
        self.rub_rate = self.rates['RUB']
    def convert(self, amount):
        return amount * self.rub_rate