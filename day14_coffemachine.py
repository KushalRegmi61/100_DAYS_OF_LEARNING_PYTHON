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

# TODO 1   printing the resources after the coffee is prepared
def report(RESOURCES, MONEY): 
    print("Water:", RESOURCES['water'],"\n Milk:",RESOURCES['milk'], "\n Coffee:" ,RESOURCES['coffee'])
    print("available money", MONEY)
def user_choice():
    return input("“What would you like? (espresso/latte/cappuccino):”")   
# TODO CHECKING IF THE RESOURCES AVAILABLE ARE SUFFFICIENT OF NOT  
def check_resources(DICT):
    for ingredient, quantity in DICT.items():
        if quantity < resources.get(ingredient, 0):
            return True
        else:
            print(f"Sorry! Not enough {ingredient}")
            
            return False
# TODO UPDATE RESCOURCES IF THE ITEMS IS PREPARED
def update_resources(update):
    # resources['water'] = resources['water'] -update['water']
    # resources['milk'] = resources['milk']- update['milk']
    # resources['coffee'] = resources['coffee'] - update['coffee']
    for items in update:
        resources[items] -= update[items]
            
# TODO CALCULATE THE AMOUNT REQUIRED 
def cost_comparision():
    """"use to compare cost and refund  """
    quater = int(input("How many quarters(1 q = 0.25$)"))
    dimes = int(input("how many dimes:(1 DIMES = 0.1$)"))
    return (quater * .25 + dimes* .1)
# TODO USING WHILE LOOP FOR THE FINAL OUTPUT
cond1 = True
money = 0 
while True:
    choice = user_choice()  
    if choice == 'report':
        report(resources,money)
    elif choice == 'off':
        cond1 = False
    else:
        price = int(MENU[choice]['cost'])    
        items_ingridents = MENU[choice]['ingredients']
        cond = check_resources(items_ingridents)
        # if check_recource function is true then this block of code is executed
        if cond:
            user_price = cost_comparision()
            if user_price >= price:
                print("Here is your change:",user_price-price, "$" )
                print("Enjoy your !",choice)
                update_resources(items_ingridents)
                money = price;
                
            else:
                print("Not enough money for:  ", c, "your $",user_price,"amount is refunded")
        # else:
        #     print("not enough resources")
                
            
    
                     
   
