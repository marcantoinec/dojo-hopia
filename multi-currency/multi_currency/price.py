class Price:
    def __init__(self, amount: float, currency: str):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other):
        return self._amount == other._amount and self._currency == other._currency

    def __add__(self, other):
        return Price(self._amount + other._amount, self._currency)

    def __rmul__(self, other):
        return Price(self._amount * other, self._currency)

    def __mul__(self, other):
        return other * self

    def convert_to(self, new_currency: str):
        rates = {("USD", "EUR"): 0.5, ("EUR", "USD"): 2}
        return Price(self._amount * rates[(self._currency, new_currency)], new_currency)

