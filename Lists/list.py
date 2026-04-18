#sequence data type

roll_no = [1,2,3,4,5]
print(roll_no)
print(roll_no[1])

print("list can be of mixed type, hexagenous, ordered, dynamiclly sized, mutable")

mixed_list = ["maheen" , 31, "OOP" , 3.5]
print(mixed_list)

roll_no[0] = 0
print("changed index value as mutable ")
print(roll_no)

roll_no[1:4] = [45,46,47]
print(roll_no)

"""
import random

print("choice(list) -> random number from list")
l = [3,4,22,4,2]
print(random.choice(l))

print("shuffle(list) ->Shuffle the list randomnly")
print(random.shuffle(l)) # None 

shuffled = random.shuffle(l)
print(shuffled) #None

random.shuffle(l)
print(l)

"""