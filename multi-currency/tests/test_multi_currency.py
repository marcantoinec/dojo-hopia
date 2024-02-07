from multi_currency.price import Price


def test_equal_dollar():
    assert Price(1, "USD") == Price(1, "USD")


def test_not_equal_different_currencies():
    assert Price(1, "EUR") != Price(1, "USD")


def test_add_same_currencies():
    assert Price(2, "EUR") == Price(1, "EUR") + Price(1, "EUR")


def test_mult_same_currencies():
    assert Price(2, "EUR") == 2 * Price(1, "EUR")
    assert Price(2, "EUR") == Price(1, "EUR") * 2


def test_conversion_rate_2():  # 1 EUR = 2 USD
    assert Price(1, "USD").convert_to("EUR") == Price(0.5, "EUR")


def test_add_different_currencies():
    assert Price(1, "USD") + Price(1, "EUR") == Price(3, "USD")
    assert Price(1, "USD") + Price(1, "EUR") == Price(1.5, "EUR")
