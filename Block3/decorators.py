import hashlib
from datetime import datetime


# 1.1 Написать декоратор, который перед запуском произвольной функции с произвольным набором аргументов будет
# показывать в консоли сообщение "Покупайте наших котиков!" и возвращать результат запущенной функции.
def advertisement_simple(func):
    def wrap(*args, **kvargs):
        print('Покупайте наших котиков')

        return func(*args, **kvargs)

    return wrap


# 1.2 Параметризовать декоратор таким образом, чтобы сообщение, печатаемое перед выполнением функции можно было
# задавать как параметр во время декорирования.
def advertisement(message='Покупайте наших котиков'):
    def advertisement_middleware(func):
        def wrap(*args, **kvargs):
            print(message)

            return func(*args, **kvargs)

        return wrap

    return advertisement_middleware


# 2.1 Написать декоратор, который внутри себя выполнял бы функцию и возвращал бы результат её работы в случае успешного
# выполнения. В случае возникновения ошибки во время выполнения функции нужно сделать так, чтобы выполнение функции
# было повторено ещё раз с теми же самыми аргументами, но не более 10 раз. Если после последней попытки функцию так и
# не удастся выполнить успешно, то бросать исключение.
def ten_attempts(func):
    def wrap(*args, **kvargs):
        attempts = 0
        stop_test = False
        result = None

        while not stop_test:
            try:
                if attempts > 0:
                    print('-' * 75)
                    print(f'Попытка {attempts + 1}')
                result = func(*args, **kvargs)
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
        def wrap(*args, **kvargs):
            attempts = 0
            stop_test = False
            result = None

            while not stop_test:
                try:
                    if attempts > 0:
                        print('-' * 75)
                        print(f'Попытка {attempts + 1}')
                    result = func(*args, **kvargs)
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
def cache_parameters(func, *args, **kvargs):
    hash_str = f'''{"{"}
    function: {func},
    args: {str(args)},
    kvargs: {str(kvargs)}
{"}"}'''

    hash_bytes = hash_str.encode('UTF-8')
    hash_object = hashlib.md5(hash_bytes)

    return hash_object.hexdigest()


# 3.1 Написать кэширующий декоратор. Суть в том, что если декорируемая функция будет запущена с теми параметрами с
# которыми она уже запускалась - брать результат из кэша и не производить повторное выполнение функции.
def use_cache_decorator_simple(func):
    def wrap(*args, **kvargs):
        cache_key = cache_parameters(func, *args, **kvargs)
        if cache_key in CACHE_SIMPLE.keys():
            print('Извлечено из кэша:')
            result = CACHE_SIMPLE[cache_key]
        else:
            result = func(*args, **kvargs)
            CACHE_SIMPLE[cache_key] = result
        return result

    return wrap


# 4.1 Написать декоратор, который бы измерял время работы функции и печатал бы его на экран.
# 4.2 Доработать декоратор таким образом, чтобы в логах было название запускаемой функции помимо времени исполнения.
def time_deco_simple(func):
    def wrap(*args, **kvargs):
        time_start = datetime.now()
        result = func(*args, **kvargs)
        time_finish = datetime.now()
        print(f'''Вызов функции  {func.__name__} с аргументами
    args: {str(args)},
    kvargs: {str(kvargs)}
Время выполнения {time_finish - time_start}''')
        return result

    return wrap


# 4.3 Доработать декоратор так, чтобы запись лога для функции велась в файл, путь к которому нужно было бы задавать
# во время декорирования как параметр.
def time_deco_log(filename):
    def time_deco_middleware(func):
        def wrap(*args, **kvargs):
            time_start = datetime.now()
            f_log = open(filename, 'a')
            result = func(*args, **kvargs)
            time_finish = datetime.now()
            current_log = f'''Вызов функции  {func.__name__} с аргументами
            args: {str(args)},
            kvargs: {str(kvargs)}
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


CACHE_SIMPLE = {}
