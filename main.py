from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
import os
from stegano import lsb

root = Tk()
root.title("Steganography Image Encryption")
root.geometry("700x500+150+180")
root.resizable(False,False)
root.config(bg="black")

def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select Image File',
                                      filetype=(("PNG file","*.png"),
                                                ("JPG file","*.jpg"),("JPEG file","*.jpeg"),("All file","*.txt")))
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lb1.configure(image=img,width=250,height=250)
    lb1.image=img

def hide():
    global secret
    message = text1.get(1.0,END)
    secret = lsb.hide(str(filename),message)
    if secret:
        print("Text hide in Image")

def show():
    show = lsb.reveal(filename)
    text1.delete(1.0,END)
    text1.insert(END,show)
    if show:
        print("Hidden text are shown")

def save():
    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG file", "*.png"),("JPG file", "*.jpg"),("JPEG file", "*.jpeg"),("All files", "*.*")]
    )
    if save_path:
        secret.save(save_path)
        print("Image saved successfully!")

icon = PhotoImage(file="logo.png")
root.iconphoto(False,icon)

logo = PhotoImage(file="security.png")
Label(root,image=logo,bg = "black").place(x=10,y=0)

Label(root,text="  Steganography Image Encryption",bg="black",fg="yellow",font="arial 20 bold").place(x=100,y=20)

f1 = Frame(root,bd=2,bg="black",width=320,height=280,relief=RAISED)
f1.place(x=20,y=80)

lb1 = Label(f1,bg="black")
lb1.place(x=40,y=10)

f2 = Frame(root,bd=3,bg="grey",width=310,height=280,relief=RAISED)
f2.place(x=370,y=80)

text1 = Text(f2,font="Robot 20",bg="white",fg="black",relief=RAISED,wrap=WORD)
text1.place(x=0,y=0,width=300,height=270)

Button(text="Open Image",width=10,height=2,font="arial 8 bold",command=showimage).place(x=70,y=400)
Button(text="Save Image",width=10,height=2,font="arial 8 bold",command=save).place(x=190,y=400)

Button(text="Hide Data",width=10,height=2,font="arial 8 bold",command=hide).place(x=430,y=400)
Button(text="Show Data",width=10,height=2,font="arial 8 bold",command=show).place(x=550,y=400)
root.mainloop()
