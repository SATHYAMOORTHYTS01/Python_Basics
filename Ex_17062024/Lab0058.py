def make_pizza(*toppings):  # * - ANY number of arguments
    for topping in toppings:
        print(topping,end="\n")

mani = make_pizza("tomato", "onion", "capsicum")
sathya = make_pizza("olive", "mushroom")


