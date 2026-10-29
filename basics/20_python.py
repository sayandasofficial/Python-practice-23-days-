#map()

def mul(n):
    return n*2

numbers =list(map(int,input().split()))
print("your inputed numbers are :",numbers)

result = map(mul,numbers)
print("your doubled numbers are ",list(result))