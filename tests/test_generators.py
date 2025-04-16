import pytest
from src.generators import filter_by_currency

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


def test_filter_by_currency_eur(currency_eur):
    assert (
        list(
            transactions[i]
            for i in range(0, len(transactions))
            if transactions[i]["operationAmount"]["currency"]["name"] == "EUR"
        )
        == currency_eur
    )


def test_filter_by_currency_usd(currency_usd):
    assert (
        list(
            transactions[i]
            for i in range(0, len(transactions))
            if transactions[i]["operationAmount"]["currency"]["name"] == "USD"
        )
        == currency_usd
    )
