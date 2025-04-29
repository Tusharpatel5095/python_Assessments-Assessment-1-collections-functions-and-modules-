def buy_fruit(d,f):
        while True:
                n = input("Enter the fruit you want to buy : ")
                if n not in d.keys():
                        print(f"{n} is currently not avaible")
                        c = input("Do you want to buy another fruit  (y/n) : ")
                        if c.lower == 'y':
                                continue
                        else:
                                return None 
                else:
                        break
        while True:
                try:
                        q = int(input("Enter the quantity : "))
                except ValueError:
                        print("Enter a number !!")
                        continue
                if q > d[n]['qty']:
                        print(f"We only have {d[n]['qty']} {n} in stock")
                else:
                        break
        d[n]['qty'] -= q
        print(f"\n\t\tPlease pay your bill of Rs.{d[n]['price'] * q}\n")
        print("\t\tThank you for chosing our store")

        file = open(f, 'a')
        file.write(f"{q} {n} sold for Rs.{d[n]['price'] * q}\n")
        file.close()
def view_stock(d):
        for i in d:
                print(f"{i} : ")
                for j in d[i]:
                        print(f"{j} - {d[i][j]}", end = '\t')
                print()