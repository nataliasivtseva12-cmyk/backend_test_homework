import time


# Функция time_of_function() примет на вход
# любую другую функцию и засечёт время её выполнения
def time_of_function(func):
    start_time = time.time()
    # Вызываем функцию, полученную в аргументе
    result = func()
    execution_time = round(time.time() - start_time, 3)
    print(f'Время выполнения: {execution_time} сек.')
    # Возвращаем результат выполнения функции, полученной в аргументе
    return result


def sleep_one_sec():
    time.sleep(1)
    return 'Функция sleep_one_sec() завершила вычисления.'


# Вызываем функцию time_of_function(), передаём в аргументе
# объект функции sleep_one_sec (без скобок!)
decorator_result = time_of_function(sleep_one_sec)

# Печатаем результат, который вернула функция time_of_function().
# Но на самом-то деле time_of_function() вернула
# результат выполнения sleep_one_sec(), вызванной внутри декоратора
print(decorator_result)