#Find out largest number between 3 numbers

try:

    x=int(input("Enter value of x: "))
    y=int(input("Enter value of y: "))
    z=int(input("Enter value of z: "))




    if x>y and x>z:
        print("x is the largest number")
    elif y>z:
        print("y is the largest number")
    else:
        print("z is the largest number")

except:
    print("Invalid Input. Please type a integer value")


