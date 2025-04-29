def add_stock(dic, file):
        print("ADD FRUIT STOCK")
        n = input("Enter fruit name : ")
        while True:
                try:
                        q = int(input("Enter quantity (in kgs) : "))
                        p = float(input("Enter price : "))
                except ValueError:
                        print("Enter number!!")
                        continue
                break
        dic[n] = {'qty' : q, 'price' : p}
        f = open(file, 'a')
        f.write(f'New stock of {q} {n} of Rs.{p} added\n')
        f.close()

def view_stock(d):
        print("STOCK DETAILS")
        for i in d:
                print(f"{i} : -")
                for j in d[i]:
                        print(f"{j} : {d[i][j]}")

def update_stock(d, file):
        print("UPDATE STOCK")
        while True:
                try:
                        n = int(input("Select a function : \n1.Add stock \n2.Remove stock \n3.Change price \n"))
                except ValueError:
                        print("Enter the corresponding number")
                        continue
                break
        while True:
                fr = input("Enter the fruit'a name which you want to update : ")
                if fr not in d.keys():
                        print(f"{fr} doesn't exist in the stock")
                else:
                        break
        log = ''
        if n == 1:
                while True:
                        try:
                                aq = int(input("Enter quantity to add : "))
                        except ValueError:
                                print("Enter a integer !!")
                                continue
                        break
                d[fr]['qty'] += aq
                log = f'{aq} {fr} added to the stock'
        if n == 2:
                while True:
                        try:
                                aq = int(input("Enter quantity to remove : "))
                        except ValueError:
                                print("Enter a integer !!")
                                continue
                        break
                if aq < d[fr]['qty']:
                        d[fr]['qty'] -= aq
                        log = f'{aq} {fr} removed from the stock'
                else:
                        print(f"Quantity is lower than the number {aq}")
        if n == 3:
                while True:
                        try:
                                pri = float(input("Enter the new price : "))
                        except ValueError:
                                
                                print("Enter a number !!")
                                continue
                        break
                d[fr]['price'] = pri
                log = f'Price of {fr} updated to {pri}'
        file = open(file, 'a')
        file.write(f'{log}\n')
        file.close()