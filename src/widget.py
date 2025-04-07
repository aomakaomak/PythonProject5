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


user_input = "Visa Platinum 7000792289606361"
print(mask_account_card(user_input))