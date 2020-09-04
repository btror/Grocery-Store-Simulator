from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk


class Store:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory


class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.cart = {
            "apple": 0,
            "carrot": 0,
            "tomato": 0,
            "pickle": 0,
            "banana": 0,
            "onion": 0
        }


store_inventory = {
    "apple": .99,
    "carrot": .59,
    "tomato": 1.24,
    "pickle": 2.88,
    "banana": .79,
    "onion": .65
}

grocery_store = Store("Stan's Fruit Stand", store_inventory)
shopper = Customer("Anna", 200)

root = Tk()
root.title("Grocery Store Simulator")
root.geometry('700x550')
root.resizable(False, False)

'''
systems
'''


def add_to_cart(number):
    value = 0
    if number == 1:
        value = combobox_apple.get()
        shopper.cart["apple"] = value
        print(shopper.cart)
    if number == 2:
        value = combobox_carrot.get()
        shopper.cart["carrot"] = value
        print(shopper.cart)
    if number == 3:
        value = combobox_tomato.get()
        shopper.cart["tomato"] = value
        print(shopper.cart)
    if number == 4:
        value = combobox_pickle.get()
        shopper.cart["pickle"] = value
        print(shopper.cart)
    if number == 5:
        value = combobox_banana.get()
        shopper.cart["banana"] = value
        print(shopper.cart)
    if number == 6:
        value = combobox_onion.get()
        shopper.cart["onion"] = value
        print(shopper.cart)


def check_out():
    added_to_cart = Frame(root, width=700, height=550)
    added_to_cart.pack()

    button_back = Button(added_to_cart, text="back", font=("default", 18), command=added_to_cart.destroy)
    button_back.place(x=316, y=465)

    top_cart_label = Label(added_to_cart, text="Your Items", font=("default", 14))
    top_cart_label.place(x=20, y=20)
    # ttk.Separator(added_to_cart).place(x=0, y=70, relwidth=1)

    count = 0
    y_value = 30
    total_cost = 0
    for amount in shopper.cart.values():
        if amount != 0:
            temp_name = ''
            item_cost = 0
            ttk.Separator(added_to_cart).place(x=0, y=(y_value + 40), relwidth=1)
            y_value += 60
            if count == 0:
                temp_name = "(" + str(amount) + ")    apples"
                item_cost = float(amount) * float(grocery_store.inventory.get('apple'))
                item_cost = round(item_cost, 2)
                print(item_cost)

            if count == 1:
                temp_name = "(" + str(amount) + ")    carrots"
                item_cost = float(amount) * float(grocery_store.inventory.get('carrot'))
                item_cost = round(item_cost, 2)
                print(item_cost)

            if count == 2:
                temp_name = "(" + str(amount) + ")    tomatoes"
                item_cost = float(amount) * float(grocery_store.inventory.get('tomato'))
                item_cost = round(item_cost, 2)
                print(item_cost)

            if count == 3:
                temp_name = "(" + str(amount) + ")    pickles"
                item_cost = float(amount) * float(grocery_store.inventory.get('pickle'))
                item_cost = round(item_cost, 2)
                print(item_cost)

            if count == 4:
                temp_name = "(" + str(amount) + ")    bananas"
                item_cost = float(amount) * float(grocery_store.inventory.get('banana'))
                item_cost = round(item_cost, 2)
                print(item_cost)

            if count == 5:
                temp_name = "(" + str(amount) + ")    onions"
                item_cost = float(amount) * float(grocery_store.inventory.get('onion'))
                item_cost = round(item_cost, 2)
                print(item_cost)

            total_cost += item_cost
            total_cost = round(total_cost, 2)

            ttk.Separator(added_to_cart).place(x=0, y=430, relwidth=1)
            Label(added_to_cart, text="$" + str(item_cost)).place(x=650, y=y_value)
            Label(added_to_cart, text=temp_name).place(x=28, y=y_value)
            Label(added_to_cart, text="  total").place(x=50, y=445)
            Label(added_to_cart, text="$" + str(total_cost)).place(x=650, y=445)
        count += 1


'''
labels and buttons
'''

label_apple = Label(root, text="Fresh Apples", bg="light blue")
label_carrot = Label(root, text="Sliced Carrots", bg="light blue")
label_tomato = Label(root, text="Washed Tomatoes", bg="light blue")
label_pickle = Label(root, text="Sliced Pickles", bg="light blue")
label_banana = Label(root, text="Brazilian Bananas", bg="light blue")
label_onion = Label(root, text="Hole Onions", bg="light blue")

img_apple = Image.open("pics/apple.jpg")
apple = ImageTk.PhotoImage(img_apple.resize((100, 100)))
panel_apple = Label(root, image=apple, height=100, width=100)

