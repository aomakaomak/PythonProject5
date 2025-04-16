import pytest
from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator,
)

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 142264287,
        "state": "CANCELED",
        "date": "2019-05-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79614.93",
            "currency": {"name": "EUR", "code": "EUR"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
]


def test_filter_by_currency_usd(currency_usd):
    generator = filter_by_currency(transactions, "USD")
    assert list(generator) == currency_usd


def test_filter_by_currency_eur(currency_eur):
    generator = filter_by_currency(transactions, "EUR")
    assert list(generator) == currency_eur


def test_filter_by_currency_empty_list():
    empty_list = []
    generator = filter_by_currency(empty_list, "EUR")
    assert list(generator) == []


def test_filter_by_currency_rub():
    generator = filter_by_currency(transactions, "RUB")
    assert list(generator) == []


def test_transaction_descriptions():
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"


def test_transaction_descriptions_empty():
    empty_list = []
    generator = transaction_descriptions(empty_list)
    assert next(generator) == []


def test_card_number_generator_1():
    generator = card_number_generator(100, 103)
    assert next(generator) == "0000 0000 0000 0100"
    assert next(generator) == "0000 0000 0000 0101"
    assert next(generator) == "0000 0000 0000 0102"


def test_card_number_generator_2():
    generator = card_number_generator(10093730, 94389384844)
    assert next(generator) == "0000 0000 1009 3730"
    assert next(generator) == "0000 0000 1009 3731"
    assert next(generator) == "0000 0000 1009 3732"


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (99999999999999999, 999999999999999999, "Вы вышли за диапазон значений"),
        (0, 99999999999999999999999, "Вы вышли за диапазон значений"),
        (-15, 9999999, "Вы вышли за диапазон значений"),
        (10, 5, "Старт должен быть меньше стопа"),
        (None, None, "Введите 2 числа"),
    ],
)
def test_card_number_generator_max(start, stop, expected):
    generator = card_number_generator(start, stop)
    assert next(generator) == expected
