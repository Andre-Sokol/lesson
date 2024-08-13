my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = my_list[-0]
b = len(my_list)
while True:
    for c in my_list:
        if c > 0:
            print(c)
        elif c < 0 or b > 12:
            break
    break

