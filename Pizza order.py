# These are the variables
pizza_price = 12.50
delivery = 7
pizza_topping = 0.75

# The menu for the pizzas
print( "Hello, Welcome to Le Cheesy Penny")
print("Our menu has multiple toppings you can choose from or if you don't want toppings then that can be arranged \n""Out menu of toppings are comprised of: \n""pepperoni \n""Hawaiian \n""Meat Lovers \n""Veggie pizza")


# Have another variable equal to the input
num_pizzas = int(input("How many pizzas are you planning on ordering today?"))
toppings = input("What toppings would you like?")
other_pizza = int(input("How many pizzas with toppings would you like?"))


# Set this variable so it times the number of pizzas and price
order_total = num_pizzas * pizza_price + other_pizza * pizza_topping


# Use the "if" statement to calculate for free pizzas
if num_pizzas < 3:
    print("The cost for delivery will be ${}".format(delivery))
    order_total += delivery
else:
    print("Free delivery for 3 or more pizzas!")

# Print the full total cost of everything
total_pizzas = num_pizzas + other_pizza
print("You order of {} pizzas, {} with {} brings the total cost to ${}".format(total_pizzas, other_pizza,toppings,order_total))
