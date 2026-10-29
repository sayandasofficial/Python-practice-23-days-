'take input 2d array and Print each element using nested loops'

print("enter rows and colums(dimension) : ")
rows , cols = map(int,input().split())

matrix=[]

for i in range(rows):
    print("enter row",i+1,"element: ")
    row=list(map(int,input().split()))
    matrix.append(row)

for i in range(rows):
    for j in range(cols):
        print(matrix[i][j])


