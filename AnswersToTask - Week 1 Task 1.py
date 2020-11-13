print("Answers to online task by Hampo, JohnPaul A.C.")
print()
print("Week 1 Answers")
print("Answer to last week's task No.1\
      Hello Dear! Here is a little task for us in python.\
\
1] Write a program to find the sum of the data structure below\
[[1,2,3],[4,5,6,7],[8,9]]\
\
2] Write a program to convert the tuple to a dictionary where\
name is the key and age is the value. Example: x = ('John', 23, 'm'), ('Peter', 43, 'm')\
then the output will be y = {'John': 23, 'Peter': 43}.")
print()
print("Solution")
print("Task Number 1")
a = [[1,2,3],[4,5,6,7],[8,9]]
print("Using a for loop")
b = []
for i in range(len(a)):
    for j in range(len(a[i])):
        b.append(a[i][j])
print("The sum of the list of lists = ", sum(b))
print()
print("Alternatively: using list comprehension")
c =[sum(a[i]) for i in range(len(a))]
print("The sum of the list of lists = ", sum(c))
print()
print("Or")
print()
d = sum([sum(a[i]) for i in range(len(a))])
print("The sum of the list of lists = ", d)
'''
from itertools import accumulate
datalist = [[1,2,3], [4,5,6,7], [8,9]]
print(list(accumulate([x for x in datalist for x in x]))[8])
print(list(accumulate([x for x in datalist for x in x]))) 'returns a list of progressive sums
'''
print()
print("Solution")
print("Task Number 2")
x = ('John', 23, 'm'), ('Peter', 43, 'm')
print("Using a for loop")
y = dict()
for name, age, sex in x:
    y[name] = age
print("The new dictioary is:\n", y)
print()
print("Alternatively: using dictionary comprehension")
print()
y2 = {name:age for name, age, sex in x}
print("The new dictioary is:\n", y2)
