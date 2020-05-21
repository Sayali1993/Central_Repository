import os
import psutil

print("\nYour current memory status of drives in GB: ", '\n')
print("-------------------------------------------")
os.system('df -h')

while True:
    path = input('\nEnter the path of disk you want to select [e.g.,C: or D: ] : ')
    try:
        obj_Disk = psutil.disk_usage(path)
        total = (obj_Disk.total / (1024.0 ** 3))
        used_pes = obj_Disk.percent
        break
    except:
        print(">>ERROR: Enter the valid input..(E.g,'C:')")
while True:
    try:
         per = abs(int(input("\nHow much you want to fill in (1 - 100)% ? : ")))
         if per <= used_pes:
            print("Memory is already ", round(used_pes), ' % occupied \n')
            break
         else:
            rem_per = per-used_pes
            rem_gb = (rem_per/100)*total
            global in_bytes
            in_bytes = rem_gb * (1024.0 ** 3)
            file = open(path + '/' + 'newfile.txt', "wb")
            bytes_in_file = in_bytes
            file.seek(int(bytes_in_file) - 1)
            file.write(b"\0")
            file.close()
            print("\nDisk", path, "is updated with", per, "%")
            print("-------------------------------------------")
            os.system('df -h')
            os.path.exists(path+'/'+'newfile.txt')
            os.remove(path+'/'+'newfile.txt')

         break
    except:
         print(">>ERROR: Enter the Valid input range from 1 - 100.")
