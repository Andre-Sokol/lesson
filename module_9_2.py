first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(l) for l in first_strings if len(l) >=5]
second_result = [(a, b) for a in first_strings for b in second_strings if len(a) == len(b)]
third_result = {l: len(l) for l in first_strings + second_strings if len(l)%2 == 0}
print(first_result)
print(second_result)
print(third_result)