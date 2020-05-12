import re
input_file = open("Readme1.txt", "r")
list_statwith_a,list_not_statwith,list_endwith,list_not_endwith,list_contain_a,list_not_contain_a, list_reg_ex = ([] for i in range(7))
count = 0
count1 = 0
for line in input_file:
    words = line.split()
    for word in words:
        if word.startswith('a'):
            list_statwith_a.append(word)
        else:
            list_not_statwith.append(word)
        if word.endswith('e'):
            list_endwith.append(word)
        else:
            list_not_endwith.append(word)
        if 'a' in word:
            list_contain_a.append(word)
        else:
            list_not_contain_a.append(word)
        reg_ex = re.match(r"^.*\b(is)\b.*$", word)
        if reg_ex:
            count += 1
        else:
            count1 += 1
input_file.close()
dict = {}
dict["words starting with string a"] = list_statwith_a
dict["word count starting with string a"] = len(list_statwith_a)
dict["words not starting with string  a"] = list_not_statwith
dict["word count not starting with string a"] = len(list_not_statwith)
dict["words ending string e"] = list_endwith
dict["word count ending with string e"] = len(list_endwith)
dict["words containing a"] = list_contain_a
dict["word count contain with string a"] = len(list_contain_a)
dict["word  not ending with string e"] = list_not_endwith
dict["word count not ending with string e"] = len(list_not_endwith)
dict["word not containing with string a"]= list_not_contain_a
dict["Word count not containing string a"] = len(list_not_contain_a)
dict["<^.*\b(is)\b.*$> will disaply the count of is word"] = count
dict["word count with not regex <^.*\b(is)\b.*$>"] = count1
print(dict)