import re
data_time = re.compile(r'[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]')
list_input = ["random_2020-05-04 18:08_string", "random_string_2019-02-12 12:00", "string_random_2019-02-15 16:00"]
print('\nList : ', list_input, '\n')
for i in list_input:
    data = data_time.search(i)
    print(i, '--> ' + data.group())