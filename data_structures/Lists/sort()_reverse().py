num = [2,4,3,5,1,2]
print(num.sort()) # None -> no return type

sorted = num.sort() # None 
print(sorted)

num.sort() #original list is modified
print(num)

print("Reverse function")
num.reverse()
print(num)

print("For Mixed list")
mixed = ["maheen" , 2, True , 9.3]
#mixed.sort() # error
print("Sorting the mixed list will give erorr")
mixed.reverse() 
print("mixed list can be reversed" , mixed)
