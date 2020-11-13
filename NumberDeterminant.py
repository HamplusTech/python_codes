#A program to determine what a number is.
number = input("Please enter a number\n")
if number.isalpha():
    print("Ooop!!!! You must enter a numeric value. Either an INTEGER or a FLOAT.")
elif number.isdecimal():
    if int(number) % 2 == 0:
        print("Congrats! You entered an even number")
    elif int(number) % 3 == 0:
        print("Congrats! You entered an odd number")
    else:
        print("Congrats! You entered a prime number")
    print("Congrats! You entered an integer")
elif not number.isdecimal():
    print("Congrats! You entered a float")

print("Thanks for using this program. Written with Love from Hamplus Technologies [Hamplus Hub]")
