import pandas as pd


def get_transactions_from_csv(filepath: str) -> list[dict]:
    """Получаем данные из файла csv"""
    try:
        df = pd.read_csv(filepath).to_dict(orient="records")
    except Exception as ex:
        raise Exception(f"Возникла ошибка {ex}")
    return df


def get_transactions_from_xlsx(filepath: str) -> list[dict]:
    """Получаем данные из файла формата xlsx"""
    try:
        df = pd.read_excel(filepath).to_dict(orient="records")
    except Exception as ex:
        raise Exception(f"Возникла ошибка {ex}")
    return df
