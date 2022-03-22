MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

import os


def function_espresso():
    global bank
    global water
    global coffee
    quarters = int(input("Quarters "))
    dimes = int(input("Dimes "))
    nickels = int(input("Nickels "))
    pennies = int(input("Pennies "))
    change = (((quarters * .25) + (dimes * .1) + (nickels * .05) + (pennies * .01)) - 1.5).__round__(2)
    if change < .00:
        print("not enough money paid, no coffee for you!")
    elif change >= .00:
        bank += 1.5
        print(f"Here is your ${change}.")
        if water > 50 and coffee > 18:
            water -= 50
            coffee -= 18
            print("Enjoy your Espresso!")
        else:
            bank -= 1.5
            print("We are out of resources, your money has been refunded.")

def function_latte():
    global bank
    global water
    global milk
    global coffee
    quarters = int(input("Quarters "))
    dimes = int(input("Dimes "))
    nickels = int(input("Nickels "))
    pennies = int(input("Pennies "))
    change = (((quarters * .25) + (dimes * .1) + (nickels * .05) + (pennies * .01)) - 2.5).__round__(2)
    if change < .00:
        print("not enough money paid, no coffee for you!")
    elif change >= .00:
        bank += 2.5
        print(f"Here is your ${change}.")
        if water > 200 and milk > 150 and coffee > 24:
            water -= 200
            milk -= 150
            coffee -= 24
            print("Enjoy your Latte!")
        else:
            bank -= 2.5
            print("We are out of resources, your money has been refunded.")


def function_cappuccino():
    global bank
    global water
    global milk
    global coffee
    quarters = int(input("Quarters "))
    dimes = int(input("Dimes "))
    nickels = int(input("Nickels "))
    pennies = int(input("Pennies "))
    change = (((quarters * .25) + (dimes * .1) + (nickels * .05) + (pennies * .01)) - 3.0).__round__(2)
    if change < .00:
        print("not enough money paid, no coffee for you!")
    elif change >= .00:
        bank += 3.
        print(f"Here is your ${change}.")
        if water > 200 and milk > 150 and coffee > 24:
            water -= 250
            milk -= 100
            coffee -= 24
            print("Enjoy your Cappuccino!")
        else:
            bank -= 3.0
            print("We are out of resources, your money has been refunded.")



bank = 0
water = 300
milk = 200
coffee = 100

make_coffee = True

while make_coffee == True:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if coffee_choice == "espresso":
        print("That will be $1.50.")
        function_espresso()
        os.system('clear')
    elif coffee_choice == "latte":
        print("That will be $2.50")
        function_latte()
        os.system('clear')
    elif coffee_choice == "cappuccino":
        print("That will be $3.00")
        function_cappuccino()
        os.system('clear')
    elif coffee_choice == "report":
        print(f"There is {water}ml water, {milk}ml milk and {coffee}g coffee left. There is ${bank} in the coffee machine.")
        os.system('clear')
    elif coffee_choice == "off":
        make_coffee = False
