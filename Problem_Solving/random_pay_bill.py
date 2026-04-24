import random

name = input("enter the names separated by comma: ")

print(name)

splited = name.split(',')
print(splited)

print("choice() function")
print(random.choice(splited))

print("by using indxes of the list")
n = len(splited) - 1 
person = random.randint(0 , n)
print(splited[person])
