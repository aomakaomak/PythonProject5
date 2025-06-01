import pytest
from src.search_description import search_in_description

def test_search_in_description(search_into_description):
    assert search_in_description(search_into_description, "Перевод") == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод физическому лицу', 'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации для различных нужд', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}]


def test_search_in_description_empty():
    assert search_in_description([], "Перевод") == []

