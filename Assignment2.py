import re
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
# Initialize matrix
matrix = []
print("Enter the entries rowwise:")
# For user input
for i in range(R):  # A for loop for row entries
    a = []
    for j in range(C):  # A for loop for column entries
        a.append(input())
    matrix.append(a)
print(R,C)
# For printing the matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = " ")
    print()
String = ''
for y in range(C):
    for x in range(R):
        String += matrix[x][y]
print(String)
temp_len = len(String) - len(re.sub(r'\W+.$', '', String))
String1 = re.sub(r'\W+', ' ', String[:-temp_len]) + String[-temp_len:]
String1 = re.sub(r'\d+', ' ', String1[:-temp_len]) + String1[-temp_len:]
print(String1)


