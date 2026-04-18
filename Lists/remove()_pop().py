num = [1,2,3,4,5,3,6,3]
print(num)

num.remove(3)
#print(num.remove(3))   ERROR
print("remove(n) only first occurence is removed")
print(num)

print("pop() will remove and return the value of last idex")
print("removed value is " , num.pop())
print(num)

