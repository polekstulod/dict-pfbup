class Customers:
    greeting = "Welcome to the Coffee Palace"

    def __init__(self, name, beverage, food, total):
        self.name = name
        self.beverage = beverage
        self.food = food
        self.total = total


c_1 = Customers("Samirah", "Ice coffee latte", "Cinnamon roll", 225)
c_2 = Customers("Jerry", "Caramel Macchiato", "Glazed doughnut", 230)

print(Customers.greeting)
print(c_1.beverage)
print(c_2.food)
