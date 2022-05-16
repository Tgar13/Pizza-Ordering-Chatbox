print("Hello, my name is Alex your virtual assistant. I will help you order a pizza!")
print("I am going to ask you a few questions. After typing an answer, press enter.")
userName = input("\nEnter your name:  ")
while (len(userName) == 0):
    userName = input("Please enter your name:  ")
if userName == "Professor Quigley":
    print("\nMy creator, " + userName + ". Pleasure to serve you!")
else:
    print("\nHello, " + userName + ". Nice to meet you!")
size = input ("\nWhat size do you want? Enter small, medium, or large: ")
while (len(size) == 0):
    size = input("Please specify pizza size:  ")
while size.lower() != "small" and size.lower() != "medium" and size.lower() != "large":
    size = input("Invalid value. Please enter small, medium, or large: ") 
flavor = input ("\nEnter flavor of pizza: " )
while (len(flavor) == 0):
    flavor = input("Please specify pizza flavor:  ")
crustType = input("\nWhat type of crust do you want: ")
while (len(crustType) == 0):
    crustType = input("Please specify crust type:  ")
quantity = input("\nHow many of these do you want to order: ")
while not quantity.isdigit():
    quantity = input("\nValue not recognized. Please enter a numeric value: ")
quantity = int(quantity)
method = input("\nIs this carryout or delivery:  ")
while method.lower() != "delivery" and method.lower() != "carryout" and method.lower() != "carry out":
    method = input("Invalid value. Please specify carryout or delivery:  ")    
salesTax = 1.1
pizzaCost = 14.99
if size.lower() == "small":
    pizzaCost = 8.99
elif size.lower() == "medium":
    pizzaCost = 14.99
elif size.lower() == "large":
    pizzaCost = 17.99
if method.lower() == "delivery":
    deliveryFee = 5
else:
    deliveryFee = 0
total = (pizzaCost * quantity) * salesTax + deliveryFee
print("\n-------------------")
print("Thank you, ", userName, ", for your order.")
print("Your, ", quantity, size, flavor, "pizza with", crustType, "crust cost", "${:,.2f}".format(total) + ".")
if total >= 50:
    print("\nCongratulations, you've been awarded a $10 off coupon for your next order!")
else:
    print("\nOrders over $50 will receive a free $10 off coupon!")
print("-------------------")