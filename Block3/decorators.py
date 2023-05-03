import hashlib
from datetime import datetime as dt, timedelta as td
import os
from dotenv import load_dotenv
from MyTreasury.YariqGunesBot import bot_client as bot


# 1.1 Написать декоратор, который перед запуском произвольной функции с произвольным набором аргументов будет
# показывать в консоли сообщение "Покупайте наших котиков!" и возвращать результат запущенной функции.
def advertisement_simple(func):
    def wrap(*args, **kwargs):
        print('Покупайте наших котиков')

        return func(*args, **kwargs)

    return wrap


# 1.2 Параметризовать декоратор таким образом, чтобы сообщение, печатаемое перед выполнением функции можно было
# задавать как параметр во время декорирования.
def advertisement(message='Покупайте наших котиков'):
    def advertisement_middleware(func):
        def wrap(*args, **kwargs):
            print(message)

            return func(*args, **kwargs)

        return wrap

    return advertisement_middleware


# 2.1 Написать декоратор, который внутри себя выполнял бы функцию и возвращал бы результат её работы в случае успешного
# выполнения. В случае возникновения ошибки во время выполнения функции нужно сделать так, чтобы выполнение функции
# было повторено ещё раз с теми же самыми аргументами, но не более 10 раз. Если после последней попытки функцию так и
# не удастся выполнить успешно, то бросать исключение.
def ten_attempts(func):
    def wrap(*args, **kwargs):
        attempts = 0
        stop_test = False
        result = None

        while not stop_test:
            try:
                if attempts > 0:
                    print('-' * 75)
                    print(f'Попытка {attempts + 1}')
                result = func(*args, **kwargs)
                print('=' * 75)
                print(f'Функция успешно выполнена с {attempts + 1} попытки')
                stop_test = True
            except:
                attempts += 1
                if attempts > 10:
                    raise "Не удалось выполнить функцию с 10 попытки"

        return result

    return wrap


# 2.2 Параметризовать декоратор таким образом, чтобы количество попыток выполнения функции можно было задавать как
# параметр во время декорирования.
def try_attempts(max_attempts_count):

    def attempts_before_success(func):
        def wrap(*args, **kwargs):
            attempts = 0
            stop_test = False
            result = None

            while not stop_test:
                try:
                    if attempts > 0:
                        print('-' * 75)
                        print(f'Попытка {attempts + 1}')
                    result = func(*args, **kwargs)
                    print('=' * 75)
                    print(f'Функция успешно выполнена с {attempts + 1} попытки')
                    stop_test = True
                except:
                    attempts += 1
                    if attempts > max_attempts_count:
                        raise f"Не удалось выполнить функцию с {max_attempts_count} попытки"

            return result

        return wrap

    return attempts_before_success


# Вспомогательная функция для кеширующего декоратора.
def cache_parameters(func, *args, **kwargs):
    hash_str = f'''{"{"}
    function: {func},
    args: {str(args)},
    kwargs: {str(kwargs)}
{"}"}'''

    hash_bytes = hash_str.encode('UTF-8')
    hash_object = hashlib.md5(hash_bytes)

    return hash_object.hexdigest()


# 3.1 Написать кэширующий декоратор. Суть в том, что если декорируемая функция будет запущена с теми параметрами с
# которыми она уже запускалась - брать результат из кэша и не производить повторное выполнение функции.
def use_cache_decorator_simple(func):
    def wrap(*args, **kwargs):
        cache_key = cache_parameters(func, *args, **kwargs)
        if cache_key in CACHE_SIMPLE.keys():
            print('Извлечено из кэша:')
            result = CACHE_SIMPLE[cache_key]
        else:
            result = func(*args, **kwargs)
            CACHE_SIMPLE[cache_key] = result
        return result

    return wrap


# 3.2 Сделать так, чтобы информация в кэше была актуальной не более 10 секунд. Предусмотреть механизм автоматической
# очистки кэша в процессе выполнения функций.
#
# 3.3 Параметризовать время кэширования в декораторе.
def use_cache_decorator_limited_time(seconds=10):
    def use_cache_decorator(func):
        def wrap(*args, **kwargs):
            cache_key = cache_parameters(func, *args, **kwargs)
            if cache_key in CACHE_SIMPLE.keys():
                result_from_cache, time_to_expire = CACHE_SIMPLE[cache_key]

                if time_to_expire < dt.now():
                    print('Могло быть извлечено из кэша, однако пришлось пересчитать:')
                    result = func(*args, **kwargs)
                    CACHE_SIMPLE[cache_key] = result, dt.now() + td(seconds=seconds)
                else:
                    print('Извлечено из кэша:')
                    result = result_from_cache
            else:
                result = func(*args, **kwargs)
                CACHE_SIMPLE[cache_key] = result, dt.now() + td(seconds=seconds)
            return result

        return wrap

    return use_cache_decorator


