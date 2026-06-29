# def add_number(a):
#     def new_number(b):
#         return a + b
#     return new_number
#
# xyz = add_number(1)
#
# print(xyz(2))

import time
from unittest import result


def decorated(func):
    def wrapper(*args, **kwargs):
        new = time.time()
        func(*args, **kwargs)
        end = time.time()
        return f'{end - new:.2f}'
    return wrapper



def hello_world(a):
    time.sleep(a)
    return None


bein_123 = decorated(hello_world)
print(bein_123(3))