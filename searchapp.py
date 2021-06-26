from tkinter import *
from tkinter.scrolledtext import ScrolledText
import wikipedia as wiki

root = Tk()
root.title("GRUB")
root.geometry('320x480')
root.configure(bg='white')


def search():
    search_data = ent.get()
    data = wiki.summary(search_data, sentences = 10)

    ent.set('')
    text.delete(0.0,END)

    search_lbl['text'] = "Searching result for : {}".format(search_data)
    text.insert(0.0,data)


def enter_pressed(event):
    search()


our = Label(root,text='GRUB',font=('arial',20),bg='white',fg='green')
our.place(x=120,y=0)

ent = StringVar()
search_entry = Entry(root, width = 30, font=('arial',12), bd=2,relief= RIDGE, textvariable=ent)
search_entry.bind('<Return>',enter_pressed)
search_entry.place(x=50,y=30)

search_lbl = Label(root,text='Searching result for: ',font=('arial',12,'bold'),bg='white')
search_lbl.place(x=15,y=70)

text = ScrolledText(root,font=('times',12),bd=4,relief=SUNKEN,wrap=WORD)
text.place(x=15,y=100,height=300,width=300)

search_btn = Button(root,text='Search',font=('arial',12,'bold'),width=10,command=search)
search_btn.place(x=15,y=420)

clear_btn = Button(root,text='Clear', font=('arial',12,'bold'),width=10,
                   command=lambda :text.delete(0.0,END))

clear_btn.place(x=122,y=420)

exit_btn = Button(root,text='Exit', font=('arial',12,'bold'),width=10,command=root.quit)
exit_btn.place(x=230,y=420)



root.mainloop()
