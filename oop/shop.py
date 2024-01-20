from rice import ponni_rice
from milk import aavin_milk
from toiletries import hamam_soap

def checkout(cart):
    amount = 0
    for i in cart:
        amount = amount + (i.price + i.sales_tax())
    return amount

def choose_items():
    cart = []
    cart.append(ponni_rice())
    cart.append(aavin_milk())
    cart.append(hamam_soap())
    return cart

def shop():
    cart = choose_items()
    total_amount = checkout(cart)
    print(f'total amount of shopped items: {total_amount}')

def main():
    shop()

if __name__ == '__main__':
    main()