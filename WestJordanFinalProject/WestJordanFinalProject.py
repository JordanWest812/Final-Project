'''This is a program to display a GUI which allows user interactions to order a pizza.
Jordan West
5/13/2023
Version 1.0
'''
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import urllib.request

#create GUI window
root = Tk()
root.title("West's Pizzeria")
root.geometry("750x500")


#create tabs
notebook = ttk.Notebook(root)

tab1 = Frame(notebook)
tab2 = Frame(notebook)
tab3 = Frame(notebook)
tab4 = Frame(notebook)

#name tabs
notebook.add(tab1, text = "Information")
notebook.add(tab2, text = "Confirmation")
notebook.add(tab3, text = "Sizes")
notebook.add(tab4, text = "Toppings")


notebook.pack(expand = True, fill = "both")

#images
url = "https://raw.githubusercontent.com/JordanWest812/Final-Project/main/WestJordanFinalProject/pizza1.jpg"
urllib.request.urlretrieve(url, "pizza1.jpg")

url2 = "https://raw.githubusercontent.com/JordanWest812/Final-Project/main/WestJordanFinalProject/pizza2.jpg"
urllib.request.urlretrieve(url2, "pizza2.jpg")


photo1 = Image.open("pizza1.jpg")
sized_photo1 = photo1.resize((250, 250), Image.LANCZOS)
photo1 = ImageTk.PhotoImage(sized_photo1)

image1_label = Label(tab1, image = photo1)
image1_label.image = photo1
image1_label.grid(row = 7)

photo2 = Image.open("pizza2.jpg")
sized_photo2 = photo2.resize((250, 250), Image.LANCZOS)
photo2 = ImageTk.PhotoImage(sized_photo2)

image2_label = Label(tab4, image = photo2)
image2_label.image = photo2
image2_label.grid(row = 7)

#definitions

def tab():
    current_tab = notebook.index(notebook.select())
    if current_tab < 4:
        notebook.select(current_tab + 1)

def exit():
    root.destroy()

def back():
    current_tab = notebook.index(notebook.select())
    if current_tab > 0:
        notebook.select(current_tab - 1)

def confirm():
    name = name_input.get()
    name_lab = Label(tab2, text = "Your name : " + name)
    name_lab.grid(row = 0, column = 0, sticky = "nw")

    address1 = address_input.get()
    address2 = address2_input.get()
    address_lab = Label(tab2, text = "Your address : " + address1 + " " + address2)
    address_lab.grid(row = 1, column = 0, sticky = "nw")
    notebook.select(1)

def redo_contact():
    name_input.delete(0, END)
    address_input.delete(0, END)
    address2_input.delete(0, END)
    notebook.select(0)

def checkout_button():
    checkout_window = tk.Toplevel()
    checkout_window.geometry("500x500")
    top_label = Label(checkout_window, text = "Checkout Window")
    top_label.pack()

    size = var.get()
    tops = []
    count = 0

    if size == "Large":
        order_price = 8.99
        if size == "Medium":
            order_price = 7.99
    else:
        order_price = 6.99

    for top in toppings_list.curselection():
        tops.append(toppings_list.get(top))
        count +=1

    top_price = count * .50

    final_price = order_price + top_price

    name = name_input.get()
    name_lab = Label(checkout_window, text = "Your name : " + name)
    name_lab.pack()

    address1 = address_input.get()
    address2 = address2_input.get()
    address_lab = Label(checkout_window, text = "Your address : " + address1 + " " + address2)
    address_lab.pack()

    final_size_label = Label(checkout_window, text = "Your pizza size: " + size )
    final_size_label.pack()

    final_tops_label = Label(checkout_window, text = "Your pizza topping(s) selected: " + ", ".join(tops))
    final_tops_label.pack()

    final_price_label = Label(checkout_window, text = "Your final price is: $" + str(final_price))
    final_price_label.pack()

    exit_button5 = Button(checkout_window, text = "Exit", command= exit, bg = "red")
    exit_button5.pack()


#get personal information
name_label = Label(tab1, text = "Name ")
name_label.grid(row = 0, column = 0, sticky = "e")

name_input = Entry(tab1, width = 50)
name_input.grid(row = 0, column = 1, sticky = "w")

address_label = Label(tab1, text = "Address ")
address_label.grid(row = 1, column = 0, sticky = "ne")

address_input = Entry(tab1, width = 50)
address_input.grid(row = 1, column = 1, sticky = "nw")

address2_label = Label(tab1, text = "Address 2 ")
address2_label.grid(row = 2, column = 0, sticky = "ne")

address2_input = Entry(tab1, width = 50)
address2_input.grid(row = 2, column = 1, sticky = "nw")


#lists for ordering
sizes = ["Large", "Medium", "Small"]

toppings = ["Sausage", "Pepperoni", "Chicken", "Bacon", "Black Olives", "Onions", "Green Peppers", "Banana Peppers"]

#creat a dropdown options menu for Pizza size
size_label = Label(tab3, text = "Select the size of pizza you wish to order")
size_label.grid(row = 4, column = 0, sticky = "nw")

var = StringVar(root)
var.set(sizes[0])
size_choice = OptionMenu(tab3, var, *sizes)
size_choice.grid(row = 4, column = 1, sticky = "w")

size_price_label = Label(tab3, text = "Large : $8.99\n Medium: $7.99\n Small: $6.99")
size_price_label.grid(row = 4, column = 2, sticky = "w")

#listboxes for ordering - Toppings
toppings_label = Label(tab4, text = "Select your topping(s)")
toppings_label.grid(row = 5, column = 0)

toppings_list = Listbox(tab4, selectmode = MULTIPLE, bg = "yellow", fg = "black")
toppings_list.grid(row = 5, column = 1, sticky = "w")

for item in toppings:
     toppings_list.insert(0, item)


toppings_price_label = Label(tab4, text = "$.50 for each topping selected.")
toppings_price_label.grid(row = 5, column = 2, sticky = "w")

#exit buttons

exit_button1 = Button(tab1, text = "Exit", command = exit, bg = "red")
exit_button1.grid(row = 99, column = 99)

exit_button2 = Button(tab2, text = "Exit", command = exit, bg = "red")
exit_button2.grid(row = 99, column = 99)

exit_button3 = Button(tab3, text = "Exit", command = exit, bg = "red")
exit_button3.grid(row = 99, column = 99)

exit_button4 = Button(tab4, text = "Exit", command = exit, bg = "red")
exit_button4.grid(row = 99, column = 99)

#back buttons

back_button1 = Button(tab3, text = "Go Back", command = back)
back_button1.grid(row = 99, column = 0)

back_button2 = Button(tab4, text = "Go Back", command = back)
back_button2.grid(row = 99, column = 0)


#next tab buttons
next_button1 = Button(tab2, text = "Sizes", command = tab)
next_button1.grid(row = 99, column = 3)

next_button1 = Button(tab3, text = "Toppings", command = tab)
next_button1.grid(row = 99, column = 3)

#confirmation buttons
confirm_button = Button(tab1, text = "Confirm contact information", command = confirm, bg = "green")
confirm_button.grid(row = 99, column = 1)

redo_button = Button(tab2, text = "Redo contact information", command = redo_contact)
redo_button.grid(row = 99, column = 0)

checkout_button = Button(tab4, text = "Checkout", command = checkout_button)
checkout_button.grid(row = 99, column = 3)

root.mainloop()
