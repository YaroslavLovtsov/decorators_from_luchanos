# Задача 7
#
# 7.2 Модернизировать декоратор таким образом, чтобы можно было не только осуществлять запись в файл, но и в целом
# производить любую операцию логирования или оповещения.
from random import randint
from Block3.MyTreasury.ChessKnightPath import Desk
from Block3.MyTreasury.pictures.create_picture import draw_simple_picture
from decorators import result_to_log_deco, result_to_telegram, picture_to_telegram


@result_to_log_deco('chess_knight_moves.txt')
def fill_desk_and_print(my_desk):
    my_desk.try_pass_all_desk()
    while not my_desk.success:
        improve_attempts = 0
        while not my_desk.success and improve_attempts < 100000:
            improve_attempts += 1
            my_desk.undo_last_move()

        if not my_desk.success:
            my_desk = Desk(randint(1, 8) - 1, randint(1, 8) - 1)

    return str(my_desk)


@result_to_telegram
def func1():
    return 'Hello world'


@picture_to_telegram
def func2():
    return draw_simple_picture()


desk = Desk(randint(1, 8) - 1, randint(1, 8) - 1)
print(fill_desk_and_print(desk))
print('-' * 75)
print(func1())
print('-' * 75)
print(func2())
