
def calculate_discount(price,discount_percent):
    ## the price and discount_percentage here is different from the price and discount_percentage in the try and except 
    ## if the discount is greater than 20%
    if discount_percent >= 0.2:
        return price + price*discount_percent
    else:
        return price # give back the normal price 

try:
    price = float(input("What is the Price of Goods?:\n"))
    discount_percent = float(input("What is the discount for the Goods?:\n"))/100
    Total_amount =(calculate_discount(price,discount_percent))
    print(Total_amount)
except ValueError:
    print("Invalid input. Please enter numerical values for price and discount percentage.")