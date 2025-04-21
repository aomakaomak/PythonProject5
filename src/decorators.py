import time
from functools import wraps


from pyexpat.errors import messages


def logging_time(filename = None):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            t1 = time.localtime()
            time_begin = time.strftime("%H:%M:%S", t1)
            result = func(*args, **kwargs)
            t2 = time.localtime()
            time_end = time.strftime("%H:%M:%S", t2)
            message_ok = f"{func} Время начала работы {time_begin}, время конца работы {time_end}"
            if filename == None:
                print(message_ok)
            else:
                with open(filename, 'w', encoding = "utf8") as file:
                    file.write(message_ok)
            return result

        return inner
    return wrapper



@logging_time(filename = "logs.txt")
def my_func(a):
    for i in range(a):
        continue

print(my_func(100000000))


