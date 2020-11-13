print("Dynamic Systems")
t = [1,2,3,4,5,6,7]
x = 10
n = [1,2,3,4,5,6,7]
y1, y2, y3, y4 = [], [], [], []
for n in range(len(n)):
    y1.append( x * n + (6 * x * (n-2)))
    y2.append( 4 * x * (n+7) + x * n)
    
for t in range(len(t)):
    y3.append( x * (t + 1))
    y4.append( t * x * (t) + x * (t-1))
print()
print(y1, "\n", y2, "\n", y3, "\n", y4)
print("Thanks")
print("Hamplus Technologies aka Hamplus Hub")
