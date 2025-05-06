import time

import pytest

from src.decorators import log


def test_log_empty():

    @log()
    def delete(a, b):
        time.sleep(2)
        return a / b

    result = delete(100, 20)
    assert result == 5
    result = delete(100, 0)
    assert result == "delete error: ZeroDivisionError. Inputs: (100, 0), {} \n"


def test_log_filename():

    @log(filename="log.txt")
    def delete(a, b):
        time.sleep(2)
        return a / b

    result = delete(100, 50)
    assert result == 2
    result = delete(100, 0)
    assert result == "delete error: ZeroDivisionError. Inputs: (100, 0), {} \n"
