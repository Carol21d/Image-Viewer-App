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
status = Label(root, text="Image 1 of " + str(len(image_list)))

my_label = Label(image=my_img)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_back
    global button_forward

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(
        root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    status = Label(root, text=" " + str(image_number) +
                   " " + str(len(image_list)))
    status.grid(row=2, columnspan=3, sticky=W+E)


def back(image_number):
    global my_label
    global button_back
    global button_forward

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(
        root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


button_back = Button(root, text="<<", command=back)
button_exit = Button(root, text="EXIT PROGRAM", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))


button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)
status.grid(row=2, columnspan=3, sticky=W+E)


root.mainloop()
