import json
from src.processing import filter_by_state
from src.processing import sort_by_date
from src.generators import filter_by_currency
from src.search_description import search_in_description


def get_choice():
    """Повторяем запрос ввода в случае ошибки"""
    choice_status = (
        input(
            """Введите статус, по которому необходимо выполнить фильтрацию.
                              Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: """
        )
    ).lower()
    if choice_status in ["executed", "cancelled", "pending"]:
        return choice_status
    else:
        print(f'Статус операции "{choice_status}" недоступен.')
        return get_choice()


def main():
    """Основная входная функция"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    choice = input(
        """Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла: """
    )
    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        status = get_choice()
        try:
            with open("data/oper.json", encoding="UTF-8") as file:
                operations = list(json.load(file))

            filtered_operations = filter_by_state(operations, user_state=status)

            is_sort_by_date = input("Отсортировать операции по дате? Да/Нет: ")
            if is_sort_by_date.lower() == "да":
                how_sort = input("Отсортировать по возрастанию или по убыванию?: ")
                if how_sort == "по возрастанию":
                    decrease = False
                elif how_sort == "по убыванию":
                    decrease = True

            if (is_sort_by_date).lower() == "да":
                filtered_operations = sort_by_date(
                    filtered_operations, decreasing=decrease
                )

            is_rub = input("Выводить только рублевые транзакции? Да/Нет: ")
            if is_rub.lower() == "да":
                filtered_operations = list(
                    filter_by_currency(filtered_operations, "руб.")
                )

            is_filter_description = input(
                "Отфильтровать список транзакций по определенному слову в описании? Да/Нет: "
            )
            if is_filter_description.lower() == "да":
                word = input("Введите это слово: ")
                filtered_operations = search_in_description(filtered_operations, word)

            print("Распечатываю итоговый список транзакций...")
            print(f"Всего банковских операций в выборке: {len(filtered_operations)}")

            return filtered_operations

        except Exception as ex:
            raise Exception(f"Ошибка {ex}")


print(main())
