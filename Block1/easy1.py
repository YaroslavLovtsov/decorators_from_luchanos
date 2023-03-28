
def string_mult(test_string: str, quant: int) -> str:
    small = test_string.lower()
    big = test_string.upper()

    if not isinstance(quant, int):
        print('Количество повторов не является целым числом')
        return ''
    elif quant < 0:
        print('Количество повторов отрицательно')
        return ''

    ind = 0
    res_list = []

    while ind < quant:
        if ind % 2 == 0:
            res_list.append(small)
        else:
            res_list.append(big)

        ind += 1

    return ''.join(res_list)


if __name__ == "__main__":

    # Написать простую функцию, которая на вход принимает строку ('test') и целое число (3),
    # а возвращает строку вида 'testTESTtest' - исходную строку, умноженную на 3, в разном регистре.
    print(string_mult('TeSt', 10))

    # Записать эту функцию в произвольную переменную. Напечатать эту переменную на экран. Что вы видите?
    another_string_mult = string_mult
    print(another_string_mult)

    # Вызвать функцию суммирования через переменную, в которую вы только что её записали.
    print(another_string_mult("buy our kitties!", 13))

