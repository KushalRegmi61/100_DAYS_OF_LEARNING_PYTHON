from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
cofemaker = CoffeeMaker()
menu = Menu()
money = MoneyMachine()
while True:
    choice = input(f"What you would like?{menu.get_items()}").lower()
    if choice == "report":
        cofemaker.report()
        money.report()
    elif choice =="off":
        print("Thank You! Please visit again....")
        break
    else:
        drink = menu.find_drink(choice)
        if cofemaker.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                cofemaker.make_coffee(drink)
               

                
        