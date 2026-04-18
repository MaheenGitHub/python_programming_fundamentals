#calcualte BMI  (body mass index)

weight = input("enter weinght: ")
height = input("enter height: ")

bmi = int(weight)/((float(height))**2)
print("the BMI is: " , bmi)

if (bmi < 18.5):
    print('underweight')
    if(bmi < 16):
        print("sever thinness")
    elif(bmi < 17) :
        print("moderate thinness")
    else  :
        print("mild thinness")

elif (bmi < 25) :
    print("normal range")

elif( bmi  <30 ):
    print("overweight (Pre obeese) ")

else :
    print("obese")
    if( bmi < 35) :
        print("class 1")
    elif(bmi < 40) :
        print("class 2")
    else :
        print("class 3")