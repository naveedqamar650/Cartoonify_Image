import os
from tkinter import *

def quit(*args):
    root.destroy()


root = Tk()
root.attributes("-fullscreen", False)
root.geometry("600x350")
root.configure(background='pink')
root.bind("<Escape>", quit)
root.bind("x", quit)

Label(root, text="Image Filters", bg="pink", fg="white",
      font=("arial", 64)).pack()

def image():
    os.system('image.py')


def cartoon():
    os.system('cartoon.py')


def edge():
    os.system('edgy.py')


def blur():
    os.system('blurry.py')


Button(root, text="Cartoonify", bd=10,
       command=cartoon, font=('times new roman', 12), bg="pink", fg="black", height=5, width=7).place(x=100, y=220)

Button(root, text="Image", bd=10,
       command=image, font=('times new roman', 12), bg="pink", fg="black", height=5, width=7).place(x=200, y=220)

Button(root, text="Blurry", bd=10,
       command=blur, font=('times new roman', 12), bg="pink", fg="black", height=5, width=7).place(x=300, y=220)

Button(root, text="Edgy", bd=10,
       command=edge, font=('times new roman', 12), bg="pink", fg="black", height=5, width=7).place(x=400, y=220)

Button(root, text="EXIT", bd=10,
       command=quit, font=('times new roman', 12), bg="pink", fg="black", height=2, width=10).place(x=637, y=700)

# if __name__ == '__main__':
root.mainloop()
