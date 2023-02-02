from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffeemaker = CoffeeMaker()
machine = MoneyMachine()

ON = True

while ON:
    option = menu.get_items()
    choose = input(f"what would you like? ({option}):")

    if choose == "off":
        ON = False
    elif choose == "report":
        coffeemaker.report()
        machine.report()
    else:
        drink = menu.find_drink(choose)
        if coffeemaker.is_resource_sufficient(drink):
            if machine.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)





