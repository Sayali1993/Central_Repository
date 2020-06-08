import os.path
import shutil
path = input('\nEnter the path [e.g, C:/..] to create files : ')
isExist = os.path.exists(path)
if isExist:
    no_of_files = int(input("Enter number of files you want to create: "))
    total_size = no_of_files * 2048
    stat = shutil.disk_usage(path)
    if total_size > stat[2]:
        print("* No sufficient memory *")
    else:
        for i in range(no_of_files):
            file_name = (path + "file_" + str(i) + ".txt")
            file = open(file_name, "w")
            string = "S" * 2048
            file.write(string)
            file.close()
        print("* ", no_of_files, " files are successfully created at location", path)
else:
    print("Path not exist. Please enter the valid path to create files.")
