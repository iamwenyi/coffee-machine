machine = True

def make_espresso(water,coffee):
    water_left = water - 50
    coffee_left = coffee - 18
    
    usedFor_esp = [water_left,coffee_left]
    return usedFor_esp
    
def make_latte(water,milk,coffee):
    water_left = water - 200
    milk_left = milk - 150
    coffee_left = coffee - 24
    
    usedFor_lat = [water_left,milk_left,coffee_left]
    return usedFor_lat
    
def make_cappuccino(water,milk,coffee):
    water_left = water - 250
    milk_left = milk - 100
    coffee_left = coffee - 24
    
    usedFor_cap = [water_left,milk_left,coffee_left]
    return usedFor_cap

def money_process():
    rm_one_comp = 1
    rm_five_comp = 5
    rm_ten_comp = 10
    
    rm_one = int(input("RM 1 papers: "))
    rm_five = int(input("RM 5 papers: "))
    rm_ten = int(input("RM 10 papers: "))
    
    rm_one_user = rm_one_comp * rm_one
    rm_five_user = rm_five_comp * rm_five
    rm_ten_user = rm_ten_comp * rm_ten
    
    total_user = rm_one_user + rm_five_user + rm_ten_user
    return total_user

def main():
    machine = True
    make_coffee = True
    
    water = 300
    milk = 200
    coffee = 100
    money = 0
    
    espresso_p = 6
    latte_p = 14
    cappuccino_p = 20
    
    while machine == True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
        if choice == "report":
            print("")
            print(f"Water: {water} ml \nMilk: {milk} ml \nCoffee: {coffee} g \nMoney: RM{money}")
            
        elif choice == "espresso":
            if water >= 50 and coffee >= 18:
                
                print(f"{choice} cost: RM{espresso_p}")
                total_user = money_process()
                
                if total_user == espresso_p:
                    money = money + total_user
                
                elif total_user > espresso_p:
                    change = total_user - espresso_p
                    print(f"Here is RM{change} in change.")
                    money = money + total_user - change
                    
                else:
                    print("")
                    print("Sorry, that's not enough money. Money refunded.")
                    make_coffee = False
                
                if make_coffee == True:
                    usedFor_esp = make_espresso(water,coffee)
                
                    print("")
                    print("Here's your espresso, enjoy!")
                
                    water = usedFor_esp[0]
                    coffee = usedFor_esp[1]
            else:
                if water < 50 and coffee >= 18:
                    print("")
                    print("Sorry, there is not enough water")
                    
                elif water >= 50 and coffee < 18:
                    print("")
                    print("Sorry, there is not enough coffee")
                    
                else:
                    print("")
                    print("Sorry, there are not enough ingredients")
                    
        elif choice == "latte":
            if water >= 200 and milk >= 150 and coffee >= 24:
                
                print(f"{choice} cost: RM{latte_p}")
                total_user = money_process()
                
                if total_user == latte_p:
                    money = money + total_user
                
                elif total_user > latte_p:
                    change = total_user - latte_p
                    print(f"Here is RM{change} in change.")
                    money = money + total_user - change
                    
                else:
                    print("")
                    print("Sorry, that's not enough money. Money refunded.")
                    make_coffee = False
                
                if make_coffee == True:
                    usedFor_lat = make_latte(water,milk,coffee)
                    print("")
                    print("Here's your latte, enjoy!")
                
                    water = usedFor_lat[0]
                    milk = usedFor_lat[1]
                    coffee = usedFor_lat[2]
            else:
                if water < 200 and milk >= 150 and coffee >= 24:
                    print("")
                    print("Sorry, there is not enough water")
                    
                elif water >= 200 and milk < 150 and coffee >= 24:
                    print("")
                    print("Sorry, there is not enough milk")
                    
                elif water >= 200 and milk >= 150 and coffee < 24:
                    print("")
                    print("Sorry, there is not enough coffee")
                    
                else:
                    print("")
                    print("Sorry, there are not enough ingredients")
                    
        elif choice == "cappuccino":
            if water >= 250 and milk >= 100 and coffee >= 24:
                
                print(f"{choice} cost: RM{cappuccino_p}")
                total_user = money_process()
                
                if total_user == cappuccino_p:
                    money = money + total_user
                
                elif total_user > cappuccino_p:
                    change = total_user - cappuccino_p
                    print(f"Here is RM{change} in change.")
                    money = money + total_user - change
                    
                else:
                    print("")
                    print("Sorry, that's not enough money. Money refunded.")
                    make_coffee = False
                
                if make_coffee == True:
                    usedFor_cap = make_cappuccino(water,milk,coffee)
                    print("")
                    print("Here's your cappuccino, enjoy!")
                    
                    water = usedFor_cap[0]
                    milk = usedFor_cap[1]
                    coffee = usedFor_cap[2]
            else:
                if water < 250 and milk >= 100 and coffee >= 24:
                    print("")
                    print("Sorry, there is not enough water")
                    
                elif water >= 250 and milk < 100 and coffee >= 24:
                    print("")
                    print("Sorry, there is not enough milk")
                    
                elif water >= 250 and milk >= 100 and coffee < 24:
                    print("")
                    print("Sorry, there is not enough coffee")
                    
                else:
                    print("")
                    print("Sorry, there are not enough ingredients")
        
        elif choice == "off":
            machine = False
            print("Bye!")
            
main()