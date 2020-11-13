print("Answers to online task by Hampo, JohnPaul A.C.")
print()
print("Week 1 Answers - Task 2")
print("Answer to last week's task No.1\
      Hello Dear! Here is a little weekend task for us in python.\
Consider the data structure below:\
menu = {'meal_1': 'Spaghetti',\
 'meal_2': 'Fries',\
 'meal_3': 'Cheeseburger',\
 'meal_4': 'Lasagna',\
 'meal_5': 'Soup',\
 'meal_6': ['Pancakes', 'Ice-cream', 'Tiramisu']}\
1] Create a new dictionary that contains the first five meals as keys and assign the following\
      five values as prices (in dollars): 10, 5, 8, 12, 5. Start by Price_list = {}.\
2] Create a JSON in which the values of the keys of menu dictionary have a dictionary\
      showing the recipe for the values.)")
print()
print("Solution")
print("Task Number 1")
menu = {'meal_1': 'Spaghetti',
 'meal_2': 'Fries',
 'meal_3': 'Cheeseburger',
 'meal_4': 'Lasagna',
 'meal_5': 'Soup',
 'meal_6': ['Pancakes', 'Ice-cream', 'Tiramisu']}
print("Using Dictionary comprehension")
prices = [10, 5, 8, 12, 5]
Price_list = {list(menu.values())[i] : prices[i] for i in range(len(prices))}
print("The menu by price dictionary is \n", Price_list)
print()
print("Solution")
print("Task Number 2")
print("A JSON is a list of dictionary. JSON stands for Java Script Object Notation ")
print("Observing the dictionary called menu, the value of meal_6 is a list, hence for \
simplicity I change the list to a value as shown below: \n")
menu_new = menu
menu_new["meal_6"] = "Fruits"
print("The new menu without a list value is :", menu_new)
ingredient_sample = ["ingredient1", "ingredient2", "ingredient2", "..."]
ingredients_menu = [{value: ingredient_sample for key, value in list(menu_new.items())}]
print("The JSON showing ingredients is:\n", ingredients_menu)
