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

image_list = [my_img, my_img_2, my_img_3, my_img_4, my_img_5]


my_label = Label(image=my_img)
my_label.grid(row=0, column=0, columnspan=3)


def forward():
    return


def back():
    return


button_back = Button(root, text="<<", command=back)
button_exit = Button(root, text="EXIT PROGRAM", command=root.quit)
button_forward = Button(root, text=">>", command=forward)


button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)


root.mainloop()
