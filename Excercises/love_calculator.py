ur_name = (input("enter ur name: ")).lower()
crush_name = (input("enter ur crush name: ")).lower()

name = ur_name + crush_name
count1 = 0
if ('t' in name ) :
    count1 +=  name.count('t')
if ('r' in name ) :
    count1 +=  name.count('r')
if ('u' in name ) :
    count1 += name.count('u')
if ('e' in name ) :
    count1 += name.count('e')

count2 = 0
if ('l' in name ) :
    count2 +=  name.count('l')
if ('o' in name ) :
    count2 +=  name.count('o')
if ('v' in name ) :
    count2 += name.count('v')
if ('e' in name ) :
    count2 += name.count('e')

count = int(str(count1) + str(count2))

if (count < 10 ) :
    print("phaki love")
elif (count >= 40 and count <= 80 ):
    print("okayish love")
elif (count > 90 ):
    print("coke and mentos love")
else :
    print(f"ur love score is {count}")

"""
simpler logic

t = name.count('t')
r = name.count('r')
u = name.count('u')
e = name.count('e')

true = t + r + u + e

love_score = int(str(true) + str(love))

"""