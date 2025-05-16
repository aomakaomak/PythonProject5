import pytest
import requests
from unittest.mock import Mock, patch
from src.external_api import get_amount, API_KEY

test_data = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {"amount": "100", "currency": {"name": "руб.", "code": "USD"}},
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589",
}

answer = {
    "success": True,
    "query": {"from": "USD", "to": "RUB", "amount": 100},
    "info": {"timestamp": 1747408144, "rate": 80.696385},
    "date": "2025-05-16",
    "result": 8070.8,
}


@patch("requests.get")
def test_get_amount(mock_get):
    mock_get.return_value.json.return_value = answer
    mock_get.return_value.status_code = 200
    assert get_amount(test_data) == 8070.8
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=100",
        headers={"apikey": API_KEY},
    )


@patch("requests.get")
def test_get_amount_404(mock_get):
    mock_get.return_value.json.return_value = answer
    mock_get.return_value.status_code = 404
    assert get_amount(test_data) == "Error: 404"
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=100",
        headers={"apikey": API_KEY},
    )
