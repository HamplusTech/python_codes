def divisibleByThree(x):
    if not x / 3 == 0:
        print (x, "is divisible by 3")
    else:
        print (x, "is not divisible by 3")

def divisibleByThree_1(x):
    if  x % 3 == 0:
        print (x, "is divisible by 3")
    else:
        print (x, "is not divisible by 3")

def evenlyDivisibleElement (x, y=list()):
    '''This function prints out the list of integers that
evenly divide an integer from a list of integer'''
    a = list()
    for i in range(len(y)):
        if x % y[i] == 0:
            a.append(y[i])
    return a
        
