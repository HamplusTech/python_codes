class Rectangle():

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


class Square(Rectangle):

    def __init__(self, length):
        super (Square, self).__init__(length, length)
        #or Rectangle.__init_(length, length)


print("String formating")
name = 'JohnPaul'
age = 24
height = 1.7

print('My name is %s and my age is %d but my height is %f' % (name, age, height))
print()
print('My name is {} and my age is {} but my height is {}'.format(name, age, height))
print()
print(f"My name is {name} and my age is {age} but my height is {height}")      
