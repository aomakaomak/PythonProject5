import json

def get_transactions(file_path: str) -> list:
    """ Функция, которая принимает путь к файлу json и выводит его содержимое в консоль """
    try:
        with open(file_path, "r", encoding="UTF-8") as json_file:
            transactions_list = json.load(json_file)
    except:
        return []
    else:
        return transactions_list

print(get_transactions("data/operations.json"))



