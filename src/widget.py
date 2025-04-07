import masks

def mask_account_card(user_input: str) -> str:
    list_user_input = user_input.split()
    string = ""
    if "Счет" in user_input:
        for word in list_user_input:
            if word.isdigit():
                string = masks.get_mask_account(word)
    else:
        for word in list_user_input:
            if word.isdigit():
                string = masks.get_mask_card_number(word)
    return string


user_input = "Visa Platinum 7000792289606361"
print(mask_account_card(user_input))