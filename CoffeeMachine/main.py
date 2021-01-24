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

money = 0

machine_power_on = True


def is_resources_sufficient(order):
    """"Returns True when order can be made, False if ingredients are insufficient."""
    ingredients = MENU[order]['ingredients']
    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    else:
        return True


def make_transaction(order):
    print("Please insert coins.")
    quarter = int(input("how many quarters?: "))
    dime = int(input("how many dimes?: "))
    nickle = int(input("how many nickles?: "))
    penny = int(input("how many pennies?: "))
    insert_money = 0.25 * quarter + 0.1 * dime + 0.05 * nickle + 0.01 * penny
    order_cost = MENU[order]['cost']

    if insert_money < order_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        if insert_money > order_cost:
            print(f'Here is ${round(insert_money - order_cost, 2)} dollars in change.')
        global money
        money += order_cost
        return True


def make_coffee(order):
    """"Deduct the required ingredients from the resources."""
    ingredients = MENU[order]['ingredients']
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]

    print(f"Here is your {order} ☕️. Enjoy!")


def machine(input_command):
    if input_command == 'off':
        global machine_power_on
        machine_power_on = False
    elif input_command == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif input_command in MENU:
        if is_resources_sufficient(input_command):
            if make_transaction(input_command):
                make_coffee(input_command)
    else:
        print("Please input another command.")


while machine_power_on:
    command = input("What would you like? (espresso/latte/cappuccino): ")
    machine(command)
