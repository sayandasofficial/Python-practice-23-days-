matrix = [
    [1,2,3],[4,5,6],[7,8,9]
]

a=len(matrix)
b=len(matrix[1])

print("row",a)
print("column",b)

for i in range(len(matrix)):
    for j in range(len(matrix[1])):
        print(matrix[i][j])
