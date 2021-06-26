from sys import exit

Machine = 1
Active = 1
resources = {'water': 1000,
             'milk': 750,
             'coffee': 500,
             'money': 0}
go = 1
stop = 0


def resource_checker(check_water=0, check_coffee=0, check_milk=0):
    signal = go
    if check_water > resources['water']:
        print("Sorry there is not enough water")
        signal = stop
    if check_milk > resources['milk']:
        print("Sorry there is not enough milk")
        signal = stop
    if check_coffee > resources['coffee']:
        print("Sorry there is not enough coffee")
        signal = stop

    if signal == go:
        return go
    else:
        return stop


def money_checker(amounts, coin_insert=True, inserted_coin=0):
    print("INSERT COINS quarter = $0.25, dime = $0.10, nickle = $0.05, pennie = $0.01 "
          "(input 'go' to proceed)")
    while coin_insert:
        coin = input(f"[{round(inserted_coin,2)}]: ").lower()
        if coin == 'quarter':
            inserted_coin += .25
        elif coin == 'dime':
            inserted_coin += .1
        elif coin == 'nickle':
            inserted_coin += .05
        elif coin == 'pennie':
            inserted_coin += .01
        elif coin == 'go':
            print(f"Total amount inserted is ${round(inserted_coin,2)}")
            break

    if inserted_coin >= amounts:
        change = inserted_coin - amounts
        print(f"Your change is ${round(change,2)}")
        return go
    else:
        print("Sorry not enough money [MONEY REFUNDED]")
        return stop


while Machine is Active:
    resource_signal = 0
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == 'espresso':
        resource_signal = resource_checker(50, 18)
        water = 50
        coffee = 18
        milk = 0
        amount = 1.50
        product = 'espresso'
        print("That would be $1.50")
    elif order == 'latte':
        resource_signal = resource_checker(200, 24, 150)
        water = 200
        coffee = 24
        milk = 150
        amount = 2.5
        product = 'latte'
        print("That would be $2.50")
    elif order == 'cappuccino':
        resource_signal = resource_checker(250, 24, 100)
        water = 250
        coffee = 24
        milk = 100
        amount = 3.00
        product = 'cappuccino'
        print("That would be $3.00")
    elif order == 'off':
        exit()
    elif order == 'report':
        print("Water : {0}ml".format(resources['water']))
        print("Milk : {0}ml".format(resources['milk']))
        print("Coffee : {0}g".format(resources['coffee']))
        print("Money : ${0}".format(round(resources['money'],2)))
    else:
        print("Invalid Input please try again")
        continue

    if resource_signal == go:
        money_signal = money_checker(amount)
        if money_signal == go:
            resources['water'] -= water
            resources['milk'] -= milk
            resources['coffee'] -= coffee
            resources['money'] += amount
            print (f"Here is your {product}. Enjoy!")

        else:
            continue
    else:
        continue
