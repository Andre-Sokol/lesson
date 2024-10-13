first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# высчитываем разницу длин строк из списков first и second, если их длины не равны.
first_result = (len(i) - len(j) for i, j in zip(first, second) if len(i) != len(j))

# результаты сравнения длин строк в одинаковых позициях из списков first и second.
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

print(list(first_result))
print(list(second_result))
