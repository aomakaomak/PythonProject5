from src.transaction_counter import transaction_count


def test_transaction_count(trans_count, get_categories):
    assert transaction_count(trans_count, get_categories) == {
        "Оплата за коммуналку": 2,
        "Перевод организации": 1,
    }


def test_transaction_count_empty(trans_count):
    assert transaction_count(trans_count, []) == {}


def test_transaction_count_wrong_cat(trans_count):
    assert (
        transaction_count(trans_count, ["Нет такой категории", "И такой тоже нет"])
        == {}
    )
