import Manager as m , customer as c
d = {'Apples' : {'qty': 12, 'price': 100}, 'Banana' : {'qty' : 15, 'price' : 75}} # to store all the stock related data
f = 'logs.txt' # file store logs of all the functions 
while True: # taking input for roles
    print("\n\n\t\t1.Manager\n\t\t2.Customer\n\n")
    try:
        role = int(input("Enter your role : "))
    except ValueError:
        print("Enter the corresponding number !!")
        continue
    break
if role == 1: # menu for manger role
    while True:
        print("\n\t\tFRUIT MARKET MANAGER")
        print('''\t\t1. Add Fruit Stock
                2. View Fruit Stock
                3. Update Fruit Stock
                4. Exit\n''')
        try:
            n = int(input("Enter your choice : "))
        except ValueError:
            print("Enter the corrresponding number")
            continue
        if n == 1:
            m.add_stock(d, f)
        elif n == 2:
            m.view_stock(d)
        elif n == 3:
            m.update_stock(d, f)
        elif n == 4:
            break
        else:
            print("Invalid input !!")

if role == 2: # menu for customer role
    while True:
        print("\n\t\tWelcom to FRUIT MARKET ")
        print('''\t\t1. Buy Fruit 
                2. View Fruit Stock
                3. Exit\n''')
        try:
            n = int(input("Enter your choice : "))
        except ValueError:
            print("Enter the corrresponding number")
            continue
        if n == 1:
            c.buy_fruit(d, f)
        elif n == 2:
            c.view_stock(d)
        elif n == 3:
            break
        else:
            print("Invalid Input !!")