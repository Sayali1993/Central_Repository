list_input = ["random_2020-05-04 18:08_string", "random_string_2019-02-12 12:00", "string_random_2019-02-15 16:00"]
print(list_input)
for file_ in list_input:
    print(file_, ' -> ', file_.translate({ord(i): None for i in 'random, string, _'}))