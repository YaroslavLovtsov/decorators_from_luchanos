
def factorize(check_number):
    result = []

    check_list1 = [2, 3, 5]
    check_list2 = [1, 7, 11, 13, 17, 19, 23, 29]

    current_check_number = check_number

    current_check_list = check_list1 + check_list2[1:]
    current_result = [current_check_list[inx] for inx, ch_el in enumerate(current_check_list) if
                      check_number % ch_el == 0]
    for elem in current_result:
        while current_check_number % elem == 0:
            current_check_number //= elem
            result.append(elem)

    step = 30
    step_number = 0
    while current_check_number > step * step:
        current_check_list = [step + sh_el for sh_el in check_list2]
        current_result = [current_check_list[inx] for inx, ch_el in
                          enumerate(current_check_list) if current_check_number % ch_el == 0]
        for elem in current_result:
            while current_check_number % elem == 0:
                current_check_number //= elem
                result.append(elem)

        step += 30
        step_number += 1

    if current_check_number != 1:
        result.append(current_check_number)

    return result
