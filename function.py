
def calculate_discount(price,discount_percent):
    if discount_percent >= 0.2:
        return price + price*discount_percent
    else:
        return price

price = int(input("What is the Price of Goods\n"))
discount_percent = int(input("What is the Price of Goods\n"))/100
Total_amount =(calculate_discount(price,discount_percent))
print(Total_amount)