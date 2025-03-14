
def calculate_discount(price,discount_percent):
    price = int(input("What is the Price of Goods\n"))
    discount_percent = int(input("What is the Price of Goods\n"))/100
    if discount_percent >= 0.2:
        return price + price*discount_percent
    else:
        return price

print(calculate_discount(200,10))