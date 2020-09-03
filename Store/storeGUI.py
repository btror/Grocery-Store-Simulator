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


store_inventory = {
    "apple": 50,
    "carrot": 40,
    "tomato": 55,
    "pickle": 20,
    "banana": 42,
    "onion": 23
}

grocery_store = Store("Stan's Fruit Stand", store_inventory)
shopper = Customer("Anna", 200)

root = Tk()
root.title("Grocery Store Simulator")
root.geometry('700x550')
root.resizable(False, False)

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

button_apple = Button(root, text="add to cart")
button_carrot = Button(root, text="add to cart")
button_tomato = Button(root, text="add to cart")
button_pickle = Button(root, text="add to cart")
button_banana = Button(root, text="add to cart")
button_onion = Button(root, text="add to cart")

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


def check_out():
    added_to_cart = Frame(root, width=700, height=550)
    added_to_cart.pack()

    button_back = Button(added_to_cart, text="back", font=("default", 18), command=added_to_cart.destroy)
    button_back.place(x=316, y=465)


button_check_out = Button(root, text="check out", font=("default", 18), command=check_out)
button_check_out.place(x=288, y=465)

mainloop()
