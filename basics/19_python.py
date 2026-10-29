#List Comprehension : List comprehension is a shorter way to create a list using a loop

square = [i*i for i in range(1,6)]
print(square)

condition = [i for i in range (1,10) if i%2==0]
print(condition)