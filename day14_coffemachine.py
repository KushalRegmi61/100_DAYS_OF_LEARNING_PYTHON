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

def report(RESOURCES, MONEY):
    print(RESOURCES)
    print(MONEY)
def user_choice():
    return input("“What would you like? (espresso/latte/cappuccino):”")   
# TODO CHECKING IF THE RESOURCES AVAILABLE ARE SUFFFICIENT OF NOT  
def check_resources(DICT):
    for ingredient, quantity in DICT.items():
        if quantity < resources.get(ingredient, 0):
            return True
        else:
            return False
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
    c = user_choice()
    price = int(MENU[c]['cost'])  
    if c == 'report':
        report(resources,money)
    items_ingridents = MENU[c]['ingredients']
    cond = check_resources(items_ingridents)
    user_price = cost_comparision()
    # if check_recource function is true then this block of code is executed
    if cond:
        if user_price >= price:
            print("Here is your change:",user_price-price, "$" )
            print("Enjoy your c!")
        else:
            print("Not enough money for: your $ ", c, "amount is refunded")
    else:
        print("not enough resources")
                
            
    
                     
   
