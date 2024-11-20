name = input(" Enter your Name : ")
while True :
    item = int(input(" Enter Number of Items : "))
    price = float(input(" Enter Price of an Item : "))
    total = item * price
    while True:
        item1 = int(input(" Enter Number of Items : "))
        price1 = float(input(" Enter Price of an Item : "))
        total1 = item1 * price1
        choice = input(" Add items : (yes or no) and (Y or N)")
        if(choice == 'yes' or choice == 'Y'):
            continue
        else:
            total_amount = total + total1
            print("-"*70)
            print(f"Name : {name}")
            print(f"Total Payable Amount is : {total_amount}")
            print("-"*70)
            break
        
    