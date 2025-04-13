import asyncio
from converters import *

def main():    
    amount = int(input('Введите значение в USD: \n'))
    
    converter = UsdRubConverter()
    print(f"{amount} USD to RUB: {converter.convert(amount)}")
    
    converter = UsdEurConverter()
    print(f"{amount} USD to EUR: {converter.convert(amount)}")
    
    converter = UsdGbpConverter()
    print(f"{amount} USD to GBP: {converter.convert(amount)}")
    
    converter = UsdCnyConverter()
    print(f"{amount} USD to CNY: {converter.convert(amount)}")

if __name__ == "__main__":
    main()