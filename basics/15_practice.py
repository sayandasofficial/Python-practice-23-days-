'''def introduce(name,age):
    print(name)
    print(age)

introduce("sayan",21)'''


def introduce(a,b):
    return a+b


result = introduce(2,4)
print(result)

'A function can return a Boolean'

def func(n):
    return n%2==0

print(func(3))

def calculate(a,b):
    return a+b,a-b

sum_result , diff_result =calculate(5,6)
print(sum_result)
print(diff_result)