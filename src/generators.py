from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator:
    """
    Функция, которая принимает список словарей (банковских операций)
    и название нужной валюты и выводит список операций с заданной валютой
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["name"] == currency:
            yield transaction
    # yield (
    #     transactions[i]
    #     for i in range(0, len(transactions))
    #     if transactions[i]["operationAmount"]["currency"]["name"] == currency
    # )


def transaction_descriptions(transactions: list[dict]) -> Iterator:
    """
    Функция, которая принимает список словарей (банковских операций)
    и выводит список операций поочередно
    """
    if transactions == []:
        yield transactions
    else:
        for transaction in transactions:
            yield transaction["description"]





# transactions = [
#     {
#         "id": 939719570,
#         "state": "EXECUTED",
#         "date": "2018-06-30T02:08:58.425572",
#         "operationAmount": {
#             "amount": "9824.07",
#             "currency": {"name": "USD", "code": "USD"},
#         },
#         "description": "Перевод организации",
#         "from": "Счет 75106830613657916952",
#         "to": "Счет 11776614605963066702",
#     },
#     {
#         "id": 142264268,
#         "state": "EXECUTED",
#         "date": "2019-04-04T23:20:05.206878",
#         "operationAmount": {
#             "amount": "79114.93",
#             "currency": {"name": "USD", "code": "USD"},
#         },
#         "description": "Перевод со счета на счет",
#         "from": "Счет 19708645243227258542",
#         "to": "Счет 75651667383060284188",
#     },
#     {
#         "id": 142264287,
#         "state": "CANCELED",
#         "date": "2019-05-04T23:20:05.206878",
#         "operationAmount": {
#             "amount": "79614.93",
#             "currency": {"name": "EUR", "code": "EUR"},
#         },
#         "description": "Перевод со счета на счет",
#         "from": "Счет 19708645243227258542",
#         "to": "Счет 75651667383060284188",
#     }
# ]



