# Задача 3 Требуемые декораторы реализованы в модуле decorators.py
#
# 3.2 Сделать так, чтобы информация в кэше была актуальной не более 10 секунд. Предусмотреть механизм автоматической
# очистки кэша в процессе выполнения функций.
#
# 3.3 Параметризовать время кэширования в декораторе.
from decorators import use_cache_decorator_simple


@use_cache_decorator_simple
def my_cache_summa(*args):
    res_sum = 0
    for el_sum in args:
        res_sum += el_sum

    return res_sum


@use_cache_decorator_simple
def my_cache_product(*args):
    res_prod = 1
    for el_prod in args:
        res_prod *= el_prod

    return res_prod


if __name__ == "__main__":
    TEST_LIST = [(2, 3), (5, 8), (2, 3)]
    for test_elem in TEST_LIST:
        str1 = ' + '.join(map(lambda ii: str(ii), test_elem))
        print(f'{str1} = {my_cache_summa(*test_elem)}')
        str2 = ' * '.join(map(lambda ii: str(ii), test_elem))
        print(f'{str2} = {my_cache_product(*test_elem)}')
