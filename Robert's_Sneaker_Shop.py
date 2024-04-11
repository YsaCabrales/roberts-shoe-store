from tkinter import*
from tkinter import messagebox

#SHOP -----------------------------------------
shop = Tk()
shop.title("Shoe Store")
shop.geometry("970x770")
label1 = Label(shop, text="Welcome to Ron Store").pack()

#Customer Details
name = Label(shop, text="Name: ").place(x=10,y=20)
age = Label(shop, text="Age: ").place(x=10,y=40)
address = Label(shop, text="Address").place(x=10,y=60)
name_entry = Entry(shop, width=20)
name_entry.place(x=60,y=20)
age_entry = Entry(shop, width=5)
age_entry.place(x=60,y=40)
address_entry = Entry(shop, width=20)
address_entry.place(x=60,y=60)

size_choices = [
    "US 7",
    "US 7.5",
    "US 8",
    "US 8.5",
    "US 9",
    "US 9.5",
    "US 10",
    "US 10.5",
    "US 11",
    "US 11.5",
    "US 12",
    "US 12.5",
    "US 13"]
products = []

#Add to Cart Commands
def P1():
    global products
    products.append("P1")
    messagebox.showinfo("Add to Cart","Successfully Added to cart")
def P2():
    global products
    products.append("P2")
    messagebox.showinfo("Add to Cart","Successfully Added to cart")
def P3():
    global products
    products.append("P3")
    messagebox.showinfo("Add to Cart","Successfully Added to cart")
def P4():
    global products
    products.append("P4")
    messagebox.showinfo("Add to Cart","Successfully Added to cart")
def P5():
    global products
    products.append("P5")
    messagebox.showinfo("Add to Cart","Successfully Added to cart")
def P6():
    global products
    products.append("P6")
    messagebox.showinfo("Add to Cart","Successfully Added to cart")
def P7():
    global products
    products.append("P7")
    messagebox.showinfo("Add to Cart","Successfully Added to cart")
def P8():
    global products
    products.append("P8")
    messagebox.showinfo("Add to Cart","Successfully Added to cart")
def P9():
    global products
    products.append("P9")
    messagebox.showinfo("Add to Cart","Successfully Added to cart")
def P10():
    global products
    products.append("P10")
    messagebox.showinfo("Add to Cart","Successfully Added to cart")
def P11():
    global products
    products.append("P11")
    messagebox.showinfo("Add to Cart","Successfully Added to cart")
def P12():
    global products
    products.append("P12")
    messagebox.showinfo("Add to Cart","Successfully Added to cart")

#LOGOS ------------------------------------------
Nikelogo_photo = PhotoImage(file = "Logos\\Nike_Logo.png")
Label(shop, image = Nikelogo_photo).place(x=90,y=100)
Adidaslogo_photo = PhotoImage(file = "Logos\\Adidas_Logo.png")
Label(shop, image = Adidaslogo_photo).place(x=430,y=100)
Sperrylogo_photo = PhotoImage(file = "Logos\\Sperry_Logo.png")
Label(shop, image = Sperrylogo_photo).place(x=710,y=125)

#PRODUCTS ---------------------------------------
#Product 1
P1_frame = Frame(shop, width=310, height=125, bg="grey")
P1_frame.place(x=5,y=185)

P1_photo = PhotoImage(file = "ShoeProducts\\product1.png")
Label(P1_frame, image = P1_photo).place(x=5,y=5)

Label(P1_frame, text="Nike Air Force 1 '07 Craft").place(x=170,y=10)
Label(P1_frame, text="Php 6,445").place(x=55,y=100)
Label(P1_frame, text="4.8 / 5 stars").place(x=170,y=40)

P1_addtocart = Button(P1_frame, text="Add to Cart", command=P1, bg="orange").place(x=230,y=95)

#Product 2
P2_frame = Frame(shop, width=310, height=125, bg="grey")
P2_frame.place(x=5,y=320)

P2_photo = PhotoImage(file = "ShoeProducts\\product2.png")
Label(P2_frame, image = P2_photo).place(x=5,y=5)

Label(P2_frame, text="Nike Zoom Fly 3").place(x=170,y=10)
Label(P2_frame, text="Php 8,095").place(x=55,y=100)
Label(P2_frame, text="4.4 / 5 stars").place(x=170,y=40)

P2_addtocart = Button(P2_frame, text="Add to Cart", command=P2, bg="orange").place(x=230,y=95)

#Product 3
P3_frame = Frame(shop, width=310, height=125, bg="grey")
P3_frame.place(x=5,y=455)

P3_photo = PhotoImage(file = "ShoeProducts\\product3.png")
Label(P3_frame, image = P3_photo).place(x=5,y=5)

Label(P3_frame, text="Nike Air Force 1 Pixel").place(x=170,y=10)
Label(P3_frame, text="Php 5,295").place(x=55,y=100)
Label(P3_frame, text="4.8 / 5 stars").place(x=170,y=40)

P3_addtocart = Button(P3_frame, text="Add to Cart", command=P3, bg="orange").place(x=230,y=95)

#Product 4
P4_frame = Frame(shop, width=310, height=125, bg="grey")
P4_frame.place(x=5,y=590)

