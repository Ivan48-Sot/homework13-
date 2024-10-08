# 1. Функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print(f'a: {a}, b: {b}, c: {c}')

# Вызовы функции с разным количеством аргументов
print_params()  # без аргументов
print_params(10)  # только a
print_params(10, 'тест')  # a и b
print_params(b=25)  # только b
print_params(c=[1, 2, 3])  # только c

# 2. Распаковка параметров
values_list = [42, 'пример', False]
values_dict = {'a': 100, 'b': 'слово', 'c': None}

print_params(*values_list)  # распаковка списка
print_params(**values_dict)  # распаковка словаря

# 3. Распаковка + отдельные параметры
values_list_2 = ['текст', 3.14]
print_params(*values_list_2, 42)  # распаковка списка + отдельный параметр
