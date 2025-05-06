import time
from functools import wraps
from pyexpat.errors import messages


def log(filename=None):
    """Декоратор, который записывает логи в консоль либо в файл"""

    def wrapper(func):

        @wraps(func)
        def inner(*args, **kwargs):
            try:
                t1 = time.localtime()
                time_begin = time.strftime("%H:%M:%S", t1)
                result = func(*args, **kwargs)
                t2 = time.localtime()
                time_end = time.strftime("%H:%M:%S", t2)
                message_ok = f"{func.__name__} Время начала работы {time_begin}, время конца работы {time_end} \n"

            except Exception as e:
                message_ok = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs} \n"
                result = message_ok

            finally:
                if filename == None:
                    print(message_ok)
                else:
                    with open(filename, "a", encoding="utf8") as file:
                        file.write(message_ok)
                return result

        return inner

    return wrapper


@log(filename="log.txt")
def delete(a, b):
    time.sleep(2)
    return a / b


print(delete(100, 0))
