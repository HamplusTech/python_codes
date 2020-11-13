print ("Welcome. you can calculate the Count, Sum, Mean, Median & Mode of numbers entered by you\n")
Count = 0
Sum = 0
Max = 0
Min = 0
Mean = 0
Median = 0
Mode = 0
numberList = list()
number = input ("Please how many numbers do you want to type?\n")
for a in range(1,int(number)+1):
    userInput = int(input("Enter an integer\n"))
    numberList.append(userInput)

Count = len(numberList)
Sum = sum(numberList)
Max = max(numberList)
Min = min(numberList)
Mean = Sum/Count

print ("The Count of the entered integers is\nCount = ", Count)
print ("The Sum of the entered integers is\nSum = ", Sum)
print ("The Maximum of the entered integers is\nMax = ", Max)
print ("The Minimum of the entered integers is\nMin = ", Min)
print ("The Mean of the entered integers is\nMean = ", Mean)
