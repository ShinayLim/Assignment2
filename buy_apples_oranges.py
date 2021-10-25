apple_price = 20
orange_price = 25

number_of_apples_you_want_to_buy = int(input("How many apple/s you want to add in your cart?: "))
total_amount_of_apple_price = number_of_apples_you_want_to_buy * apple_price
print ("Total amount of item/s: " + str(total_amount_of_apple_price))

number_of_oranges_you_want_to_buy = int(input("How many orange/s you want to add in your cart?: "))
total_amount_of_orange_price = number_of_oranges_you_want_to_buy * orange_price
print ("Total amount of item/s: " + str(total_amount_of_orange_price))

total_amount = total_amount_of_apple_price + total_amount_of_orange_price

print(f"\nThe total amount is {total_amount}")

answer = input("Do you want to continue your transaction? Type yes or no: ")
if answer == "yes":
    print("The parcel is on your way, please prepare your cash with the amount of " + str(total_amount))
elif answer == "no":
    print("Thank you for your time. Please come again.")