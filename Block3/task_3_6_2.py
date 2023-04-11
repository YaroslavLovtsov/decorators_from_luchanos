# Задача 6
# Сами декораторы в модуле decorators.py
from decorators import password_simple_required_deco


@password_simple_required_deco
def say_hello():
    print('Hello world')


say_hello()
