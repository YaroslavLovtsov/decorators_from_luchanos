# Задача 1. Требуемые декораторы реализованы в модуле decorators.py
from decorators import advertisement, advertisement_simple


@advertisement_simple
def my_func1():
    print('Hello world')


@advertisement('Подписывайтесь на мой телеграм-канал t.me/YariqGunesTravel')
def my_func2():
    print('Hello world')


if __name__ == "__main__":
    my_func1()
    my_func2()
