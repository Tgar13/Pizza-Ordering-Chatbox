print("Hello, my name is Alex your virtual assistant. I will help you order a pizza!")
print("I am going to ask you a few questions. After typing an answer, press enter.")
userName = input("\nEnter your name:  ")
print("\nHello, " + userName + ". Nice to meet you!")
size = input ("\nWhat size do you want? Enter small, medium, or large: ")
flavor = input ("\nEnter flavor of pizza: " )
crustType = input("\nWhat type of crust do you want: ")
quantity = input("\nHow many of these do you want to order: ")
quantity = int(quantity) 
method = input("\nIs this carryout or delivery:  ")
salesTax = 1.1
pizzaCost = 14.99
total = (pizzaCost * quantity) * salesTax
print("-------------------")
print("Thank you, ", userName, ", for your order.")
print("Your, ", quantity, size, flavor, "pizza with", crustType, "crust cost", "${:,.2f}".format(total) + ".")
