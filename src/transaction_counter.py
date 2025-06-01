from collections import Counter


def transaction_count(transactions: list[dict], list_category: list[str]) -> dict:
    """
    Принимает список словарей с данными о банковских операциях и список категорий
    операций, а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории
    """
    categories_for_count = []
    for category in list_category:
        for transaction in transactions:
            if category == transaction["description"]:
                categories_for_count.append(category)
    counted = dict(Counter(categories_for_count))
    return counted
