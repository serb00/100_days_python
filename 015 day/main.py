from decimal import *

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
    "money": 0,
}

turned_off = False
getcontext().prec = 7


def read_integer(prompt="Enter an integer: "):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("That's not a valid integer! Please try again.")


def report():
    global resources
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def check_resources(coffee):
    global resources
    ingredients = coffee["ingredients"]
    for ingredient in ingredients:
        print(ingredient)
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
        else:
            return True


def check_transaction(coffee, cash):
    global resources
    coffee_price = Decimal(coffee["cost"])
    if cash > coffee_price:
        change = cash - coffee_price
        resources["money"] += coffee_price
        print(f"Here is ${change:.2f} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")


def process_coins(coffee):
    print("Please insert coins.")
    quarters = read_integer("How many quarters?")
    dimes = read_integer("How many dimes?")
    nickles = read_integer("How many nickles?")
    pennies = read_integer("How many pennies?")
    cash = Decimal(0.25) * quarters + Decimal(0.1) * dimes + Decimal(0.05) * nickles + Decimal(0.01) * pennies
    if check_transaction(coffee, cash):
        return True
    else:
        return False


def make_coffee(coffee):
    global resources
    ingredients = coffee["ingredients"]
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    return True


def order(prompt):
    if prompt not in MENU:
        print("We do not have such drink, please try again.")
        return False

    coffee = MENU[prompt]
    if check_resources(coffee):
        if process_coins(coffee):
            if make_coffee(coffee):
                print(f"Here is your {prompt} ☕️. Enjoy!")
            else:
                print("Something went wrong. Please call: +1 (123) 999-99-99")


def turn_off():
    global turned_off
    turned_off = True


def turn_on():
    # Display main menu
    while not turned_off:
        user_input = input("What would you like? (espresso/latte/cappuccino):")
        match user_input:
            case "report":
                report()
            case "off":
                turn_off()
            case "refill":
                refill()
            case _:
                order(user_input)


def refill():
    global resources
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100
    print("All ingredients refilled.")


if __name__ == "__main__":
    turn_on()
