from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# print the report
money_machine = MoneyMachine()
money_machine.report()
coffee_maker = CoffeeMaker()
coffee_maker.report()


menu = Menu()
is_on = True
# check resources sufficient?
while is_on:
    options = menu.get_items()
    choice = input(f"what would you like?'({options}):")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        # print(drink)
        is_enough_ingredients = (coffee_maker.is_resource_sufficient(drink))
        is_payment_successful = (money_machine.make_payment(drink.cost))

        # process coins
        # check transaction successful
        if is_enough_ingredients and is_payment_successful:
                coffee_maker.make_coffee(drink)