# 4.1 Написать декоратор, который бы измерял время работы функции и печатал бы его на экран.
# 4.2 Доработать декоратор таким образом, чтобы в логах было название запускаемой функции помимо времени исполнения.
def time_deco_simple(func):
    def wrap(*args, **kwargs):
        time_start = dt.now()
        result = func(*args, **kwargs)
        time_finish = dt.now()
        print(f'''Вызов функции  {func.__name__} с аргументами
    args: {str(args)},
    kwargs: {str(kwargs)}
Время выполнения {time_finish - time_start}''')
        return result

    return wrap


# 4.3 Доработать декоратор так, чтобы запись лога для функции велась в файл, путь к которому нужно было бы задавать
# во время декорирования как параметр.
def time_deco_log(filename):
    def time_deco_middleware(func):
        def wrap(*args, **kwargs):
            time_start = dt.now()
            f_log = open(filename, 'a')
            result = func(*args, **kwargs)
            time_finish = dt.now()
            current_log = f'''Вызов функции  {func.__name__} с аргументами
            args: {str(args)},
            kwargs: {str(kwargs)}
        Старт {time_start}
        Время выполнения {time_finish - time_start}
{'#' * 150}
'''
            f_log.write(current_log)
            f_log.write(f"")
            f_log.close()
            return result

        return wrap

    return time_deco_middleware


# 6.1 Написать декоратор, который будет запрашивать у пользователя пароль при попытке функции осуществить вызов. Если
# введён верный пароль, то функция будет выполнена и вернется результат её работы. Если нет - в консоли появляется
# соответствующее сообщение.
def password_simple_required_deco(func):
    load_dotenv('.env')

    def password_required_wrap(*args, **kwargs):
        password = input('Введите пароль: ')
        if password == os.getenv('DECO_PASSWORD_COMMON'):
            result = func(*args, **kwargs)
        else:
            print("Пароль введен некорректно")
            result = None

        return result

    return password_required_wrap


# 6.2 Параметризовать декоратор таким образом, чтобы можно было задавать индивидуальный пароль для каждой декорируемой
# функции.
def password_required_deco(password_id):
    def password_required_middleware(func):
        load_dotenv('.env')

        def password_required_wrap(*args, **kwargs):
            password = input('Введите пароль: ')
            if password == os.getenv(password_id):
                result = func(*args, **kwargs)
            else:
                print("Пароль введен некорректно")
                result = None

            return result

        return password_required_wrap

    return password_required_middleware


# 7.1 Написать декоратор, который после выполнения функции будет возвращать результат и записывать его в текстовый файл.
#
def result_to_log_deco(file_name):
    def result_to_log_inner(func):
        def wrap(*args, **kwargs):
            f_log = open(file_name, 'a')
            f_log.write('-' * 50)
            f_log.write('\n')
            result = func(*args, *kwargs)
            f_log.write(str(result))

            return result

        return wrap

    return result_to_log_inner


def result_to_telegram(func):
    def wrap(*args, **kwargs):
        admin_chat_id = os.getenv('ADMIN_CHAT_ID')

        result = func(*args, **kwargs)
        bot.send_message(chat_id=admin_chat_id, text=f'''Вызов функции  {func.__name__} с аргументами
    args: {str(args)},
    kwargs: {str(kwargs)}
Результат выполнения 
{result}''')

        bot.send_message(chat_id=admin_chat_id, text='Подписывайтесь на телеграм-канал t.me/YariqGunesTravel')
        bot.send_message(chat_id=admin_chat_id, text='Добро пожаловать на http://github.com/YaroslavLovtsov')

        return result

    return wrap


def picture_to_telegram(func):
    def wrap(*args, **kwargs):

        admin_chat_id = os.getenv('ADMIN_CHAT_ID')
        result = func(*args, **kwargs)

        bot.send_photo(chat_id=admin_chat_id, photo=open(result, 'rb'))
        bot.send_message(chat_id=admin_chat_id, text='Подписывайтесь на телеграм-канал t.me/YariqGunesTravel')
        bot.send_message(chat_id=admin_chat_id, text='Добро пожаловать на http://github.com/YaroslavLovtsov')

        return result

    return wrap


CACHE_SIMPLE = {}
CACHE_LIMITED_TIME = {}
