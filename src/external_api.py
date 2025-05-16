# import requests
#
# url = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=100"
#
# payload = {}
# headers= {
#   "apikey": "ViEI99ST9ykVpZcxIws9zE9OuDWnF9nx"
# }
#
# response = requests.request("GET", url, headers=headers, data = payload)
#
# status_code = response.status_code
# result = response.json()
# print(result)


import requests

url = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=100"

headers= {
  "apikey": "ViEI99ST9ykVpZcxIws9zE9OuDWnF9nx"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}", response.text)


def get_amount(transaction: dict) -> float:
  """ Функция принимает транзакцию и выдает ее сумму в рублях"""
  operation_amount = transaction["operationAmount"]["amount"]
  if transaction["operationAmount"]["currency"]["code"] != "RUB":
    currency_from = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_from}&amount={amount}"
    headers = {
      "apikey": "ViEI99ST9ykVpZcxIws9zE9OuDWnF9nx"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
      data = response.json()
      print(data)
      operation_amount = data["result"]
    else:
      operation_amount = f"Error: {response.status_code}", response.text
  return operation_amount

test_tr =  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "1000",
      "currency": {
        "name": "руб.",
        "code": "EUR"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }

print(get_amount(test_tr))
