##print ("This program checks for the maximum of two numbers")
##max_num = 0
##first_number = int(input("Please enter the first number\n"))
##second_number = int(input("Please enter the second number\n"))
##if first_number > second_number:
##    max_num = first_number
##else:
##    max_num = second_number
##print ("The maximum number of ", first_number, " and ", second_number, " is ", max_num)


##a = 10
##if a > 11:
##    print ("Greater")
##elif a == 10:
##    print("Equal")
##else:
##    print("Lesser")


###Using Try and Except
##data = input("Please enter a number\n")
##try:
##    data = float(data)
##    print("You entered a number! Horay!")
##except:
##    print("Oops! You entered a non number")


'''A pay computation program'''
hours = input ("Enter Hours: ")
try:
    hours = float(hours)
    rate = input ("Enter rate: ")
    try:
        rate = float(rate)
        if hours > 40:
            pay = 40 * rate + (hours - 40) * 1.5 * rate
        else:
            pay = rate *hours
        print("Pay: ", pay)
    except:
        print ("Error, please enter numeric input as rate")
except:
    print ("Error, please enter numeric input as hours")
