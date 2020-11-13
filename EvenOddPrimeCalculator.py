# A program to print the even numbers in the first 100 poaitive integer
numbers = range(1,101)
odd, even, prime = list(), list(), list([2,3,5])
for number in numbers:
    if not number % 2:
        even.append(number)
    elif number % 2:
        odd.append(number)
for number in numbers:
    for pnumber in prime:
        if not number % pnumber :
            prime.append(number)
print("The even numbers in the first 100 positive integers are\n", even)
print()
print("The odd numbers in the first 100 positive integers are\n", odd)
print()
print("The prime numbers in the first 100 positive integers are\n", prime)
