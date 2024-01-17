#BMI = (Weight in Pounds / (Height in inchs x Height in inchs))
name = input("Enter your name: ")
weight = int(input("Enter your weight(lbs): "))
height = int(input("Enter your height(inchs): "))

def bmi_cal(weight, height):
    bmi = (weight * 703 / (height * height))

    return bmi

vai = bmi_cal(weight, height)

print(name,"your BMI is: ",vai)

def mishu(vai):
    if vai > 0:
        if (vai<18.5):
            print("you are underwight")
        elif (vai<= 24.9):
            print("you are normal weight")
        elif (vai<= 34.9):
            print("you are high weight")
        elif (vai<= 39.9):
            print("you are very high weight")
        else:
            print("you are severly high weight")

mishu(vai)
        
        


    

        
        