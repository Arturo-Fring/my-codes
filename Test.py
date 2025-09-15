# decorator function

# Вызвали func_decorator, передали ссылку на функцию some_func
# Далее объявили внутреннию функцию wrapper, которая принимает неограниченное число аргументов
# Она вывела что-то
# Она (wrapper) распаковала свои аргументы в функцию func

# вернулась ссылка на wrapper
# мы ещё записали в переменную r
# А значит, при помощи r мы вызываем wrapper, передавая в него
# неограниченное число параметров, которые распаковываются в нашу функцию и она вызывается

# А если нужен результат функции? Куда его? По идее его должна возвращать
# функция wrapper. Ведь мы вызвали r()
# То есть вызвали r() а значит wrapper(), wrapper() просто выполняет функцию
# но ведь wrapper может что-то вернуть - поэтому добавляем в него return от результата func

def func_decorator(func):

    def wrapper(*args, **kwargs):
        print("-b-")
        res = func(*args, **kwargs)
        print("-a-")
        return res
    return wrapper


@func_decorator
def some_func(a, b, c, s):
    # print(a, b, c, s)
    return a+b+c+s

# r = func_decorator(some_func)
# hi = r("title", 'bob', 'fex', 'k')
# print(hi)


# А как по-другому?
result = some_func('Arthur ', 'Gosha ', 'Danil ', 'Sergey')
print(result)
