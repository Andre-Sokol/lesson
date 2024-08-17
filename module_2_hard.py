import random


def castle():
    number = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    insert_1 = random.choice(number)
    return insert_1


insert_1 = castle()
n = ''
for i in range(1, insert_1):
    for j in range(i + 1, insert_1):
        if insert_1 % (i + j) == 0:
            n = n + str(i) + str(j)
print(insert_1, '-', n)
