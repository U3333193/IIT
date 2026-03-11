print("Welcome to the Python Coffee Shop!")

customer_name = input("What is your name? ")
print("Hello, " + customer_name + "! Let's order some coffee.")
student = input ("Are you a Student? (yes/no): ")


price_coffee = 3.50
price_latte = 4.00
price_mocha = 4.50 #addidng Mocha
total_cost_all_orders = 0 #Variables for another order
order = True #Variables for another order

while order:  # Keep ordering until user says no
    print("\n--- New Order ---")  # Separator between orders
    print("Coffee: $" + str(price_coffee))
    print("Latte: $" + str(price_latte))
    print("Mocha: $" + str(price_mocha)) #Mocha price

    choice = input("What would you like to order? (coffee/latte/mocha): ").lower()
 
    if choice == "coffee":
         cost = price_coffee
    elif choice == "latte":
         cost = price_latte
    elif choice == "mocha": #Mocha choice argument
         cost = price_mocha
    else:
         print("Sorry, we do not have that.")
         cost = 0
 
    quantity = int(input("How many cups would you like? "))
 
    total_cost = cost * quantity
 
    if quantity > 1:
         print("You get a discount of $1.00!")
         total_cost -= 1.00

    #student discount
    if student.lower() == "yes":
        print("You get 10% discount!")
        discount = total_cost * 0.10
        total_cost = total_cost - discount

    # Ask if they want to continue
    another = input("Would you like to order something else? (yes/no): ").lower()
    if another != "yes":
        order = False

print("Your total is: $" + str(total_cost))
print("Thank you, " + customer_name + "! Please come again.")
