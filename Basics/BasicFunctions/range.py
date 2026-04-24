"""
range(start_inclusive , stop_exclusive , step_size)

start and stop size are optional

by default 
start - > 0
step seize -> 1

"""


alphabets = ['a' , 'b', 'c']
for i in range(0, len(alphabets) ) :
    print(i)

print("can be used witout loops too")
a = range(3)
print(a[1])

print("-ve step size with positive range")
b = range(2,15,-3)
for i in b :
    print(i)

print("step seze can not be zeor")
# c = range(3,4,0)  # Error

print("other examples")
d = range(10, 0, -1) 
# e = range(10,0) 

# i + k step size