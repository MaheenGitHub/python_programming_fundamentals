# num[index : length]

num = [0,1,2,3,4]
print(num)

print("index 1 is", num[1])
print("index -1 is" , num[-1]) # backward indexing starts from -1 unlike forward indexing which starts from 0
print("Length is", len(num))

print("Slicing in List")
print("complete slice of 0: " , num[0:])

print("0 to 5 is" , num[0:5])

print("slice of 1 till 3 is ", num[1:3]) # not 3rd index -> bcz 3 is not index here , but length

print("skipping one digit means step 2 : " , num[0: :2])

