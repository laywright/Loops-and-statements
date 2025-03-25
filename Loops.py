def calculate_discount(price, discount_percentage):
    if discount_percentage >= 20:
        return price - (price * discount_percentage / 100)
    else:
        return price
try:
    price = float(input("Enter the price: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    final_price = calculate_discount(price, discount_percentage)

    if final_price == price:
        print("No discount applied. The final price remains: ",final_price)
    else:
        print("Discount applied! The final price is:", final_price)

except ValueError:
    print("Invalid input. Please enter numerical values for price and discount.")
except ZeroDivisionError:
    print("Invalid input. Discount percentage cannot be zero.")