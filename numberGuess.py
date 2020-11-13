import random
print ("Welcome to the number guess game.\n Made by: Hamplus Technologies")
name = input ("Please enter your name\n")
print ("Welcome ", str.upper(name))
print ("I have a number in my mind between 1 and 20, " + str.upper(name) + " can you guess the number?")
number = random.randint(1, 20)
life = 5
answer = input()
guess = 0
if answer == "Yes" or answer == "YES" or answer == "yes" or answer == "y" or answer == "Y":
    print ("You have " + str(life) + " lives")
    for trial in range (1, life+1):
        guess = int(input ("Enter a guess\n"))
        if guess < number:
            print (str.upper(name), "you have a low guess")
            life -= 1
            print ("You still have " + str(life) + " lives remaining")
        elif guess > number:
            print (str.upper(name), "you have a high guess")
            life -= 1
            print ("You still have " + str(life) + " lives remaining")
        else:
            break
elif answer == "No" or answer == "NO" or answer == "no" or answer == "n" or answer == "N":
    print ("You have opted out from playing the game. \nThanks & goodbye", str.upper(name))
else:
    print ("Your answer is not understood by me.\n Please " + str.upper(name) + " can you guess the number?")
    
    
if guess == number:
    print ("Congrats! " + str.upper(name) + " you got the number in my mind")
    print ("The number in my mind is " + str(number))
    print (str.upper(name) + ", you played this game with " + str(life) + " remaining.\n Your guess is " + str(guess))
else:
    print ("Ops!! " + str.upper(name) + " you didn't get the number in my mind")
    print ("The number in my mind is " + str(number))
    print (str.upper(name) + ", you played this game with " + str(life) + " remaining.\n Your guess is " + str(guess))


