import random

# generate pseudo random numbers and not truly random

print("----1. Generating Random Numbers (Basic)----")
# randint(a,b) where both a and b are inclusinve
print("randint(a,b) return a <= x <= b")
#print(randint(1,3))  ERROR
print(random.randint(1,3))


# randrange(a,b) where a->inclusive and b->exclusive
print("randrange(a,b) return a <= x < b")
print(random.randrange(1,3))

print("randrange(a,b,step) -> random number with a step e.g 1,3,5,7,9")
print(random.randrange(1,10,2))


# random -> return a floaing point num
print("random return 0.0 <= x < 1.0")
print(random.random())

#uniform return floating point number
print("uniform return floating a.0 <= x < b.0")
print(random.uniform(1,3))

print("----2. Sequence Manipulation----")
print("choice(list) -> random number from list")
l = [3,4,22,4,2]
print(random.choice(l))

print("choices(list, weights=None , k=1)")

print("sample(list, k) -> returns k 'unique' elements")
print(random.sample(l ,3))

print("shuffle(list) ->Shuffle the list randomnly")
print(random.shuffle(l)) # None 

shuffled = random.shuffle(l)
print(shuffled) #None

random.shuffle(l)
print(l)


"""
remaining
3. Statistical Distributions
4. Internal State Control
"""
import random

items = ['apple', 'banana', 'cherry']

# Example 1: Simple random selection of 5 items (duplicates allowed)
pick = random.choices(items, k=5)

# Example 2: Weighted selection
# Here, 'apple' is much more likely to be picked than 'cherry'
weights = [10, 2, 1] 
weighted_pick = random.choices(items, weights=weights, k=5)

print(f"Simple selection: {pick}")
print(f"Weighted selection: {weighted_pick}")