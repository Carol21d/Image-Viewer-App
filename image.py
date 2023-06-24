from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title = "Image Viewer App"
root.iconbitmap(
    "C:/Users/d3sig/OneDrive/Desktop/Projects-Python/Image-Viewer-App")

my_img = ImageTk.PhotoImage(Image.open("dead.webp"))
my_img_2 = ImageTk.PhotoImage(Image.open("escarabajo.png"))
my_img_3 = ImageTk.PhotoImage(Image.open("huevo.png"))
my_img_4 = ImageTk.PhotoImage(Image.open("koi.jpg"))
my_img_5 = ImageTk.PhotoImage(Image.open("ornitorrinco.jpg"))


my_label = Label(image=my_img)
my_label.pack()


root.mainloop()
