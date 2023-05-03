# Задача 3 Требуемые декораторы реализованы в модуле decorators.py
#
from decorators import use_cache_decorator_simple, use_cache_decorator_limited_time
from MyTreasury.factorization import factorize


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


@use_cache_decorator_limited_time()
def format_factorization_simple(current_number):
    result_list = factorize(current_number)
    return f'{current_number} = {" * ".join(map(lambda ii: str(ii), result_list))}'


if __name__ == "__main__":
    TEST_LIST = [(2, 3), (5, 8), (2, 3)]
    for test_elem in TEST_LIST:
        str1 = ' + '.join(map(lambda ii: str(ii), test_elem))
        print(f'{str1} = {my_cache_summa(*test_elem)}')
        str2 = ' * '.join(map(lambda ii: str(ii), test_elem))
        print(f'{str2} = {my_cache_product(*test_elem)}')

    TEST_LIST = [
        815000123456543267, 815000123456543291, 815000123456543267, 815000123456543293, 815000123456543291
    ]

    for el in TEST_LIST:
        print(format_factorization_simple(el))
