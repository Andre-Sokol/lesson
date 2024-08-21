def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = [2, 'Dima', False]
values_dict = {'a': 5, 'b': 'Alex', 'c': False}
print_params(*values_list, **values_dict)