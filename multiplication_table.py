print ("This program prints multiplication table")
stop = int(input("Please enter the number you want to stop at\n"))
for i in range(1,stop+1):
    print (" \n*** ", i , " times ****")
    for j in range(1,13):
        result = i * j
        print (i, " * ", j, " = ", result)
