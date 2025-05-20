import logging

logger = logging.getLogger("masks")
file_handler = logging.FileHandler("logs/masks.log", "w", encoding="UTF-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера карты"""
    string = str(card_number)
    if not string.isdigit():
        logger.error("Введен неверный номер карты")
        return "Ошибка. Пожалуйста, введите номер карты"
    elif len(string) != 16:
        logger.error("Введен неверный номер карты")
        return "Неверный номер карты"
    else:
        logger.info("Номер карты введен успешно")
        return f"{string[0:4]} {string[4:6]}** **** {string[12:16]}"


def get_mask_account(account_number: int) -> str:
    """Функция маскировки расчетного счета"""
    string = str(account_number)
    if not string.isdigit():
        logger.error("Введен неверный номер счета")
        return "Ошибка. Пожалуйста, введите номер счета"
    elif len(string) != 14:
        logger.error("Введен неверный номер счета")
        return "Неверный номер счета"
    else:
        logger.info("Номер счета введен успешно")
        return f"**{string[-4:-1]}{string[-1]}"
