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
        if response.status_code == 200:
            data = response.json()
            # print(data)
            operation_amount = data["result"]
        else:
            operation_amount = f"Error: {response.status_code}", response.text
    return operation_amount


test_data = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "100",
      "currency": {
        "name": "руб.",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }

print(get_amount(test_data))


