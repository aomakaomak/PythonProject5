import re


def search_in_description(transactions: list[dict], string: str) -> list[dict]:
    """
    Принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка.
    """
    pattern = re.compile(rf"{string}")
    new_transactions = []
    try:
        for transaction in transactions:
            if re.search(pattern, transaction["description"].lower()):
                new_transactions.append(transaction)
    except Exception as ex:
        raise KeyError(f"Возникла ошибка {ex}")

    return new_transactions


# my_transactions = [
#   {
#     "id": 441945886,
#     "state": "EXECUTED",
#     "date": "2019-08-26T10:50:58.294041",
#     "operationAmount": {
#       "amount": "31957.58",
#       "currency": {
#         "name": "руб.",
#         "code": "RUB"
#       }
#     },
#     "description": "Оплата за коммуналку",
#     "from": "Maestro 1596837868705199",
#     "to": "Счет 64686473678894779589"
#   },
#   {
#     "id": 41428829,
#     "state": "EXECUTED",
#     "date": "2019-07-03T18:35:29.512364",
#     "operationAmount": {
#       "amount": "8221.37",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод физическому лицу",
#     "from": "MasterCard 7158300734726758",
#     "to": "Счет 35383033474447895560"
#   },
#   {
#     "id": 939719570,
#     "state": "EXECUTED",
#     "date": "2018-06-30T02:08:58.425572",
#     "operationAmount": {
#       "amount": "9824.07",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     # "description": "Перевод организации для различных нужд",
#     "from": "Счет 75106830613657916952",
#     "to": "Счет 11776614605963066702"
#   }
# ]
#
# result = search_in_description(my_transactions, "Перевод")
#
# print(result)
