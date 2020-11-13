print("Answers to online task by Hampo, JohnPaul A.C.")
print()
print("Week 1 Answers - Task 3")
print("""Answer to last week's task No.1\
      Hello Dear! Here is a little weekend task for us in python.\
Consider the data structures below:
prices = {
    "box_of_spaghetti" : 4,
    "lasagna"  : 5,
    "hamburger" : 2
   }
quantity = {
    "box_of_spaghetti" : 6,
    "lasagna"  : 10,
    "hamburger" : 0
    }
1] Calculate how much was spent on products with a price of 5 naira or more.
2] Calculate how much was spent on products that cost less than 5 naira?""")
print()
print("Solution")
print("Task Number 1")
prices = {
    "box_of_spaghetti" : 4,
    "lasagna"  : 5,
    "hamburger" : 2
   }
quantity = {
    "box_of_spaghetti" : 6,
    "lasagna"  : 10,
    "hamburger" : 0
    }
print()
items_price = {item:amount for (item, amount) in list(prices.items()) if amount >= 5}
amount_spent = [quantity[item] * prices[item] for item,price in list(items_price.items())]
print(items_price)
print(sum(amount_spent))
print("The amount spent on product with price of N5 or more is \n", sum(amount_spent))
print()
print("Solution")
print("Task Number 2")
items_price_less = {item:amount for (item, amount) in list(prices.items()) if amount < 5}
amount_spent_less = [quantity[item] * prices[item] for item,price in list(items_price_less.items())]
print(items_price_less)
print(sum(amount_spent_less))
print("The amount spent on product with price of less than N5 is \n", sum(amount_spent_less))

