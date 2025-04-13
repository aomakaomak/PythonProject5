import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "value, expected",
    [
        (7000792289606361, "7000 79** **** 6361"),
        ("dksjfljfsfdfsfs", "Ошибка. Пожалуйста, введите номер карты"),
        (829834847, "Неверный номер карты"),
    ],
)
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        (32984925828374, "**8374"),
        ("dksjfljfsfdfsfs", "Ошибка. Пожалуйста, введите номер счета"),
        (829834847, "Неверный номер счета"),
    ],
)
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected
