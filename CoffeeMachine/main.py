MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

profit = 0.0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def resources_sufficient(drink):
    for i in drink["ingredients"]:
        if resources[i] <= drink["ingredients"][i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True

def process_coins():
    total = int(input("# of quarters: ")) * 0.25
    total += int(input("# of dimes: ")) * 0.1
    total += int(input("# of nickels: ")) * 0.05
    total += int(input("# of pennies: ")) * 0.01
    return total

def check_transaction(drink, total):
    cost = drink["cost"]
    if cost > total:
        print("sorry that's not enough money. Money refunded.")
    if total > cost:
        print(f"Here is ${round(total-cost, 2)} in change.")
    global profit
    profit += round(cost, 2)

def make_coffee(name):
    for key in drink["ingredients"]:
        resources[key] -= drink["ingredients"][key]
    print(f"Here is your {name}!")


on = True
while on:
    ans = input("What would you like? (espresso/latte/cappucino): ")
    if ans == "off":
        on = False
    elif ans == "report":
        print(f"water: {resources['water']} ml")
        print(f"milk: {resources['milk']} ml")
        print(f"coffee: {resources['coffee']} g")
        print(f"money: ${profit}")
    else:
        drink = MENU[ans]
        if resources_sufficient(drink):
            check_transaction(drink, process_coins())
            make_coffee(ans)
    