print("Answers to online task by Hampo, JohnPaul A.C.")
print()
print("Week 2 Answers")
print("Data = [2,4,2,1,4,5,6,1,11]. Multiply the elements in the list \
using:\
a) for loop\
b) list comprehension\
c) map function")
print()
print("Using for loop")
print()
Data = [2,4,2,1,4,5,6,1,11]
data_new = []
for element in Data:
    data_new.append(element * 2)
print("The list elements multiplied by 2 is = ", data_new)
print()
print("Using list comprehension")
Data = [2,4,2,1,4,5,6,1,11]
data_lc = [2 * element for element in Data]
print("The list elements multiplied by 2 is = ", data_lc)
print()
print("Using map function")
Data = [2,4,2,1,4,5,6,1,11]
data_map = list(map(lambda x: 2*x, Data))
print("The list elements multiplied by 2 is = ", data_map)
