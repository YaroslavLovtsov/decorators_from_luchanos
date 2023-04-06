# ### Блок 2
def sum_with_counter(*args):
    global CNT
    global COUNTER_DICT

    result = 0
    for el in args:
        result += el

    CNT += 1
    COUNTER_DICT['summation'] += 1

    return result


def inn_validate(inn_str):
    global CNT
    global COUNTER_DICT

    inn_is_valid = True
    s = 0
    s1 = 0
    s2 = 0
    lng = len(inn_str)
    check_inn_tuple = 3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8

    if lng == 12:
        for ind in range(lng):
            if inn_str.isdigit():
                cur_dig = int(inn_str[ind])
                if ind != lng - 1:
                    if ind != lng - 2:
                        s1 += check_inn_tuple[ind + 1] * cur_dig
                    else:
                        if (s1 % 11 - cur_dig) % 10 != 0:
                            inn_is_valid = False
                            break

                    s2 += check_inn_tuple[ind] * cur_dig
                else:
                    if (s2 % 11 - cur_dig) % 10 != 0:
                        inn_is_valid = False
            else:
                inn_is_valid = False
                break

    elif lng == 10:
        for ind in range(lng - 1):
            if inn_str.isdigit():
                cur_dig = int(inn_str[ind])
                s += check_inn_tuple[ind + 2] * cur_dig

        control_digit1 = (s % 11) % 10
        inn_is_valid = (control_digit1 == int(inn_str[9]))
    else:
        inn_is_valid = False

    CNT += 1
    COUNTER_DICT['inn_validation'] += 1

    return inn_is_valid


def chess_knight_moves(hor, ver):
    global CNT
    global COUNTER_DICT

    print(f'Запуск функции chess_knight_moves - конь на горизонтали {8 - hor}, вертикали {ver + 1}')
    h_list = [h_ind for h_ind in range(hor - 2, hor + 3) if h_ind * (7 - h_ind) >= 0]
    v_list = [v_ind for v_ind in range(ver - 2, ver + 3) if v_ind * (7 - v_ind) >= 0]

    result = []
    for elem in [[(h_ind, v_ind) for v_ind in v_list if (h_ind - hor) ** 2 + (v_ind - ver) ** 2 == 5]
                 for h_ind in h_list]:
        result += elem

    result_board = [['.' for _ in range(8)] for _ in range(8)]
    result_board[hor][ver] = '#'

    for cur_h, cur_v in result:
        result_board[cur_h][cur_v] = '*'

    for res_row in result_board:
        print(*res_row)

    CNT += 1
    COUNTER_DICT['chess_knight_moves'] += 1

    return result


def function1(n, d, r, epsilon=1E-15):
    def matrix_elem(p, q, ind_x, ind_y):
        if ind_y > ind_x:
            res = p
        elif ind_x > ind_y:
            res = q
        else:
            res = 1

        return res

    global CNT
    global COUNTER_DICT

    CNT += 1
    COUNTER_DICT['func1'] += 1

    if n == 1:
        return n / d
    elif n <= 0:
        raise "Параметр n должен быть больше нуля"

    my_mathix = [[matrix_elem(n, d, ind_i, ind_j) for ind_j in range(r)] for ind_i in range(r)]

    my_vector = [n - el for el in range(r)]
    stop_test = False
    count = 0

    while not stop_test:
        count += 1
        if my_vector == 0:
            old_value = my_vector[0]
        else:
            old_value = my_vector[0] / my_vector[1]

        result_vector = [0 for _ in range(r)]
        for row_ind, row in enumerate(my_mathix):
            for col_ind, col in enumerate(row):
                result_vector[row_ind] += col * my_vector[col_ind]

        my_vector = result_vector
        if my_vector[1] != 0:
            result = my_vector[0] / my_vector[1]
            delta = old_value - result

            if (delta < epsilon) and (delta > - epsilon):
                stop_test = True

        if count > 50:
            result = my_vector[0] / my_vector[1]
            stop_test = True

    return result


