numCar = input("Please enter how many cars do you have\n")
try:
    numCar = int(numCar)
    if numCar.__neg__():
        print("You have entered a negative number")
    elif numCar >= 3:
        print("You have many cars")
    else:
        print ("You have not many cars")
except:
    print("You haven't entered a number")
