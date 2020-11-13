# using BREAK, CONTINUE and PASS statements
print ("To end this script type 'end' not 'END'. Enjoy!")
count = 0
while True:
    name = input("Please enter your name\n")
    print("You type ", name)
    if name == "end":
        break
    elif name == "END":
        pass
    elif name:
        count += 1
        continue
import datetime
print ("Thanks for your time. \nYou typed a name for ", str(count) + "\n Today is:\n", datetime.date(2020,3,25))


# using pass statement for comment
while True:
    text = input("Enter any text\n")
    if text[0] == "#":
        pass
        print("You typed a comment in python language")
        continue
        pass
    else:
        print("This is the text you typed:\n",text)
    answer = input("Do you want to play again? Y or N\n")
    if (answer =="Y"):
        #print("Please enter Y or N not y or n\n")
        continue
    elif (answer=="y") or (answer== "n"):
        print("Please enter Y or N not y or n")
        break
    else:
        break
print("Made by:\n Hamplus Technologies")