def summ_with_midware():
    def yet_another_sum(*args):
        result = 0
        for el in args:
            result += el

        return result

    return yet_another_sum


if __name__ == "__main__":
    # #### Easy
    # 1. Реализовать счетчик, который будет увеличиваться каждый раз, когда у нас осуществляется запуск
    # функции суммирования.
    CNT = 0
    COUNTER_DICT = {
        'summation': 0,
        'inn_validation': 0,
        'chess_knight_moves': 0,
        'func1': 0
    }

    print('Вызываем функцию sum_with_counter с параметрами 1, 2, 33, 444')
    print(sum_with_counter(1, 2, 33, 444))

    print('Вызываем функцию sum_with_counter с параметрами 1, 1/2, 1/3, 1/4, 1/5, 1/6, 1/7, 1/8, 1/9, 1/10, 1/11, 1/12')
    print(sum_with_counter(1, 1/2, 1/3, 1/4, 1/5, 1/6, 1/7, 1/8, 1/9, 1/10, 1/11, 1/12))
    print('Вызываем функцию sum_with_counter с параметрами '
          '1, 1 / 2 / 2, 1 / 3 / 3, 1 / 4 / 4, 1 / 5 / 5, 1 / 6 / 6, 1 / 7 / 7, 1 / 8 / 8, 1 / 9 / 9')
    print(sum_with_counter(1, 1 / 2 / 2, 1 / 3 / 3, 1 / 4 / 4, 1 / 5 / 5, 1 / 6 / 6, 1 / 7 / 7, 1 / 8 / 8, 1 / 9 / 9))

    print('-' * 150)

    # Medium
    # 1. Написать ещё несколько произвольных функций (3-4 штуки) и решить задачу со счетчиком аналогично той,
    # которая была реализована для запуска функции суммирования.
    INN_DICT = {
        'Ашан': '7703270067',
        'Перекресток': '7728029110',
        "О'Кей": '7826087713',
        'Гик брейнс': "7726381870",
        'ИП Минин Владилен': '781714316555',
        'ИП Вася Пупкин (ИНН взят с потолка)': '123456789012'
        # Если добавить в словарь свой ИНН - проверка также должна показать, что ИНН корректен!
    }

    for k, v in INN_DICT.items():
        current_inn_is_valid = inn_validate(v)
        print(f'{k} - ИНН ({v}) {"корректен" if current_inn_is_valid else "некорректен!!!"}')

    print('-' * 150)
    CHESS_KNIGHT_POSITIONS = [(3, 3), (2, 5), (0, 6), (1, 1), (7, 0), (6, 5)]
    for h, v in CHESS_KNIGHT_POSITIONS:
        moves_list = chess_knight_moves(h, v)
        print('-' * 150)
        print(f"Результируюший список: {moves_list}")
        print('_' * 150)

    print('=' * 150)
    FUNC1_PARAMS = [(3, 1, 3), (5, 1, 4), (7, 1, 5), (11, 1, 6), (13, 1, 7)]
    for n_, d_, r_ in FUNC1_PARAMS:
        print('func1', n_, d_, r_, function1(n_, d_, r_))
    print(CNT, COUNTER_DICT)

    # 2. Написать функцию, внутри которой у нас будет объявляться наша функция суммирования и возвращаться в качестве
    # результата работы из объемлющей функции.
    print(summ_with_midware)

    # 3. Попробуйте вызвать написанную функцию и сохраните результат её работы в переменную. Напечатайте результат
    # на экран. Что наблюдаете?
    new_sum_function = summ_with_midware()
    print(new_sum_function)

    # 4. Осуществите вызов функции суммирования из полученной переменной.
    print(new_sum_function(1, 2, 3))

    # HARD
    # 4. Перенесите глобальный счетчик на уровень объемлющей функции. Будет ли работать наш код? Если да, то
    # как поменялся смысл написанного кода? Если нет, то что надо изменить, чтобы всё заработало?
    #
    # Данный функционал в разработке. По традиции, файл questions.md дополняется новыми вопросами.
