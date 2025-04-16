def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера карты"""
    string = str(card_number)
    if not string.isdigit():
        return "Ошибка. Пожалуйста, введите номер карты"
    elif len(string) != 16:
        return "Неверный номер карты"
    else:
        return f"{string[0:4]} {string[4:6]}** **** {string[12:16]}"


def get_mask_account(acount_number: str) -> str:
    """Функция маскировки расчетного счета"""
    string = str(acount_number)
    if not string.isdigit():
        return "Ошибка. Пожалуйста, введите номер счета"
    elif len(string) != 14:
        return "Неверный номер счета"
    else:
        return f"**{string[-4:-1]}{string[-1]}"
