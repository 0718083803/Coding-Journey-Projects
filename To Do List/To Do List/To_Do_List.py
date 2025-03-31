from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("To Do List")
root.geometry('327x362')

counter=0
#ADD FUNCTION
def add():
    x = entry.get()
    global counter
    #ONLY ADDING IF TEXTBOX HAS SOMETHING
    if len(x) <1 :
       messagebox.showwarning(message="Please Enter Something!!")
    else: 
        counter+=1
        listbox.insert(counter,str(x))
  
#REMOVE FUNCTION
def remove():
    slctd= listbox.curselection()
    listbox.delete(slctd)
#Complete Function


#LISTBOX
listbox = Listbox(root,height =7,width=30,bg="#333333",font="Algerian 15")
listbox.grid(row=0,column=0,columnspan=3)
#TEXTBOX
entry = Entry(root,width=30,font='Arial 15')
entry.grid(row=1,column=0,columnspan=2)
#ADD BUTTON
add_btn = Button(root,text="ADD",command=add,width=15,bg="Black",fg='White')
add_btn.grid(row=2,column=0,padx=30)
#REMOVE BUTTON
remove_btn = Button(root,text="REMOVE",command=remove,width=15,bg="Black",fg='White')
remove_btn.grid(row=2,column=1)

root.mainloop()