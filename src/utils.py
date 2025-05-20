import json
import logging

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("logs/utils.log", "w", encoding="UTF-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_transactions(file_path: str) -> list:
    """Функция, которая принимает путь к файлу json и выводит его содержимое в консоль"""
    try:
        logger.info("Открываем файл и записываем его содержимое в переменную")
        with open(file_path, "r", encoding="UTF-8") as json_file:
            transactions_list = json.load(json_file)
    except Exception as ex:
        logger.error(f"Не удалось открыть файл. Ошибка {ex}")
        return []
    else:
        if isinstance(transactions_list, list):
            logger.info("Запись файла в переменную прошла удачно")
            return transactions_list
        else:
            logger.error("Неверный тип объекта")
            return []
