#!/usr/bin/env python
# -*- coding: utf8 -*-
from Tkinter import *
from pygame import mixer
import sh
import time

# class Win(Tk):

#     def __init__(self,master=None):
#         Tk.__init__(self,master)
#         self.overrideredirect(True)
#         self._offsetx = 0
#         self._offsety = 0
#         self.bind('<Button-1>',self.clickwin)
#         self.bind('<B1-Motion>',self.dragwin)

#     def dragwin(self,event):
#         x = self.winfo_pointerx() - self._offsetx
#         y = self.winfo_pointery() - self._offsety
#         self.geometry('+{x}+{y}'.format(x=x,y=y))

#     def clickwin(self,event):
#         self._offsetx = event.x
#         self._offsety = event.y

app = Tk()

# w = Canvas(app, width=200, height=100)
# w.pack()

# w.create_line(0, 0, 200, 100)
# w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

# w.create_rectangle(50, 25, 150, 75, fill="blue")

def soud():
    mixer.init()
    if mixer.get_init():
        mixer.music.load('pop.ogg')
        mixer.music.play(0)
        time.sleep(.5)
        mixer.music.stop()
    else:
        print "Not Checked !!"

soud()


def say_hi():
        print "hi there, everyone!"

def pop():
    # mixer.init()
    # mixer.music.load('pop.mp3')
    # mixer.music.play(0)
    # time.sleep(1.5)
    app.destroy()

def fix_w(x,y):
    app.minsize(x, y)
    app.maxsize(x+100, y+100)

app.title("My APP")
app.geometry("400x500")
app.update()
fix_w(app.winfo_width(), app.winfo_height())
app.configure(background='#546e7a')
# app.wm_attributes('-type', 'splash')
app.wm_attributes('-alpha', '.95')

# Label
label1 = Label(text="", fg="#e84118", bg="#546e7a", font=('FontAwesome', 30))
label1.place(relx=0.5, rely=0.3, anchor='center')

ur = str(sh.whoami()).strip('\n')
# str(ur)
label2 = Label(text="hi " + ur + " !!", fg="#ffffff", bg="#546e7a", font=('Lobster 1.4', 30))
label2.place(relx=0.5, rely=0.4, anchor='center')

label3 = Label(fg="#ffffff", bg="#546e7a", font=('Raleway', 22))
label3.place(relx=0.5, rely=0.5, anchor='center')

def tim():
    tm = time.strftime('%l : %M : %S')
    label3.config(text=tm )
    label3.after(200, tim)
    
tim()

# Button
# style = Style()
# style.map("C.TButton",padding=20,
#     foreground=[('pressed', 'red'), ('active', 'blue')],
#     background=[('pressed', '!disabled', 'black'), ('active', 'white')]
#     )
button1 = Button(text="",padx=10,pady=8,fg="#cf6a87",activeforeground="#ffffff", highlightthickness = 0, bd = 0,border=0,bg="#546e7a",activebackground="#546e7a",font=('FontAwesome', 20),relief=FLAT,command=pop)
# button1["command"] = say_hi
button1.place(relx=0.5, rely=0.7, anchor='center')
# button2 = Button(text="Exit", fg="red", bg="black")
# button2["command"] = quit
# button2.grid(column=2,row=1)
# print(sh.whoami)
# app.iconbitmap(default='/home/meliodus/Documents/ivex_c2.png')
img = Image("photo", file="tk.png")
app.tk.call('wm','iconphoto',app._w,img)
app.mainloop()