P4_photo = PhotoImage(file = "ShoeProducts\\product4.png")
Label(P4_frame, image = P4_photo).place(x=5,y=5)

Label(P4_frame, text="Nike Air Max 3").place(x=170,y=10)
Label(P4_frame, text="Php 7,345").place(x=55,y=100)
Label(P4_frame, text="4.6 / 5 stars").place(x=170,y=40)

P4_addtocart = Button(P4_frame, text="Add to Cart", command=P4, bg="orange").place(x=230,y=95)

#Product 5
P5_frame = Frame(shop, width=310, height=125, bg="grey")
P5_frame.place(x=330,y=185)

P5_photo = PhotoImage(file = "ShoeProducts\\product5.png")
Label(P5_frame, image = P5_photo).place(x=5,y=5)

Label(P5_frame, text="Adidas Superstar").place(x=170,y=10)
Label(P5_frame, text="Php 4,800").place(x=55,y=100)
Label(P5_frame, text="4.7 / 5 stars").place(x=170,y=40)

P5_addtocart = Button(P5_frame, text="Add to Cart", command=P5, bg="orange").place(x=230,y=95)

#Product 6
P6_frame = Frame(shop, width=310, height=125, bg="grey")
P6_frame.place(x=330,y=320)

P6_photo = PhotoImage(file = "ShoeProducts\\product6.png")
Label(P6_frame, image = P6_photo).place(x=5,y=5)

Label(P6_frame, text="Adidas Stan Smith").place(x=170,y=10)
Label(P6_frame, text="Php 4,800").place(x=55,y=100)
Label(P6_frame, text="4.7 / 5 stars").place(x=170,y=40)

P6_addtocart = Button(P6_frame, text="Add to Cart", command=P6, bg="orange").place(x=230,y=95)

#Product 7
P7_frame = Frame(shop, width=310, height=125, bg="grey")
P7_frame.place(x=330,y=455)

P7_photo = PhotoImage(file = "ShoeProducts\\product7.png")
Label(P7_frame, image = P7_photo).place(x=5,y=5)

Label(P7_frame, text="Ultraboost 4.0 DNA").place(x=170,y=10)
Label(P7_frame, text="Php 8,900").place(x=55,y=100)
Label(P7_frame, text="4.4 / 5 stars").place(x=170,y=40)

P7_addtocart = Button(P7_frame, text="Add to Cart", command=P7, bg="orange").place(x=230,y=95)

#Product 8
P8_frame = Frame(shop, width=310, height=125, bg="grey")
P8_frame.place(x=330,y=590)

P8_photo = PhotoImage(file = "ShoeProducts\\product8.png")
Label(P8_frame, image = P8_photo).place(x=5,y=5)

Label(P8_frame, text="X9000L4 Cyberpunk 2077").place(x=170,y=10)
Label(P8_frame, text="Php 7,900").place(x=55,y=100)
Label(P8_frame, text="4.9 / 5 stars").place(x=170,y=40)

P8_addtocart = Button(P8_frame, text="Add to Cart", command=P8, bg="orange").place(x=230,y=95)

#Product 9
P9_frame = Frame(shop, width=310, height=125, bg="grey")
P9_frame.place(x=655,y=185)

P9_photo = PhotoImage(file = "ShoeProducts\\product9.png")
Label(P9_frame, image = P9_photo).place(x=5,y=5)

Label(P9_frame, text="Men's Authentic Original\nLeather Boat Shoe").place(x=170,y=10)
Label(P9_frame, text="Php 4,615").place(x=55,y=100)
Label(P9_frame, text="4.5 / 5 stars").place(x=170,y=50)

P9_addtocart = Button(P9_frame, text="Add to Cart", command=P9, bg="orange").place(x=230,y=95)

#Product 10
P10_frame = Frame(shop, width=310, height=125, bg="grey")
P10_frame.place(x=655,y=320)

P10_photo = PhotoImage(file = "ShoeProducts\\product10.png")
Label(P10_frame, image = P10_photo).place(x=5,y=5)

Label(P10_frame, text="Men's Avenue Embossed\nDuck Boot").place(x=170,y=10)
Label(P10_frame, text="Php 5,525").place(x=55,y=100)
Label(P10_frame, text="3.5 / 5 stars").place(x=170,y=50)

P10_addtocart = Button(P10_frame, text="Add to Cart", command=P10, bg="orange").place(x=230,y=95)

#Product 11
P11_frame = Frame(shop, width=310, height=125, bg="grey")
P11_frame.place(x=655,y=455)

P11_photo = PhotoImage(file = "ShoeProducts\\product11.png")
Label(P11_frame, image = P11_photo).place(x=5,y=5)

Label(P11_frame, text="Women's Saltwater Wool\nEmbossed Duck Boot\nw/ Thinsulate").place(x=170,y=10)
Label(P11_frame, text="Php 5,525").place(x=55,y=100)
Label(P11_frame, text="4.5 / 5 stars").place(x=170,y=65)

P11_addtocart = Button(P11_frame, text="Add to Cart", command=P11, bg="orange").place(x=230,y=95)

