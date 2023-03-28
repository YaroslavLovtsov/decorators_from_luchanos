
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


print(string_mult('TeSt', 17.9))

