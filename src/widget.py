import masks

def mask_account_card(user_input: str) -> str:
    """Функция универсальной маскировки номера счета либо карты"""
    list_user_input = user_input.split()
    string = ""
    if "Счет" in user_input:
        for i in range(0, len(list_user_input)):
            if list_user_input[i].isdigit():
                list_user_input[i] = masks.get_mask_account(list_user_input[i])
    else:
        for i in range(0, len(list_user_input)):
            if list_user_input[i].isdigit():
                list_user_input[i] = masks.get_mask_card_number(list_user_input[i])
    string = " ".join(list_user_input)
    return string


# user_input = "Visa Platinum 7000792289606361"
# print(mask_account_card(user_input))

# user_input = "Счет 32984925828374"
# print(mask_account_card(user_input))

def get_date(date_input: str) -> str:
    """Функция преобразования даты"""
    date_formatted = f"{date_input[8:10]}.{date_input[5:7]}.{date_input[0:4]}"
    return date_formatted

# date_input = "2024-03-11T02:26:18.671407"
# print(get_date(date_input))