

def get_choice(choice):
    choice_status = (input("""Введите статус, по которому необходимо выполнить фильтрацию.
                              Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: """)).lower()
    if choice_status not in ["executed", "cancelled", "pending"]:
        print(f'Статус операции "{choice_status}" недоступен.')
        get_choice(choice)
    else:
        return choice_status







def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    choice = input("""Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла: """)
    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        status = get_choice(choice)
        return status



print(main())