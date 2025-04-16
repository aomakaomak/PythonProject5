from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator:
    """
    Функция, которая принимает список словарей (банковских операций)
    и название нужной валюты и выводит список операций с заданной валютой
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["name"] == currency:
            yield transaction


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


def card_number_generator(start: int, stop: int) -> Iterator:
    """
    Функция генерации номеров банковских карт
    """
    if not start and not stop:
        yield "Введите 2 числа"
    elif start < 1 or stop > 9999999999999999:
        yield "Вы вышли за диапазон значений"
    elif start >= stop:
        yield "Старт должен быть меньше стопа"
    elif start >= 1 and stop <= 9999999999999999:
        for number in range(start, stop):
            str_number = str(number)  # преобразуем число в строку
            len_number = len(str_number)  # вычисляем длину строки-числа
            if len_number <= 16:
                len_zero = 16 - len_number  # вычисляем нужное количество нулей
                full_number = (
                    "0" * len_zero
                ) + str_number  # формируем строку пока без пробелов
                result = f"{full_number[0:4]} {full_number[4:8]} {full_number[8:12]} {full_number[12:]}"
                yield result
            else:
                yield "Вы вышли за диапазон значений"
