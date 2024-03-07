from tkinter import *
from tkinter import ttk
from tkinter import messagebox


win=Tk()
win.title("TODO LIST")
win.geometry("600x600")
win.resizable(False,False)

#Functions
def app():
    try:
        with open("tasklist.txt",'r') as f:
            content=f.readlines()
            for item in content:
                list1.insert(END,item)
    except FileNotFoundError:
        pass

                   
def add_task():
    text=entry1.get()
    
    if text=='':
        messagebox.showinfo('Info', "Please enter some value")
    else:
        list1.insert(END,text)
        entry1.delete(0,END)
        messagebox.showinfo('Info', " The task " + ' "'+ text +'" has been added')
    
def delete_task():
    list1.delete(ANCHOR)
    
def get_details():
    detail = list1.get(0,END)
    print(detail)
    
    with open("tasklist.txt",'w') as f:
        for item in detail:
            if item.endswith('\n'):
                f.write(item)
            else:
                f.write(item+'\n')
    
           
# Frame widget
frame1=Frame(win,width=600,height=600,bg='burlywood3')
frame1.pack(pady=20,expand=1,fill=BOTH)
    
# Scroll widget vertical


label1=Label(frame1, text="TODO LIST", bg='burlywood3',fg='black',font=("Arial bold",20))
label1.pack(pady=10)

scroll1=Scrollbar(frame1)
scroll1.pack(side=RIGHT,fill=Y)

# Listbox

list1=Listbox(frame1, yscrollcommand=scroll1.set)
list1.pack(side=TOP,fill=BOTH,expand=1,padx=20)

#tasks=['doing yoga','dusting', 'cleaning kitchen','reading magazines', 'Reading newspaper', 'Preparing Breakfast','cleaning house', 'Taking bath', 'Doing Pooja','Eating fruits','drinking water','reading books']
#for item in tasks:
 #   list1.insert(END,item)

scroll1.config(command=list1.yview)

entry1=Entry(frame1)
entry1.pack(padx=20, pady=20,fill=BOTH)


add_btn=Button(frame1,text='ADD TASK', activebackground='burlywood1',command=add_task,font=("Arial",15), bg='burlywood1',fg='black')
add_btn.pack(padx=20,pady=20,fill=BOTH,expand=1)


del_btn=Button(frame1,text='DELETE TASK',activebackground='burlywood1',command=delete_task,font=("Arial",15),bg='burlywood1',fg='black')
del_btn.pack(padx=20,pady=20,fill=BOTH,expand=1)

get_btn=Button(frame1,text='GET TASK DETAILS',activebackground='burlywood1',command=get_details,font=("Arial",15),bg='burlywood1',fg='black')
get_btn.pack(padx=20,pady=10,fill=BOTH,expand=1)

label2=Label(frame1,text='',bg='burlywood3',font=("Arial",10),width=20,height=20)
label2.pack(padx=20,pady=20,fill=BOTH)

app()

win.mainloop()
