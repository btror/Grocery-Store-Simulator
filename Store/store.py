def insert_sequence(str1, str2, int):
    str1_split1 = str1[:int]
    str1_split2 = str1[int:]
    new_string = str1_split1 + str2 + str1_split2
    return new_string


class Customer:
    def __init__(self, name, age, wallet):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.cart = []
        self.prices = []

    # cart = []
    # prices = []

    def add_item_to_cart(self):
        item = input("What do you want to buy?: ")
        self.cart.append(item)
        cost = float(input("How much does it cost?: "))
        self.prices.append(cost)
        self.wallet = self.wallet - cost

    def display_funds(self):
        print("Wallet: $" + str(self.wallet))

    def check_out(self):
        if self.wallet >= 0:
            bottom = ''
            array_length = len(self.cart)
            for i in range(array_length):
                bottom += "\t" + str(self.cart[i]) + "\t\t\t\t\t"
                receipt_list = insert_sequence(str(bottom), str(self.prices[i]), 15) + "\n"
                bottom = receipt_list + "\n"
            # display the receipt
            print("\n\n\t       Grocery Store"
                  "\t\n\t***************************"
                  "\t\n\t       CASH  RECEIPT"
                  "\t\n\t***************************"
                  "\t\n\tDescription           Price\n"
                   + bottom)


anna = Customer("Anna", 18, 200)
while True:
    anna.add_item_to_cart()
    anna.display_funds()
    continue_shopping = input("Continue?: ")
    if continue_shopping == "no":
        anna.check_out()
        break
