name = str (input("Enter your name: "))
print ("Good day "+ str(name), "please enjoy your shopping.")

money = int(input("How much money do you have on hand?: "))
price_of_apple = int(input("What is the current cost of an apple?: "))
you_can_buy = money//price_of_apple
your_change = money%price_of_apple

print(f"You can buy {you_can_buy} apples and your change is {your_change} pesos.")