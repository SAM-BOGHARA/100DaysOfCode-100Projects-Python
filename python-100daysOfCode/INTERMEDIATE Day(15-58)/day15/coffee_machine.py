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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resources_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            is_enough = False
    return is_enough


def process_coins():
    '''Returns the total calculated from coins inserted'''
    print("Please insert coins!")
    total = int(input('how many quarters? :> ')) * 0.25
    total += int(input('how many dimes? :> ')) * 0.1
    total += int(input('how many nickels? :> ')) * 0.05
    total += int(input('how many pennnies? :> ')) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change_amount = round(money_received - drink_cost, 2)
        print(f"Here is ${change_amount} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry thats not enough money!.Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    '''deduct the required ingredients from the resources'''
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


is_on = True

while is_on:
    choice = input("What would you like? (espresso(1.5$)/latte(2.5$)/cappuccino(3$)):> ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if resources_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
