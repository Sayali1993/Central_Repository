import random
import datetime
import re
from random import randrange
log_File = open("log.txt", "w")
list_ERROR, list_WARNING, list_INFO, list_DEBUG, list_CRITICAL = ([] for i in range(5))

random_list = ["ERROR", "WARNING", "INFO", "DEBUG", "CRITICAL"]

def random_date(start , l):
   current = start
   while l >= 0:
      curr = current + datetime.timedelta(minutes=randrange(60))
      yield curr
      l-=1

startDate = datetime.datetime(2019, 5, 20, 13, 00)

for x in random_date(startDate, 29):
  log_File.writelines(random.choice(random_list) + " :  " + str(random.randint(120, 130)) + '  ' + x.strftime("%d %B %Y %H:%M") + '\n')
log_File.close()

log_File = open("log.txt", "r")
count1 = 0
temp_dict = {}

for line in log_File:
    words = line.split()
    for word in words:
        if random_list[0] == word:
            list_ERROR.append(line)
        elif random_list[1] == word:
            list_WARNING.append(line)
        elif random_list[2] == word:
            list_INFO.append(line)
        elif random_list[3] == word:
            list_DEBUG.append(line)
        elif random_list[4] == word:
            list_CRITICAL.append(line)

def getDuplicatesWithCount(list_all: []):
    empty_list=[]
    dictOfElems = dict()
    for elements in list_all:
        words_list = elements.split()
        for word1 in words_list:
            for k in re.findall(r'(?<!\d)\d{3}(?!\d)', word1):
                empty_list.append(k)
    print(empty_list)
    for i in empty_list:
        if i in dictOfElems:
            dictOfElems[i] += 1
        else:
            dictOfElems[i] = 1
    pr = 1
    global summation
    summation = 0
    for key, value in dictOfElems.items():
         pr = int(key) * value
         summation += pr
    return dictOfElems

print("{} occurs {} time".format(random_list[0], len(list_ERROR)))

error_dic = getDuplicatesWithCount(list_ERROR)
for key, value in error_dic.items():
    print("ERROR CODE", key, ': occurs', value, "times.")
print("ERROR Codes summation:", summation, '\n')

print("{} occurs {} time".format(random_list[1], len(list_WARNING)))
warning_dic = getDuplicatesWithCount(list_WARNING)
for key, value in warning_dic.items():
    print("WARNING CODE", key, ': occurs', value, "times.")
print("WARNING Codes summation:", summation, '\n')

print("{} occurs {} time".format(random_list[2], len(list_INFO)))
info_dic = getDuplicatesWithCount(list_INFO)
for key, value in info_dic.items():
    print("INFO CODE", key, ': occurs', value, "times.")
print("INFO Codes summation:", summation, '\n')

print("{} occurs {} time".format(random_list[3], len(list_DEBUG)))
debug_dic = getDuplicatesWithCount(list_DEBUG)
for key, value in debug_dic.items():
    print("DEBUG CODE", key, ': occurs', value, "times.")
print("DEBUG Codes summation:", summation, '\n')

print("{} occurs {} time".format(random_list[4], len(list_CRITICAL)))
critical_dic = getDuplicatesWithCount(list_CRITICAL)
for key, value in critical_dic.items():
    print("CRITICAL CODE", key, ': occurs', value, "times.")
print("CRITICAL Codes summation:", summation, '\n')

log_File.close()