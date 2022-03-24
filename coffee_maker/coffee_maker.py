from extra import MENU, resources, logo


def amount():
    """calculates money/coin input"""
    global profit
    global choice
    print("Please insert coins")
    quantity_quarter = int(input("How many quarters?: "))
    quantity_dime = int(input("How many dimes?: "))
    quantity_nickle = int(input("How many nickles?: "))
    quantity_penny = int(input("How many pennies?: "))

    total_quarter = 0.25 * quantity_quarter
    total_dime = 0.10 * quantity_dime
    total_nickle = 0.05 * quantity_nickle
    total_penny = 0.01 * quantity_penny

    sum_amount = total_quarter + total_dime + total_nickle + total_penny
    if sum_amount < MENU[choice]["cost"]:
        print("Insufficient Fund")
        print(f"You will be refunded {sum_amount}")
    elif sum_amount >= MENU[choice]["cost"]:
        profit += MENU[choice]["cost"]
        change = sum_amount - MENU[choice]["cost"]
        print(f"Your change is ${round(change, 2)}")
        print("Here is your coffee ☕")
        print("Thank you for patronizing us")
        print("")


def espresso():
    """checks if resources are enough in the machine for the espresso order"""

    espresso_water = MENU["espresso"]["ingredients"]["water"]
    espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]
    if resources["water"] >= espresso_water and resources["coffee"] >= espresso_coffee:
        resources["water"] -= espresso_water
        resources["coffee"] -= espresso_coffee
        return True
    else:
        return False


def latte():
    """checks if resources are enough in the machine for the latte order"""

    latte_water = MENU["latte"]["ingredients"]["water"]
    latte_milk = MENU["latte"]["ingredients"]["milk"]
    latte_coffee = MENU["latte"]["ingredients"]["coffee"]
    if resources["water"] >= latte_water and resources["coffee"] >= latte_coffee and resources["milk"] >= latte_milk:
        resources["water"] -= latte_water
        resources["milk"] -= latte_milk
        resources["coffee"] -= latte_coffee
        return True
    else:
        return False


def cappuccino():
    """checks if resources are enough in the machine for the cappuccino order"""

    cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
    cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
    cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
    if resources["water"] >= cappuccino_water and resources["coffee"] >= cappuccino_coffee and resources["milk"] >= cappuccino_milk:
        resources["water"] -= cappuccino_water
        resources["milk"] -= cappuccino_milk
        resources["coffee"] -= cappuccino_coffee
        return True
    else:
        return False


print(logo)
profit = 0

flow = True
while flow:
    choice = input("What will you like to have? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${round(profit, 2)}")
    elif choice == "espresso":
        the_espresso = espresso()
        if the_espresso:
            amount()
        else:
            print("Insufficient Resources")
    elif choice == "latte":
        the_latte = latte()
        if the_latte:
            amount()
        else:
            print("Insufficient Resources")
    elif choice == "cappuccino":
        the_cappuccino = cappuccino()
        if the_cappuccino:
            amount()
        else:
            print("Insufficient Resources")
    elif choice == "off":
        flow = False
