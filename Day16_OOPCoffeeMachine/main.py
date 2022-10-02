from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


def process_coins():
    total = int(input("# of quarters: ")) * 0.25
    total += int(input("# of dimes: ")) * 0.1
    total += int(input("# of nickels: ")) * 0.05
    total += int(input("# of pennies: ")) * 0.01
    return total

on = True
while on:
    ans = input(f"What would you like? ({Menu().get_items()}): ")
    if ans == "off": 
        on = False
    elif ans == "report":
        coffee_maker.report()
        money_machine.report()
    else: 
        ans = Menu().find_drink(ans)
        
        if coffee_maker.is_resource_sufficient(ans) and money_machine.make_payment(ans.cost):
            coffee_maker.make_coffee(ans)
            
