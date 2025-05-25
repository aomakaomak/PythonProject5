import pandas as pd

def get_transactions_from_csv(filepath: str) -> list[dict]:
    try:
        df = pd.read_csv(filepath).to_dict(orient="records")
    except Exception as ex:
        raise Exception(f"Возникла ошибка {ex}")
    return df

# print(get_transactions_from_csv("data/transactions.csv"))


def get_transactions_from_xlsx(filepath: str) -> list[dict]:
    try:
        df = pd.read_excel(filepath).to_dict(orient="records")
    except Exception as ex:
        raise Exception(f"Возникла ошибка {ex}")
    return df

# print(get_transactions_from_xlsx("data/transactions_excel1.xlsx"))





