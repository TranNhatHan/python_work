pizzas = ["hawaiian", "neapolitan", "pepperoni"]
friend_pizzas = pizzas[:]

pizzas.append("calabrian")
friend_pizzas.append("greek")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend’s favorite pizzas are")
for friend_pizza in friend_pizzas:
    print(friend_pizza)