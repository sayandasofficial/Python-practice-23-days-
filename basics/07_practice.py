"Set is a collection that doesnot stores duplicate values, a set does not support normal indexing"
"like lists it is basically used to check if that value is present or not "

number={2,4,5,6,7,2,3,5}

a=[2,3,4,4,4,5,6,4]
b=set(a)
print(type(b))

print(29 in number)

"Have I already encountered this value?"

a= [10,20,30,20,30]

seen=set()

for i in a:
    if i in seen: 
        print("duplicate",i)
    seen.add(i)

''' here i = 10 and seen is firstly empty so it will return false '''

"removing numbers"

print(seen)
seen.remove(30)
print(seen)

"remove() → gives an error if the element doesn't exist"
"discard() → doesn't give an error"

"Set Operations:"

z={1,2,3,4}
y={3,4,5,6}

print("union: ", z|y)

print("intersection : ", z&y)