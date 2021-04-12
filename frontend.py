from tkinter import *
from backend import Database


database = Database(host="localhost",user="zayerwali",passwd="Z@zayer7006",db="studentdb")


def get_selected_row(event):
    try:
        global selected_row
        index = list1.curselection()[0]  # returns  the index of each tuple in a list box
        selected_row = list1.get(index)  # from the list get a specified tuple of a specified index
        e1.delete(0, END)
        e1.insert(END, selected_row[1])
        e2.delete(0, END)
        e2.insert(END, selected_row[2])
        e3.delete(0, END)
        e3.insert(END, selected_row[3])
        e4.delete(0, END)
        e4.insert(END, selected_row[4])
    except IndexError:
        pass


def view_all():
    list1.delete(0, END)
    for row in database.view():
        list1.insert(END, row)






def search_text():
    list1.delete(0, END)
    for row in database.search(roll_value.get(), name_value.get(), dob_value.get(), gender_value.get()):
        list1.insert(END, row)


def add_values():
    database.insert(roll_value.get(), name_value.get(), dob_value.get(), gender_value.get())
    list1.delete(0, END)
    list1.insert(END, (roll_value.get(), name_value.get(), dob_value.get(), gender_value.get()))


def delete_value():
    database.delete(selected_row[0])


def update_value():
    database.update(selected_row[0], roll_value.get(), name_value.get(), dob_value.get(), gender_value.get())


window = Tk()
window.wm_title("StudentData")
l1 = Label(window, text="Roll")
l1.grid(row=0, column=0)

roll_value = StringVar()
e1 = Entry(window, textvariable=roll_value)
e1.grid(row=0, column=1)

l2 = Label(window, text="Name")
l2.grid(row=0, column=2)

name_value = StringVar()
e2 = Entry(window, textvariable=name_value)
e2.grid(row=0, column=3)

l3 = Label(window, text="DOB")
l3.grid(row=1, column=0)

dob_value = StringVar()
e3 = Entry(window, textvariable=dob_value)
e3.grid(row=1, column=1)

l4 = Label(window, text="Gender")
l4.grid(row=1, column=2)

gender_value = StringVar()
e4 = Entry(window, textvariable=gender_value)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

s1 = Scrollbar(window)
s1.grid(row=2, column=2, rowspan=6)

# vertical scroll of yaxis set to this scroll i.e, s1

list1.configure(yscrollcommand=s1.set)

# configure the s1 so that the vertical view of the text changes with respect to this scroll

s1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="ViewAll", width=12, command=view_all)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Entry", width=12, command=search_text)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add", width=12, command=add_values)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12, command=update_value)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=12, command=delete_value)
b5.grid(row=6, column=3)


b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=8, column=3)

window.mainloop()
