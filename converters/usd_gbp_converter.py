from converters import CurrencyConverter

class UsdGbpConverter(CurrencyConverter):
    def __init__(self):
        super().__init__()
        self.gbp_rate = self.rates['GBP']
    def convert(self, amount):
        return amount * self.gbp_rate