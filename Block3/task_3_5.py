# Задача 5
#
# После решения задач написать функцию. Задекорировать её сразу несколькими из созданных декораторов и посмотреть
# на результат и суметь объяснить его. Потом поменять порядок декорирования и проделать то же самое.
from decorators import password_simple_required_deco, password_required_deco, time_deco_simple, result_to_telegram
from Block3.MyTreasury.factorization import factorize


@time_deco_simple
@password_required_deco('PASSWORD1')
@result_to_telegram
def func1():
    number_to_factorize = int(input('Введите целое число для разложения на множители: '))
    return factorize(number_to_factorize)


@password_simple_required_deco
@time_deco_simple
@result_to_telegram
def func2(number_to_factorize_arg):
    result_list = factorize(number_to_factorize_arg)
    return f'{number_to_factorize_arg} = {" * ".join(map(lambda ii: str(ii), result_list))}'


print('Некорректная последовательность декораторов. Требуется пароль PASSWORD1')
print(func1())
print('Время выполнения функции рассчитано с учетом времени ввода пароля, а также времени ввода числа для разложения')
print('-' * 150)
print('Корректная последовательность декораторов. Требуется пароль по умолчанию')
current_number_to_factorize = int(input('Введите целое число для разложения на множители: '))
print(func2(current_number_to_factorize))
print('Это реальное время выполнения функции')
