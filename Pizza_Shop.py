# Your code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausages", "olives", "anchovies", "mushrooms"]
print(toppings)
prices = [2, 6, 1, 3, 2, 7, 2]
print(prices)
#occurence of $2 slices
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
#length of toppings
num_pizza = len(toppings)
print(num_pizza)
print("\n")
#2D List of Pizzas_and_Prices
Pizzas_and_Prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausages"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(Pizzas_and_Prices)
print("\n")
#Sort The New List
Pizzas_and_Prices.sort()
print(Pizzas_and_Prices)
print("\n")
#First Element
cheapest_pizza = Pizzas_and_Prices[0]
print(cheapest_pizza)
#LAst Element
priciest_pizza = Pizzas_and_Prices[-1]
print(priciest_pizza)
print("\n")
#Remove Anchovies Pizza
Pizzas_and_Prices.pop()
print(Pizzas_and_Prices)