#Product 12
P12_frame = Frame(shop, width=310, height=125, bg="grey")
P12_frame.place(x=655,y=590)

P12_photo = PhotoImage(file = "ShoeProducts\\product12.png")
Label(P12_frame, image = P12_photo).place(x=5,y=5)

Label(P12_frame, text="Women's Maritime\nRepel Suede Snow Boot").place(x=170,y=10)
Label(P12_frame, text="Php 6,250").place(x=55,y=100)
Label(P12_frame, text="4.9 / 5 stars").place(x=170,y=65)

P12_addtocart = Button(P12_frame, text="Add to Cart", command=P12, bg="orange").place(x=230,y=95)

#Buy Command
def buy():
    global products
    total_price = 0
    new_name = name_entry.get()
    new_age = age_entry.get()
    new_address = address_entry.get()
    messagebox.showinfo("Congats!","Transaction complete")
    #RECEIPT --------------------------------------------
    receipt = Tk()
    receipt.title("Receipt")
    receipt.geometry("330x650")
    Label(receipt, text="Receipt").pack()
    Label(receipt, text="Name: ").place(x=10, y=20)
    Label(receipt, text="Age: ").place(x=10, y=40)
    Label(receipt, text="Address: ").place(x=10, y=60)
    Label(receipt, text=new_name).place(x=100, y=20)
    Label(receipt, text=new_age).place(x=100, y=40)
    Label(receipt, text=new_address).place(x=100, y=60)
    Item_list = Listbox(receipt, width=290, height=200)
    Item_list.place(x=10, y=110)
    for i in range(len(products)):
        if products[i] == "P1":
            total_price += 6445
            Item_list.insert(END, "Nike Air Force 1 '07 Craft")
            Item_list.insert(END, "Php 6,445")
            Item_list.insert(END, "")
        elif products[i] == "P2":
            total_price += 8095
            Item_list.insert(END, "Nike Zoom Fly 3")
            Item_list.insert(END, "Php 8,095")
            Item_list.insert(END, "")
        elif products[i] == "P3":
            total_price += 5295
            Item_list.insert(END, "Nike Air Force 1 Pixel")
            Item_list.insert(END, "Php 5,295")
            Item_list.insert(END, "")
        elif products[i] == "P4":
            total_price += 7345
            Item_list.insert(END, "Nike Air Max 3")
            Item_list.insert(END, "Php 7,345")
            Item_list.insert(END, "")
        elif products[i] == "P5":
            total_price += 4800
            Item_list.insert(END, "Adidas Superstar Shoes")
            Item_list.insert(END, "Php 4,800")
            Item_list.insert(END, "")
        elif products[i] == "P6":
            total_price += 4800
            Item_list.insert(END, "Adidas Stan Smith")
            Item_list.insert(END, "Php 4,800")
            Item_list.insert(END, "")
        elif products[i] == "P7":
            total_price += 8900
            Item_list.insert(END, "Ultraboost 4.0 DNA Shoes")
            Item_list.insert(END, "Php 8,900")
            Item_list.insert(END, "")
        elif products[i] == "P8":
            total_price += 7900
            Item_list.insert(END, "X9000L4 Cyberpunk 2077")
            Item_list.insert(END, "Php 7,900")
            Item_list.insert(END, "")
        elif products[i] == "P9":
            total_price += 4615
            Item_list.insert(END, "Men's Authentic Original Leather Boat Shoe")
            Item_list.insert(END, "Php 4,615")
            Item_list.insert(END, "")
        elif products[i] == "P10":
            total_price += 5525
            Item_list.insert(END, "Men's Avenue Embossed Duck Boot")
            Item_list.insert(END, "Php 5,525")
            Item_list.insert(END, "")
        elif products[i] == "P11":
            total_price += 5525
            Item_list.insert(END, "Women's Saltwater Wool Embossed Duck Boot w/ Thinsulate™")
            Item_list.insert(END, "Php 5,525")
            Item_list.insert(END, "")
        elif products[i] == "P12":
            total_price += 6250
            Item_list.insert(END, "Women's Maritime Repel Suede Snow Boot")
            Item_list.insert(END, "Php 6,250")
            Item_list.insert(END, "")
            
    Label(receipt, text="Total Amount: Php ").place(x=10, y=80)
    Label(receipt, text=total_price).place(x=115, y=80)

    Label(receipt, text="Payment: ").place(x=170, y=20)
    Payment = Entry(receipt, width=12)
    Payment.place(x=235, y=20)

    #Pay Command
    def pay():
        payment_amount = float(Payment.get())
        if total_price <= payment_amount:
            change = payment_amount - total_price
            changemessage = "Change: " + str(change) + "\nThank you for purchasing!"
            messagebox.showinfo("Payment Successful", changemessage)
        else:
            messagebox.showinfo("Insufficient Payment", "Insufficient Payment Amount\nPlease try again.")

    Pay_button = Button(receipt, text="Pay", command=pay, font=20, bg="blue", fg="white").place(x=225, y=50)

Buy_button = Button(shop, text="Buy Now!", command=buy, font=20, bg="green", fg="white").place(x=460,y=725)

shop.mainloop()