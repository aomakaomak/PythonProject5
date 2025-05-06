import time
from calendar import error
from functools import wraps


from pyexpat.errors import messages


def log(filename = None):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                func(*args, **kwargs)

            except Exception as e:
                message_ok = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                result = "Функция отработала с ошибкой"

            else:
                t1 = time.localtime()
                time_begin = time.strftime("%H:%M:%S", t1)
                result = func(*args, **kwargs)
                t2 = time.localtime()
                time_end = time.strftime("%H:%M:%S", t2)
                message_ok = f"{func.__name__} Время начала работы {time_begin}, время конца работы {time_end}"

            finally:
                if filename == None:
                    print(message_ok)
                else:
                    with open(filename, 'w', encoding="utf8") as file:
                        file.write(message_ok)
                return result

        return inner

    return wrapper



@log(filename="mylog.txt")
def delete(a, b):
    time.sleep(2)
    return a/b

print(delete(100, 0))


