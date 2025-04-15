from typing import Any, Callable, Iterable, Optional, Union


def filter_by_state(new_list: list[dict], user_state="EXECUTED") -> list[dict]:
    """Фуккция, которая выводит список словарей в зависимости от состояния"""
    filtered_list = []
    if len(new_list) == 0:
        return "Введите список"
    else:
        for dictionary in new_list:
            if dictionary["state"] == user_state:
                filtered_list.append(dictionary)
        return filtered_list


def sort_by_date(user_list: list[dict], decreasing=True) -> list[dict]:
    """Функция, которая сортирует словари в списке по дате"""
    if len(user_list) == 0:
        return "Введите список"
    else:
        sorted_by_day_list = sorted(
            user_list, reverse=decreasing, key=lambda x: x["date"]
        )
        return sorted_by_day_list
