# DECORATORS #
## by Luchanos ##

## Блок 1
### Easy

1. Написать простую функцию, которая на вход принимает строку ('test') и целое число (3), а возвращает строку вида 'testTESTtest' - исходную строку, умноженную на 3, в разном регистре.
2. Записать эту функцию в произвольную переменную. Напечатать эту переменную на экран. Что вы видите?
3. Вызвать функцию суммирования через переменную, в которую вы только что её записали.

### Medium

1. Написать функцию, которая на вход будет принимать произвольное количество аргументов и возвращать их сумму.
2. В сигнатуре функции объявить 4 обязательных аргумента, но оставить возможность передавать в неё сколько угодно
дополнительных аргументов. Попробуйте вызвать функцию в следующих ситуациях и объясните результат:
   - прокинуть в функцию только 1 аргумент
   - прокинуть аргументы таким образом, чтобы обязательный аргумент был передан одновременно позиционно и по ключу
   - создать кортеж со значениями и распаковать его при вызове функции с помощью *
   - создать словарь со значениями и распаковать его при вызове функции с помощью * и **: что наблюдаете? Почему?

### Hard

1. Модифицировать функцию таким образом, чтобы для суммирования брались только обязательные аргументы, первые
2 аргумента из дополнительных позиционных аргументов и любой аргумент из дополнительных аргументов (если они есть),
переданных по ключу (если они есть).

## Блок 2

### Easy

1. Реализовать счетчик, который будет увеличиваться каждый раз, когда у нас осуществляется запуск функции суммирования.

### Medium

1. Написать ещё несколько произвольных функций (3-4 штуки) и решить задачу со счетчиком аналогично той, котоая была
решена для запуска функции суммирования.
2. Написать функцию, внутри которой у нас будет объявляться наша функция суммирования и возвращаться в качестве 
результата работы из объемлющей функции.
3. Попробуйте вызвать написанную функцию и сохраните результат её работы в переменную. Напечатайте результат на экран.
Что наблюдаете?
4. Осуществите вызов функции суммирования из полученной переменной.

### Hard

4. Перенесите глобальный счетчик на уровень объемлющей функции. Будет ли работать наш код? Если да, то как поменялся 
смысл написанного кода? Если нет, то что надо изменить, чтобы всё заработало?

## Блок 3

Задача 1

1.1 Написать декоратор, который перед запуском произвольной функции с произвольным набором аргументов будет показывать
в консоли сообщение "Покупайте наших котиков!" и возвращать результат запущенной функции.
1.2 Параметризовать декоратор таким образом, чтобы сообщение, печатаемое перед выполнением функции можно было задавать
как параметр во время декорирования.

Задача 2
2.1 Написать декоратор, который внутри себя выполнял бы функцию и возвращал бы результат её работы в случае успешного
выполнения. В случае возникновения ошибки во время выполнения функции нужно сделать так, чтобы выполнение функции было
повторено ещё раз с теми же самыми аргументами, но не более 10 раз. Если после последней попытки функцию так и не 
удастся выполнить успешно, то бросать исключение.
2.2 Параметризовать декоратор таким образом, чтобы количество попыток выполнения функции можно было задавать как 
параметр во время декорирования.

Задача 3

3.1 Написать кэширующий декоратор. Суть в том, что если декорируемая функция будет запущена с теми параметрами с 
которыми она уже запускалась - брать результат из кэша и не производить повторное выполнение функции.
3.2 Сделать так, чтобы информация в кэше была актуальной не более 10 секунд. Предусмотреть механизм автоматической
очистки кэша в процессе выполнения функций.
3.3 Параметризовать время кэширования в декораторе.

Задача 4

4.1 Написать декоратор, который бы измерял время работы функции и печатал бы его на экран.
4.2 Доработать декоратор таким образом, чтобы в логах было название запускаемой функции помимо времени исполнения.
4.3 Доработать декоратор так, чтобы запись лога для функции велась в файл, путь к которому нужно было бы задавать
во время декорирования, как параметр.

Задача 5

После решения задач написать функцию и задекорировать её сразу несколькими из созданных декораторов и посмотреть 
на результат и суметь объяснить его. Потом поменять порядок декорирования и проделать то же самое.

Задача 6

6.1 Написать декоратор, который будет запрашивать у пользователя пароль при попытке функции осуществить вызов. Если 
введён верный пароль, то функция будет выполнена и вернется результат её работы. Если нет - в консоли появляется 
соответствующее сообщение.
6.2 Параметризовать декоратор таким образом, чтобы можно было задавать индивидуальный пароль для каждой декорируемой
функции.

Задача 7

7.1 Написать декоратор, который после выполнения функции будет возвращать результат и записывать его в текстовый файл.
7.2 Модернизировать декоратор таким образом, чтобы можно было не только осуществлять запись в файл, но и в целом 
производить любую операцию логирования или оповещения.