img_carrot = Image.open("pics/carrot.jpg")
carrot = ImageTk.PhotoImage(img_carrot.resize((100, 100)))
panel_carrot = Label(root, image=carrot, height=100, width=100)

img_tomato = Image.open("pics/tomato.jpg")
tomato = ImageTk.PhotoImage(img_tomato.resize((100, 100)))
panel_tomato = Label(root, image=tomato, height=100, width=100)

img_pickle = Image.open("pics/pickle.png")
pickle = ImageTk.PhotoImage(img_pickle.resize((100, 100)))
panel_pickle = Label(root, image=pickle, height=100, width=100)

img_banana = Image.open("pics/banana.jpg")
banana = ImageTk.PhotoImage(img_banana.resize((100, 100)))
panel_banana = Label(root, image=banana, height=100, width=100)

img_onion = Image.open("pics/onion.jpg")
onion = ImageTk.PhotoImage(img_onion.resize((100, 100)))
panel_onion = Label(root, image=onion, height=100, width=100)

button_apple = Button(root, text="add to cart", command=lambda: add_to_cart(1))
button_carrot = Button(root, text="add to cart", command=lambda: add_to_cart(2))
button_tomato = Button(root, text="add to cart", command=lambda: add_to_cart(3))
button_pickle = Button(root, text="add to cart", command=lambda: add_to_cart(4))
button_banana = Button(root, text="add to cart", command=lambda: add_to_cart(5))
button_onion = Button(root, text="add to cart", command=lambda: add_to_cart(6))

label_apple_price = Label(root, text="$0.99")
label_carrot_price = Label(root, text="$0.59")
label_tomato_price = Label(root, text="$1.24")
label_pickle_price = Label(root, text="$2.88")
label_banana_price = Label(root, text="$0.79")
label_onion_price = Label(root, text="$0.65")

combobox_apple = ttk.Combobox(root, width=2, state="readonly")
combobox_apple.bind("<<ComboboxSelected>>", lambda e: root.focus())
combobox_apple['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
combobox_apple.current(0)
combobox_carrot = ttk.Combobox(root, width=2, state="readonly")
combobox_carrot.bind("<<ComboboxSelected>>", lambda e: root.focus())
combobox_carrot['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
combobox_carrot.current(0)
combobox_tomato = ttk.Combobox(root, width=2, state="readonly")
combobox_tomato.bind("<<ComboboxSelected>>", lambda e: root.focus())
combobox_tomato['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
combobox_tomato.current(0)
combobox_pickle = ttk.Combobox(root, width=2, state="readonly")
combobox_pickle.bind("<<ComboboxSelected>>", lambda e: root.focus())
combobox_pickle['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
combobox_pickle.current(0)
combobox_banana = ttk.Combobox(root, width=2, state="readonly")
combobox_banana.bind("<<ComboboxSelected>>", lambda e: root.focus())
combobox_banana['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
combobox_banana.current(0)
combobox_onion = ttk.Combobox(root, width=2, state="readonly")
combobox_onion.bind("<<ComboboxSelected>>", lambda e: root.focus())
combobox_onion['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
combobox_onion.current(0)

panel_apple.place(x=100, y=45)
panel_carrot.place(x=300, y=45)
panel_tomato.place(x=500, y=45)
panel_pickle.place(x=100, y=270)
panel_banana.place(x=300, y=270)
panel_onion.place(x=500, y=270)

label_apple.place(x=115, y=17)
label_carrot.place(x=314, y=17)
label_tomato.place(x=500, y=17)
label_pickle.place(x=115, y=242)
label_banana.place(x=301, y=242)
label_onion.place(x=516, y=242)

button_apple.place(x=116, y=180)
button_carrot.place(x=316, y=180)
button_tomato.place(x=516, y=180)
button_pickle.place(x=116, y=405)
button_banana.place(x=316, y=405)
button_onion.place(x=516, y=405)

label_apple_price.place(x=113, y=154)
label_carrot_price.place(x=314, y=154)
label_tomato_price.place(x=514, y=154)
label_pickle_price.place(x=113, y=379)
label_banana_price.place(x=314, y=379)
label_onion_price.place(x=514, y=379)

combobox_apple.place(x=149, y=154)
combobox_carrot.place(x=349, y=154)
combobox_tomato.place(x=549, y=154)
combobox_pickle.place(x=149, y=379)
combobox_banana.place(x=349, y=379)
combobox_onion.place(x=549, y=379)

'''
added_to_cart = Frame(root, width=700, height=550, bg='red')
added_to_cart.pack()
added_to_cart.destroy()
'''

button_check_out = Button(root, text="check out", font=("default", 18), command=check_out)
button_check_out.place(x=288, y=465)

mainloop()
