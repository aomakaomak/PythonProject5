import pytest
from src.masks import get_mask_card_number


@pytest.mark.parametrize('value, expected', [
    (7000792289606361, "7000 79** **** 6361"),
    ("dksjfljfsfdfsfs", "Ошибка. Пожалуйста, введите номер карты"),
    (829834847, "Слишком короткий номер карты")
])
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected