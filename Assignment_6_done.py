import os
txt, pdf = ([] for i in range(2))

list_files = ["file1.txt", "file1.pdf", "file1.xlsx", "file1.xls", "file2.txt", "file3.pdf", "file4.mp4", "file2.ppt.txt"]
print("\nList of files : ", list_files)
print("-------------\n")

def sorting_list(lst):

    for file_ in lst:
        name, ext1 = os.path.splitext(file_)
        txt.append(ext1)
        mylist = list(set(txt))
        dic = {}
    for i in range(0, len(mylist)):
        ll = []
        for file1 in lst:
            name, ext = os.path.splitext(file1)
            if mylist[i] == ext:
                ll.append(file1)

        dic[mylist[i]] = ll

    print('Output : ', dic)
    return dic

sorting_list(list_files)



