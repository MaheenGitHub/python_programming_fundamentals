#no need to declare variable before using
name = input("ur name?")
print("hello " + name)

#lemgth of the string
print(len(name))

l = len(name)
print(l)

#type error when concateating different types of variables
# print (name + l)
print ("hello " + name)

#even if user enter name = 1 , it will be considered as a string because of input() 