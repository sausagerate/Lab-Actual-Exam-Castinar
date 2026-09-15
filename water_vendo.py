class WaterVendo:

    def start(self):
        choice = int(input())
        payment = int(input())

        if choice == 1:
            container = "500 mL Bottle"
            price = 10

        elif choice == 2:
            container = "1 Liter Bottle"
            price = 15

        elif choice == 3:
            container = "5 Liter Container"
            price = 40

        else:
            print("Invalid selection.")
            returnr

        print("Container:", container)
        print("Price: ₱" + str(price))

        if payment < price:
            print("Insufficient payment.")
            return

        change = payment - price

        print("Change: ₱" + str(change))

        twenty = change // 20
        change = change % 20

        ten = change // 10
        change = change % 10

        five = change // 5
        change = change % 5

        one = change

        print("₱20:", twenty)
        print("₱10:", ten)
        print("₱5:", five)
        print("₱1:", one)


machine = WaterVendo()
machine.start()