def number(largest):
    a=largest[0]

    for i in largest:
        if i>a:
            a=i

    return a


result=number([2,5,1,98,101,34])
print("largest:",result)

#Default Arguments in Python

def greet(a="user"):
    print("hello",a)

greet()