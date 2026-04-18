"""
two types: (to check a chr, string ,value, dic , tuple ,set is present in a sequence)

in
not in
"""

name = "maheen"
print("string maheen")
print("\"m\" :", "m" in name)
print("\'m\' :",'m' in name)
print("\"M\" :","M" in name)    # case sensitive
print("\"he\" :","he" in name)
print("not \"m\" :", "m" not in name)

l = [0,1,2,3,4,5]
print("list [0,1,2,3,4,5] ")
print("1 ", 1 in l)
