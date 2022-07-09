from tkinter import *
import back_end

def get_selected_row():
    global selected_tuple
    index=list1.curseselection()[0]
    selected_tuple=list1.get(index)
    return(selected_tuple)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])


def view_command():
    list1.delete(0,END)
    for row in back_end.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in back_end.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def add_command():
    back_end.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def delete_command():
    back_end.delete(selected_tuple[0])

def update_command():
    back_end.update(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

window = Tk()
window.wm_title("Bookstore")

# label for entry box
l1 = Label(window,text = "Title")
l1.grid(column =0 , row =0 )
l2 = Label(window,text = "Author")
l2.grid(column =2 , row =0 )
l3 = Label(window,text = "Year")
l3.grid(column =0 , row =1 )
l4 = Label(window,text = "ISBN")
l4.grid(column = 2, row = 1)

# empty box for book search
title_text = StringVar()
e1 = Entry(window,textvariable =title_text)
e1.grid(column = 1,row = 0)
author_text = StringVar()
e2 = Entry(window,textvariable =author_text)
e2.grid(column = 3,row = 0)
year_text = StringVar()
e3 = Entry(window,textvariable =year_text)
e3.grid(column = 1,row = 1)
isbn_text = StringVar()
e4 = Entry(window,textvariable =isbn_text)
e4.grid(column = 3,row = 1)
# box that shows the data associated w each book
list1=Listbox(window,height=6,width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

list1.bind('<<ListboxSelect>>',get_selected_row)
# scroll bar
sb1=Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#buttons for entries
b1 = Button(window, text="View All", width=12,command=view_command)
b1.grid(row=2,column=3)
b2 = Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3,column=3)
b3 = Button(window, text="Add Entry", width=12,command=add_command)
b3.grid(row=4,column=3)
b4 = Button(window, text="Update Selected", width=12,command = update_command)
b4.grid(row=5,column=3)
b5 = Button(window, text="Delete Selected", width=12, command = delete_command)
b5.grid(row=6,column=3)
b5 = Button(window, text="Close", width=12, command = window.destroy
b5.grid(row=7,column=3)

window.mainloop()
