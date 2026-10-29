'dictionary stores values in key-value pair,its also mutable {key:value} '



a={
    "name":"sayan",
    "roll":120,
    "age":21
}
numbers = { 2,4,5,6,2,4,5}

print(numbers)
print(type(numbers))

print(a)
print(type(a))

print(a["name"])
print(a["roll"])


'adding a new item'
a["city"]="kolkata"
a["age"]=20

print(a)

'safer method to get values that doesnt give error if key not present'


'print(a["ge"])'

print(a.get("ge"))

'checking if key is present or not'
print("he" in a)

'looping :'

for key in a:
    print(key)

for key in a:
    print(a[key]) 

for value in a.values():
    print(value)

for key , value in a.items():
    print(key , value)


'Frequency Counting'

s='sayan'
freq={}

for ch in s:
    freq[ch]=freq.get(ch,0)+1

print(freq)

'get(key, default) -> means giuve me the value for this key , and if not present then give me default value'