''' tuple is immutable , but list can be changed  , tupple has () and list [] 
tupple can contains duplicates , different data types values'''

number = (1,5,4,5,6,7)

print(number[1:4])
print(number[::-1])

''' Tuple unpacking '''

a,b,c,d,e,f=number

print(number.count(5))
print(number.index(5))