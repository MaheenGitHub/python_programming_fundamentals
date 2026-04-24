"""
list -> for loop -> square of each element -> print list
"""

nums = [0,1,2,3]
print(f"orginal list: {nums}")

print("modify original list")
for num in nums :
    nums[num] = num ** 2
print(f"Squared list: {nums}")

print("using append and new list")
result = []
for num in nums :
    sq = num ** 2
    result.append(sq)
print(f"result new list: {result}")