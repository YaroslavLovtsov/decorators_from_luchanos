# Задача 4 (сами декораторы в файле decorators.py)
# 4.1 Написать декоратор, который бы измерял время работы функции и печатал бы его на экран.
# 4.2 Доработать декоратор таким образом, чтобы в логах было название запускаемой функции помимо времени исполнения.
from MyTreasury.PI_many_singns import SharpFloat
from decorators import time_deco_simple, time_deco_log


@time_deco_log("log.txt")
def sharp_arc_tangent(a, b, sixtets):
    cur_ind = 1
    stop_test = False
    sign = 1

    cur_el = SharpFloat(a, b, sixtets)
    result = cur_el

    while not stop_test:
        cur_ind += 2
        sign = -sign
        cur_el = a * cur_el
        cur_el /= b
        cur_el = a * cur_el
        cur_el /= b

        if cur_el.is_zero():
            stop_test = True
        else:
            cur_add = cur_el / cur_ind
            if sign == 1:
                result += cur_add
            else:
                result -= cur_add

    return result


SIXTETS_LIST = [29, 179, 449, 1679, 3689]
for curr_sixtets in SIXTETS_LIST:
    arc_tangent_1_5 = sharp_arc_tangent(1, 5, curr_sixtets)
    arc_tangent_1_239 = sharp_arc_tangent(1, 239, curr_sixtets)
    PI = 16 * arc_tangent_1_5 - 4 * arc_tangent_1_239
    print(f'{curr_sixtets} сикстетов')
    print(PI)
