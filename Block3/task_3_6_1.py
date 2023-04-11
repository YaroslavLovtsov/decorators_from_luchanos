# Задача 6
# Сами декораторы в модуле decorators.py
from decorators import password_required_deco


@password_required_deco('PASSWORD1')
def say_hello():
    print('Hello world')


say_hello()
