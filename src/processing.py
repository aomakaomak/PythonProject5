from typing import Any, Callable, Iterable, Optional, Union


def filter_by_state(new_list: Iterable[Any], user_state="EXECUTED") -> Iterable:
    """Фуккция, которая выводит список словарей в записимости от состояния"""
    filtered_list = []
    for dictionary in new_list:
        if dictionary["state"] == user_state:
            filtered_list.append(dictionary)
    return filtered_list


# new_list = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
# ]
# print(filter_by_state(new_list))


def sort_by_date(user_list: Iterable[Any], decreasing=True) -> Iterable:
    sorted_by_day_list = sorted(user_list, reverse=decreasing, key=lambda x: x["date"])
    return sorted_by_day_list


# user_list = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
# ]
# print(sort_by_date(user_list))
