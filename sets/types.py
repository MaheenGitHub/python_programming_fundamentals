set1 = {1,2,3,4}
set2 = {4,5,6,7,8}

print("disjoint sets -> zero intersection -> nothing common")
print(set1.isdisjoint(set2))

print("subset -> set1 is a subset of set2 if set2 conitains every elemnt of set1")
print(set1.issubset(set2))

print("operator for subset <= dor : ",set1 <= set2 )

print("superset -> set1 is the superset of set2 if set1 contains every elemnt of set2 ")
print(set1.issuperset(set2))

print("operator for superset >= dor : ",set1 >= set2 )

set2.clear()    # empty set 
del(set2)       # DELETED THE SET AS WELL   
