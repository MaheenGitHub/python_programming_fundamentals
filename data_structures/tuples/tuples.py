"""
tuples -> store multiple items 
round brackets ()
immutable
execution spped fast
unchanged order
tuple = (single value with comma)
mixed values possible
"""

tuple1 = ( 10, 4,2,-4 )
tuple2 = ( "he" , "she")

print("Multiple mixed values possible")
tuple3 = ( 1, "mixed" , 22, True)
print(tuple3)


print("indexing & slicing in tuple ")
print(tuple3[2])
print(tuple3[1 : 3])
print(tuple3[:: 2])


print("immutabe , no assignmnt no remove")
# tuple3[2] = 88  # ERROR


print("single tuplle without comma doesnt exist")
tuple4 = (10)  
print("tuple4 = (10)  gives ", type(tuple4))

tuple5 = (10,)
print("tuple5 = (10)  gives ", type(tuple5))

