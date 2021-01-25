from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_machine_on = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while is_machine_on:
    command = input(f"What would you like? ({menu.get_items()}):")
    if command == "report":
        coffee_maker.report()
        money_machine.report()
    elif command == "off":
        is_machine_on = False
    else:
        order = menu.find_drink(command)
        if coffee_maker.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
            coffee_maker.make_coffee(order)
