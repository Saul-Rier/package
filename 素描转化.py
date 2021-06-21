from tkinter import *
from tkinter.tix import Tk, Control, ComboBox  #升级的组合控件包
from PIL import Image,ImageTk
import tkinter.filedialog
from skimage import filters
import matplotlib.pyplot as plt
import numpy as np


picture_path = None

def plot_image(image,title):
    plt.imshow(image,cmap='gray')
    plt.title(title)
    plt.show()

def get_pixel(grey_image,x,y):
    #获取图像像素
    pixel = np.zeros((x,y))
    for i in range(grey_image.size[0]):
        for j in range(grey_image.size[1]):
            temp = grey_image.getpixel((i,j))  # 获取图片的每一个像素  (i,j) 的 RBG 值
            pixel[i,j] = temp
    return pixel

def literary_sketch(image):
    sobel_1 = filters.sobel(image)
    sobel_2 = filters.sobel(sobel_1)
    sobel_3 = filters.sobel(sobel_2)
    sobel_4 = filters.sobel(sobel_3)
    sobel_5 = filters.sobel(sobel_4)
    sobel_6 = filters.sobel(sobel_5)
    sobel_7 = filters.sobel(sobel_6)
    sobel_8 = filters.sobel(sobel_7)
    sobel_9 = filters.sobel(sobel_8)
    sobel_10 = filters.sobel(sobel_9)
    sobel_11 = filters.sobel(sobel_10)
    sobel_2_1 = sobel_2-sobel_1
    sobel_3_2 = sobel_3-sobel_2
    sobel_4_3 = sobel_4-sobel_3
    sobel_5_4 = sobel_5-sobel_4
    sobel_6_5 = sobel_6-sobel_5
    sobel_7_6 = sobel_7-sobel_6
    sobel_8_7 = sobel_8-sobel_7
    sobel_9_8 = sobel_9-sobel_8
    sobel_10_9 = sobel_10-sobel_9
    sobel_11_10 = sobel_11-sobel_10
    difference = sobel_2_1+sobel_3_2+sobel_4_3+sobel_5_4+sobel_6_5+sobel_7_6+sobel_8_7+sobel_9_8+sobel_10_9+sobel_11_10
    return difference

def choose_picture():
    global picture_path
    path_ = tkinter.filedialog.askopenfilename()
    # 获取图片路径
    path.set(path_)
    picture_path = path_
    img_open = Image.open(e1.get())
    img_open = img_open.resize((600,400))
    img = ImageTk.PhotoImage(img_open)

    l1.config(image=img)
    l1.image = img

def transform():
    global picture_path
    i = Image.open(picture_path)
    m, n = i.size
    print(m)
    print(n)
    l = i.convert('L')  # 转化为灰度值
    the_new_order = literary_sketch(l)
    plt.imshow(the_new_order, cmap='gray')
    plt.axis('off')
    file_name = '1.png'
    plt.savefig(file_name)
    picture_path = 'E:/pycharm/dark/soda/智能程序设计/1.png'

def show():
    global picture_path
    path_ = picture_path
    path.set(path_)
    picture_path = path_
    img_open = Image.open(e1.get())
    img = ImageTk.PhotoImage(img_open)
    l2.config(image=img)
    l2.image = img

root = Tk()
path = StringVar()
Button(root, text='Select', command=choose_picture).pack()
Button(root, text='Transform', command=transform).pack()
Button(root, text='Show', command=show).pack()
e1 = Entry(root, state='readonly', text=path)
e1.pack()
l1 = Label(root,width = 600,height = 400)
l1.pack(side = 'left')
l2 = Label(root,width = 600,height = 400)
l2.pack(side = 'right')
root.mainloop()
