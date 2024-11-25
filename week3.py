def calculate_discount(price, discount_percent):
    #Calculate the final price after applying discount if discount is 20% or higher.
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompting the user for inputs
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculating the final price
final_price = calculate_discount(original_price, discount_percentage)

# Displaying the result
if final_price == original_price:
    print(f"No discount applied. The original price is ${original_price:.2f}.")
else:
    print(f"The final price after applying the discount is ${final_price:.2f}.")