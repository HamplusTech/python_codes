def quad (x):
    y = (x * x) - (5 * x) + 3
    return y

def root1(a, b, c ):
    import math
    x1 = (-b + math.sqrt((b * b) - (4 * a * c)) )/ (2 * a)
    return x1

def root2 (a, b, c):
    import math
    x1 = (-b - math.sqrt((b * b) - (4 * a * c)) )/ (2 * a)
    return x1
