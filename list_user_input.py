#List operation with user input
a = list()
for i in range(5):
    b = int(input("Please enter integer in the list\n"))
    a.append(b)
print (a)
print("Maximum = ", max(a))
print ("Minimum = ", min(a))
print ("Average = " , sum(a) *0.5)
print ("The Count = ", len(a))
tempSort = sorted(a)
print ("Sorted of the list = ", tempSort, "\n Original of the list = ", a)
