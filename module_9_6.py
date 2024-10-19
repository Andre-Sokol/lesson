def all_variants(text):
    for len_ in range(len(text)):
        for l in range(len(text) - len_):
            yield text[l:l + len_ + 1]


a = all_variants("abc")
for i in a:
    print(i)