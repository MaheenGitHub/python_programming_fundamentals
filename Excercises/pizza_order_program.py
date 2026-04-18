size = int(input("enter 1 for small, 2 for medium and 3 for large piza: "))


if ( size == 1):
    price = 100
elif (size == 2) :
    price = 200
else :
    price = 300 

pep = input("Do you want peporoni?Enter Y/N: ")

if( pep == 'y' or pep == 'Y') :
    if (size == 1 ):
        price += 30 
    else :
        price += 50

cheese = input("Do u want cheese? Enter Y/N: ")

if (cheese == 'y' or cheese == 'Y') :
    price += 20

print(f"Total price is {price}")
