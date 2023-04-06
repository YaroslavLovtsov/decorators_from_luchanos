
def healthy_men_sum(*args):
    result = 0
    for el in args:
        result += el

    return result


def smoker_sum(arg1, arg2, arg3, arg4, *args):
    result = arg1 + arg2 + arg3 + arg4

    for el in args:
        result += el

    return result


def crazy_smoker_sum(arg1, arg2, arg3, arg4, *args, **kvargs):
    result = arg1 + arg2 + arg3 + arg4

    print("Выдача на печать *args")
    print(*args)
    print("Выдача на печать *kvargs")
    print(*kvargs)
    print("Выдача на печать **kvargs")
    try:
        print(**kvargs)
    except TypeError:
        print("Ошибка при попытке выдать на печать **kvargs")

    for inx, el in enumerate(args):
        if inx < 2:
            result += el

    if 'bonus_arg' in kvargs.keys():
        result += kvargs['bonus_arg']

    return result


if __name__ == "__main__":
    # Написать функцию, которая на вход будет принимать произвольное количество аргументов и возвращать их сумму.
    print(healthy_men_sum(1, 2, 3, 40.4, 5, 6, 77))

    # В сигнатуре функции объявить 4 обязательных аргумента, но оставить возможность передавать в неё сколько угодно
    # дополнительных аргументов.
    print(smoker_sum(111, 2, 3, 40.4, 5, 6, 77))

    #    - прокинуть в функцию только 1 аргумент
    try:
        print(smoker_sum(1))
    except TypeError:
        print("Запуск функции с одним аргументом - ошибка, меньше 4 аргументов указывать нельзя!")

    #    - прокинуть аргументы таким образом, чтобы обязательный аргумент был передан одновременно позиционно и по
    # ключу
    try:
        print(smoker_sum(1, 2, 3, 4, arg1=5))
    except TypeError:
        print("Запуск функции с аргументом, переданным одновременно позиционно и по ключу - ошибка")

    # Модифицировать функцию таким образом, чтобы для суммирования брались только обязательные аргументы,
    # первые 2 аргумента из дополнительных позиционных аргументов и любой аргумент из дополнительных аргументов
    # (если они есть), переданных по ключу (если они есть).
    #    - создать кортеж со значениями и распаковать его при вызове функции с помощью *
    #    - создать словарь со значениями и распаковать его при вызове функции с помощью * и **: что наблюдаете? Почему?
    print(crazy_smoker_sum(111, 2, 3, 40.4, 5, 66, 7777, extra_arg_1=8888, bonus_arg=9999))
