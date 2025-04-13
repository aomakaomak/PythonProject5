from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(user_input: str) -> str:
    """Функция универсальной маскировки номера счета либо карты"""
    list_user_input = user_input.split()
    string = ""

    if len(user_input) == 0 or user_input.isalpha():
        return "Введите номер счета или карты"
    elif "Счет" in user_input:
        for i in range(0, len(list_user_input)):
            if list_user_input[i].isdigit():
                list_user_input[i] = get_mask_account(list_user_input[i])
    else:
        for i in range(0, len(list_user_input)):
            if list_user_input[i].isdigit():
                list_user_input[i] = get_mask_card_number(list_user_input[i])
    string = " ".join(list_user_input)
    return string


def get_date(date_input: str) -> str:
    """Функция преобразования даты"""
    if len(date_input) == 0:
        return "Введите дату"
    else:
        date_formatted = f"{date_input[8:10]}.{date_input[5:7]}.{date_input[0:4]}"
        return date_formatted
