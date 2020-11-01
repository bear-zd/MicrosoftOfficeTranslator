# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 23:47:23 2020

@author: a8275
"""


import tkinter as tk
from tkinter.tix import Tk, Control, ComboBox  #升级的组合控件包
from tkinter.messagebox import showinfo, showwarning, showerror #各种类型的提示框

root=tk.Tk()
root.title("Document Translator")    # 设置窗口标题
root.geometry("800x450")    # 设置窗口大小 注意：是x 不是*
root.resizable(width=True, height=False) # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
root.tk.eval('package require Tix')  #引入升级包，这样才能使用升级的组合控件

header = tk.Label(root,#简介
    text = '这是一个简单的小程序，能够将你的文档利用API进行翻译',  #文本
    bg ='green',   #字体的背景颜色
    font = ('微软雅黑',12),  #字体和大小
    width = 800 , height = 2)  #字体所占的宽度和高度
header.pack()



frame10=tk.Frame(root)
frame10.pack()
group=tk.LabelFrame(frame10,text='制作者',padx=5,pady=5)
group.grid()
w=tk.Label(group,text='zidea')
w.pack()

root.mainloop()