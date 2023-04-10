# Задача 2. Требуемые декораторы реализованы в модуле decorators.py
from decorators import ten_attempts, try_attempts


@ten_attempts
def my_func1():
    nom = int(input('Введите числитель: '))
    den = int(input('Введите знаменатель: '))

    return nom / den


@try_attempts(5)
def my_func2():
    my_list = [1, 2, 3]
    inx = int(input('Введите индекс массива: '))
    return my_list[inx]


if __name__ == "__main__":
    print(my_func1())
    print(my_func2())
