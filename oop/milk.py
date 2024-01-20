import food_item as fi

class Milk(fi.FoodItem):
    def __init__(self, name, price, calories, type):
        print("Milk constructor")
        super().__init__(name, price, calories)
        self.type = type

    def sales_tax(self):
        print(f'[Milk] Sales tax for {self.name} with price {self.price} is 10%')
        return self.price * 0.1
    
    def expiration(self):
        return "1 Week from Date of Package"


# utility function to create a milk packet
def aavin_milk():
    return Milk("Aavin", 50, 60, "Pasteurized")

# For testing purpose
def main():
    my_milk = Milk("Aavin", 30, 60, "Pasteurized")

    print(f'item name: {my_milk.name}')
    print(f'price before tax: {my_milk.price}')
    print(f'calories: {my_milk.calories}')
    print(f'type: {my_milk.type}')
    print(f'sales tax: {my_milk.sales_tax()}')
    print(f'expiration: {my_milk.expiration()}')

if __name__ == '__main__':
    main()
