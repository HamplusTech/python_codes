print("Static and Dynamic Systems")
print()
x = [2, 4, 6, 8, 10]
print("Static System")
ys = []
for n in range(len(x)):
    ys.append(2 * x[n] + 8 * x[n] + 17)
print()
print("x", x)
print("y", ys)
print()
print("Dynamic System")
yd = []
for n in range(len(x)):
    yd.append(2 * x[n-1] + 8 * x[n] + 17)
print()
print("x", x)
print("y", yd)
print()
print("Thanks")
print("Hamplus Technologies aka Hamplus Hub")
