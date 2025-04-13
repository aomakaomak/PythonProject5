import pytest

@pytest.fixture
def user_input_correct():
    return "Visa Platinum 7000 79** **** 6361"


@pytest.fixture
def filter_executed():
    return [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
]