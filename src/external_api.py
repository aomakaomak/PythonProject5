import os
from dotenv import load_dotenv
import requests

load_dotenv(".env")

API_KEY = os.getenv("API_KEY")


def get_amount(transaction: dict) -> float:
    """Функция принимает транзакцию и выдает ее сумму в рублях"""
    operation_amount = transaction["operationAmount"]["amount"]
    if transaction["operationAmount"]["currency"]["code"] != "RUB":
        currency_from = transaction["operationAmount"]["currency"]["code"]
        amount = transaction["operationAmount"]["amount"]
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_from}&amount={amount}"
        headers = {"apikey": API_KEY}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception("Failed to convert currency")
        data = response.json()
        operation_amount = data["result"]
    return operation_amount
