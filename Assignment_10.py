import os.path
import shutil
path = input('\nEnter the path [e.g, C:\..] to create files : ')
isExist = os.path.exists(path)
while True:
    if isExist:
        try:
            no_of_files = int(input("Enter the number of files you want to create: "))
            total_data_size = int(input("Enter the total size of data which will be divided into {} files : "
                               .format(no_of_files)))
            each_file_size = total_data_size/no_of_files
            stat = shutil.disk_usage(path)
            if each_file_size > stat[2]:
                print("* No sufficient memory *")
            else:
                for i in range(no_of_files):
                    file_name = (path + "file_" + str(i) + ".txt")
                    file = open(file_name, "w")
                    string = "S" * int(each_file_size)
                    file.write(string)
                    file.close()
                print("\n*", no_of_files, "files are successfully created at location", path)
                print('* Each file has data size', each_file_size)
            break

        except:
            print("* ERROR -> Enter the valid input *\n")
    else:
        print("* ERROR -> Path not exist. Please enter the valid path to create files.")
        break

