'''for i in range(1,7):
    print(i)

'range(start, stop, step)'

a=int(input())

for i in range(1,11,a):
    print(i)

'Counting backwards'

for i in range(10,0,-1):
    print(i)'''


'loop through a list'

numbers=[2,3,4,5,6,7]
for i in range(len(numbers)):
    print(i)

'print only even numbers between 1 to 10 but break if value is == 5 and also skip the value 2'

for i in range(1,11):
    if(i%2==0):
        if(i==2):
            continue
        else:
            print("even",i)
    else:
        if(i==5):
            break
        else:
            print("odd",i)
        