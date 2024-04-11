import tkinter as tk
import re
from tkinter import END
my_w = tk.Tk()
my_w.geometry("430x400")
my_w.title("Autocomplete-DeskTop-App")
font1 = ('Times',24,'bold')

#datasource_from_google_sheets
#import pygsheets
#path = '' #get json file from google cloud
#gc = pygsheets.authorize(service_account_file = path)
#sh = gc.open('my_sheet')
#wk1 = sh[0]
#my_list = wk1.get_col(2, include_tailing_empty = false)
#my_list = wk1.get_values('B1','B14')
#print(my_list)

#datasource_from_database
#from sqlalchemy import create_engine
#my_conn = create_engine("")
#q = "select query"
#my_cursor = my_conn.execute(q)
#result = my_cursor.fetchall()
#print(result)
#my_list(r for r, in result)
#print(my_list)


my_list = ["Aecde" ,"adba" ,"acbd" ,"abded" ,"bdbd" ,"baba" ,"bcbc" ,"bdbd"] #source

l0 = tk.Label(text='Autocomplete', font=font1)
l0.grid(row=0, column=1)
def my_upd(my_widget):
    my_w = my_widget.widget
    index = (my_w.curselection()[0])
    value = my_w.get(index)
    e1_str.set(value)
    l1.delete(0, END)

def my_down(my_widget):
    l1.focus()
    l1.selection_set(0)

e1_str = tk.StringVar()
e1 = tk.Entry(my_w ,font = font1 ,textvariable = e1_str)
e1.grid(row = 1 ,column = 1 ,padx = 50 ,pady = 10)
l1 = tk.Listbox(my_w ,height = 6 ,font = font1 ,relief = 'flat', bg = 'SystemButtonFace', highlightcolor = 'SystemButtonFace')
l1.grid(row = 2 ,column = 1)

def get_data(*args):
    search_str = e1.get() #user entered String
    l1.delete(0, END)
    for element in my_list:
        if(re.match(search_str ,element ,re.IGNORECASE)):
            l1.insert(tk.END,element)

#l1.bind("<<ListboxSelect>>", my_upd)
e1.bind("<Down>", my_down)

l1.bind("<Right>", my_upd)

l1.bind("<Return>", my_upd)

e1_str.trace('w', get_data)

#print(my_w['bg'])
my_w.mainloop() #keep the window open