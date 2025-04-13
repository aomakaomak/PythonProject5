def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера карты"""
    string = str(card_number)
    if string.isdigit():
        return f"{string[0:4]} {string[4:6]}** **** {string[12:16]}"
    else:
        return "Ошибка. Пожалуйста, введите номер карты"


# card_number = 7000792289606361
# print(get_mask_card_number(card_number))


def get_mask_account(acount_number: str) -> str:
    """Функция маскировки расчетного счета"""
    string = str(acount_number)
    return f"**{string[-4:-1]}{string[-1]}"


# acount_number = 32984925828374
# print(get_mask_account(acount_number))
