import item

class FoodItem(item.Item):
    def __init__(self, name, price, calories):
        print("FoodItem constructor")
        super().__init__(name, price)
        self.calories = calories

# For testing purpose
def main():
    vegetable = FoodItem("Fresh Produce - Tomato", 30, 200)

    print(f'item name: {vegetable.name}')
    print(f'price before tax: {vegetable.price}')
    print(f'calories: {vegetable.calories}')
    print(f'sales tax: {vegetable.sales_tax()}')

if __name__ == '__main__':
    main()
