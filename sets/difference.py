set1 ={1,2,3,4,5}
set2 = {4,5,6,7}
set3 = {4,52, 4}

print("set as an arguemnt")
print(set1.difference(set2))

print("list/tuple etc as argumnt is first converted into set")
print(set1.difference([4,5,6,7]))

print("difference update")
set1.difference_update(set2)
print(set1)

print("symmetric difference -> either in set1 or set2 but not in both")
print(set1.symmetric_difference(set2))  
print("formula is: (set1 U set2) - (set1 intersecct set2)")
# not allowed in multiple sets

print("operator XOR ^ for symmetric diff")
print(set1 ^ set2) 
print("^ on multiple sets: " ,set1 ^ set2 ^ set3)

print("symmetric diff update")
set2.symmetric_difference_update(set1)
print(set2)