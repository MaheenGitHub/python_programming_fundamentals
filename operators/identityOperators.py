"""
two identity opertors: (compare onject ids/memory location and not values)
is
is not 
"""

print("same values")
a = 5
b = 5 
print("a==b ", a==b)
print("a is b ", a is b)
print("a is not b ", a is not b)
print(id(a) == id(b))
print(id(a),id(b))

# a = 5 at specific memeory address
# for b =5 , same value as a , o new memory address is created
#same memory address for both a and b
# resusing the memory ddress for same data/object in oython
print("different values")
a = 5
b = 6
print(a is b)   #new memory address
print(a is not b)
print(id(a),id(b))

print("when different datatypes")            
a = 5
b = '5' # 0r 5.0
print(a == b)
print(a is b) #false bcz differen value/dataypes

print("int, float,bool are immutable")
a = 5
print(id(a))
a = 6   #reassinging the variabl but still the memoory id changes
print(id(a))
print("here is the catch, 'is' doesnt look t the history of memory")
print(a == a)
print(a is a) # both are now pointing towards '6' , i.e new memory address

c = 10
print(id(c))
c = 15
print(id(c))
print(c is c )