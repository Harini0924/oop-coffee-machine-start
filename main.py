from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#objects
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
#menu_item =MenuItem()







want_to_place_order =True
while (want_to_place_order==True):
    options = menu.get_items()
    drink_option = input(f"What would you like? {options}: ")
    if (drink_option == "off"):
        want_to_place_order = False
    elif(drink_option =="report"):
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(drink_option)
        if(coffee_maker.is_resource_sufficient(drink)):
            money_per_drink = drink.cost
            if(money_machine.make_payment(money_per_drink)):
                coffee_maker.make_coffee(drink)



