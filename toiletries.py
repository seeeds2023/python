import item

class Toiletries(item.Item):
    def __init__(self, name, price, skin_type):
        print("Toiletries constructor")
        super().__init__(name, price)
        self.skin_type = skin_type

    def info(self):
        return "Made In India"
    
# utility function to create a soap
def hamam_soap():
    return Toiletries("Hamam Soap", 30, "OilySkin")

# For testing purpose
def main():
    my_soap = Toiletries("Bath Soap", 30, "DrySkin")

    print(f'item name: {my_soap.name}')
    print(f'price before tax: {my_soap.price}')
    print(f'skin type: {my_soap.skin_type}')
    print(f'sales tax: {my_soap.sales_tax()}')
    print(f'info: {my_soap.info()}')

if __name__ == '__main__':
    main()
