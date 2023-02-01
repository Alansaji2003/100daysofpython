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
    "milk":  200,
    "coffee": 100,
    "Money": 0,
}


def check(x):
    if x == "espresso":
        if MENU["espresso"]["ingredients"]["water"] >= resources["water"]:
            print("Sorry there is not enough water.")
            return False
        elif MENU["espresso"]["ingredients"]["coffee"] >= resources["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
        else:
            return True
    if x == "latte":
        if MENU["latte"]["ingredients"]["water"] >= resources["water"]:
            print("Sorry there is not enough water.")
            return False
        elif MENU["latte"]["ingredients"]["coffee"] >= resources["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
        elif MENU["latte"]["ingredients"]["milk"] >= resources["milk"]:
            print("Sorry there is not enough milk.")
            return False
        else:
            return True
    if x == "cappuccino":
        if MENU["cappuccino"]["ingredients"]["water"] >= resources["water"]:
            print("Sorry there is not enough water.")
            return False
        elif MENU["cappuccino"]["ingredients"]["coffee"] >= resources["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
        elif MENU["cappuccino"]["ingredients"]["milk"] >= resources["milk"]:
            print("Sorry there is not enough milk.")
            return False
        else:
            return True

profit = 0


def count(y):
    global profit
    print("Please insert coins")
    q = int(input("How many quarters "))
    d = int(input("How many dimes "))
    n = int(input("How many nickels "))
    p = int(input("How many pennies "))
    total = q*0.25 + d*0.1 + n*0.05 + p*0.01
    profit += total
    resources["Money"] = profit
    return total


def use(x):
    if x == "espresso":
        resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
    elif x == "latte":
        resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
        resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
    else:
        resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
        resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]


OFF = False

while not OFF:

    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "espresso":
        c = check(choice)
        if not c:
            OFF = True
        else:
            a = count(choice)
            if a > MENU["espresso"]["cost"]:
                change = a - MENU["espresso"]["cost"]
                print(f"Here is your change ${change}")
                print("ENJOY YOUR ESPRESSO ☕")
                use(choice)
            elif MENU["espresso"]["cost"] > a:
                print(f"Sorry cash is not enough, here is your refund ${a}")
            else:
                print("ENJOY YOUR ESPRESSO ☕")

    elif choice == "latte":
        c = check(choice)
        if not c:
            OFF = True
        else:
            a = count(choice)
            if a > MENU["latte"]["cost"]:
                change = a - MENU["latte"]["cost"]
                print(f"Here is your change ${change}")
                print("ENJOY YOUR LATTE ☕")
                use(choice)
            elif MENU["latte"]["cost"] > a:
                print(f"Sorry cash is not enough, here is your refund ${a}")
            else:
                print("ENJOY YOUR LATTE ☕")

    elif choice == "cappuccino":
        c = check(choice)
        if not c:
            OFF = True
        else:
            a = count(choice)
            if a > MENU["cappuccino"]["cost"]:
                change = a - MENU["cappuccino"]["cost"]
                print(f"Here is your change ${change}")
                print("ENJOY YOUR CAPPUCCINO ☕")
                use(choice)
            elif MENU["cappuccino"]["cost"] > a:
                print(f"Sorry cash is not enough, here is your refund ${a}")
            else:
                print("ENJOY YOUR CAPPUCCINO ☕")

    elif choice == "off":
        print("MACHINE TURNED OFF")
        OFF = True
    elif choice == "report":
        for i in resources:
            print(i, ":", resources[i])
    else:
        print("Error")
