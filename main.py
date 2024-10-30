"""This is the menu of the cafe"""

# Greetings
print("Welcome To Our Cafe...")

# Item List

menu = {
    "Pizza":150,
    "Burger":50,
    "Noodles":20,
    "Cake":250,
    "Rice With Pulses":70,
    "Salad":50,
    "Chapati With Vegitables":60,
    "CocaCola":25,
    "RedBull":150,
    "Water":10
}

# Printing Items
print("Pizza                    150rs")
print("Burger                   50rs")
print("Noodles                  20rs")
print("Cake                     250rs")
print("Rice With Pulses         70rs")
print("Salad                    50rs")
print("Chapati With Vegitabes   60rs")
print("CocaCola                 25rs")
print("RedBull                  150rs")
print("Water                    10rs")

# Total Prize
bill = 0 # Initial Bill Price...
x = 0 # Giving the value to x for while loop...

# Getting the order by the user...

while x <= 1:
    print("Type The Item That You Want To Order")
    order1 = input("Type Here = ")

    #Adding The Price Of The Item To Bill And Also Cheaking That The Item Is In the Lis Or Not
    if order1 in menu:
        bill += menu[order1]
        print(f"Your item {order1} has been added to your order...")

    else:
        print(f"The Item {order1} Is Not In Our Menu, Please Order Something That We Can Serve To You...")

    # Another Order
    another_order = input("Would You Like To Order Anything Else? (Y/N) = ")

    if another_order == "Y":
        order2 = input("Enter The Name Of Another Item = ")
        if order2 in menu:
            bill += menu[order2]
            print(another_order)
        else:
            print(f"The order {order2} that you have given that we can not serve you..")

    print("Thanks For Your Order We Will Provide You That You Have Ordered...")
            
    print(f"Your Total Order Price Is {bill}...")
    print("====================================================================================")
    # Program Over