class Item:
    def __init__(self, name, price):
        print("Item constructor")
        self.name = name
        self.price = price

    def sales_tax(self):
        print(f'[Item] Sales tax for {self.name}, price {self.price} is 20%')
        return self.price * 0.2

# For testing purpose
def main():
    my_soap = Item("Hamam", 50)

    print(f'item name: {my_soap.name}')
    print(f'price before tax: {my_soap.price}')
    print(f'sales tax: {my_soap.sales_tax()}')

if __name__ == '__main__':
    main()