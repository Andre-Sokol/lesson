first = input('первое число: ')
second = input('второе число: ')
third = input('третье число: ')
if first==second and first==third and second==third:
    print(3)
elif first==second or first==third or second==third:
    print(2)
else:
    print(0)