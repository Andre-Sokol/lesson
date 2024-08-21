def print_params(a=1, b='строка', c=True):
    print(a, b, c)


#   1. Функция с параметрами по умолчанию
print_params()  # 1
print_params(b=25)
print_params(c=[1, 2, 3])

#   2. Распаковка параметров:
#   Функция print_params() получит 6 параметров в место трёх, результат ошибка.
values_list = [2, 'Dima', False]
values_dict = {'a': 5, 'b': 'Alex', 'c': False}
# print_params(*values_list, **values_dict)

#   3.Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)