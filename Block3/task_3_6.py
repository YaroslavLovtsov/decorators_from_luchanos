# Задача 6
#
# 6.1 Написать декоратор, который будет запрашивать у пользователя пароль при попытке функции осуществить вызов. Если
# введён верный пароль, то функция будет выполнена и вернется результат её работы. Если нет - в консоли появляется
# соответствующее сообщение.
#
# 6.2 Параметризовать декоратор таким образом, чтобы можно было задавать индивидуальный пароль для каждой декорируемой
# функции.

def password_required_deco(func):
    def password_required_wrap(*args, **kwargs):
        password = input('Введите пароль: ')
        if password == "Pa$$w0rd":
            result = func(*args, **kwargs)
        else:
            print("Пароль введен некорректно")
            result = None

        return result

    return password_required_wrap


@password_required_deco
def say_hello():
    print('Hello world')


say_hello()
