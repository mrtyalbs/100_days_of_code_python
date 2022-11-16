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


# Check resources sufficient?
def is_resources_enough(order):
    """This function checks if resources are sufficient"""
    for item in order:
        if order[item] > resources[item]:
            print(f"Sorry there is not enough {item}. ")
            return False
    return True

# Calculate the value of coins
def value_of_coins():
    """This returns total value of inserted coins."""
    print("Please insert coins. ")
    quarter = int(input("How many quarters?: "))
    dime = int(input("How many dimes?: "))
    nickel = int(input("How many nickels?: "))
    penny = int(input("How many pennies?: "))
    value_of_coins = 0.25 * quarter + 0.1 * dime + 0.05 * nickel + 0.01 * penny

    return value_of_coins

def report():
    print(f"""
    Water\t:\t{resources["water"]}\tml
    Milk\t:\t{resources["milk"]}\tml
    Coffee\t:\t{resources["coffee"]}\tml
    Money\t:\t${money}
    """)
def make_coffee():
    for item in resources:
        item -= drink["ingredients"][item]
    print(f"Here is your {customer_choice}. Enjoy! ")

money = 0
is_on = True

# Prompt user (what would u like?)
while is_on:
    customer_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if customer_choice == "off":
        is_on = False
    elif customer_choice == "report":
        report()
        is_on = False
    else:
        drink = MENU[customer_choice]

        if is_resources_enough(drink["ingredients"]):
            print(f"{customer_choice} is ${drink['cost']} ")
            value_of_coins = value_of_coins()
            if value_of_coins >= drink["cost"]:
                money += value_of_coins
                resources["water"] -= drink["ingredients"]["water"]
                resources["milk"] -= drink["ingredients"]["milk"]
                resources["coffee"] -= drink["ingredients"]["coffee"]
                report()
                print(f"Here is your {customer_choice} ☕. Enjoy! ")
            else:
                print("Sorry that's not enough money. Money refunded. ")
                is_on = False
        else:
            is_on = False


