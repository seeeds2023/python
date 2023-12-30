import food_item as fi

class Rice(fi.FoodItem):
    def __init__(self, name, price, calories, variety):
        print("Rice constructor")
        super().__init__(name, price, calories)
        self.variety = variety


# Utility function to create a rice object
def ponni_rice():
    return Rice("Ponni", 100, 170, "Par-Boiled")


# For testing purpose
def main():
    my_rice = Rice("Ponni", 70, 170, "Par-Boiled")

    print(f'item name: {my_rice.name}')
    print(f'price before tax: {my_rice.price}')
    print(f'calories: {my_rice.calories}')
    print(f'variety: {my_rice.variety}')
    print(f'sales tax: {my_rice.sales_tax()}')

if __name__ == '__main__':
    main()
