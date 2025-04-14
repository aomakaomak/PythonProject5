import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 32984925828374", "Счет **8374"),
        ("Счет", "Введите номер счета или карты"),
        ("", "Введите номер счета или карты"),
    ],
)
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("", "Введите дату"),
        # ("Счет", "Введите номер счета или карты"),
    ],
)
def test_get_date(value, expected):
    assert get_date(value) == expected
