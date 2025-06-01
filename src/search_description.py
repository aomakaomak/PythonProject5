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
