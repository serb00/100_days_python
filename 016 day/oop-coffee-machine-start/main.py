from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def turn_on():
    is_on = True
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    while is_on:
        prompt = input(f"What would you like? ({menu.get_items()}):")
        match prompt:
            case "off":
                is_on = False
            case "report":
                coffee_maker.report()
                money_machine.report()
            case _:
                drink = menu.find_drink(prompt)
                if drink is None:
                    print("No such drink, try again")
                if coffee_maker.is_resource_sufficient(drink):
                    if money_machine.make_payment(drink.cost):
                        coffee_maker.make_coffee(drink)


if __name__ == "__main__":
    turn_on()
