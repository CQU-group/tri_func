import tkinter as tk
import tkinter.messagebox
import re
import math
#from functions import *

root = tk.Tk()
root.minsize(300, 400)      # 窗口大小300*400
root.resizable(0, 0)
root.title('一个计算器')    # 计算器名字

# 计算sin
def sin_t(x):
    return round(math.sin(x),10)


# 计算cos
def cos_t(x):
    return round(math.cos(x), 10)


# 计算tan
def tan_t(x):
    return round(math.tan(x), 10)


# 计算csc
def csc_t(x):
    return round(float(1)/math.sin(x), 10)


# 计算sec
def sec_t(x):
    return round(float(1)/math.cos(x), 10)


#运算符按钮
#第一行
btnback = tkinter.Button(root, text='←', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5,
                         command=lambda x='←': buttonClick(x))
btnback.place(x=0, y=150, width=60, height=45)

btntan = tkinter.Button(root, text='tan', font=('微软雅黑', 20),  fg=('#4F4F4F'), bd=0.5,
                        command=lambda x='tan': buttonClick(x))
btntan.place(x=60, y=150, width=60, height=45)

btncsc = tkinter.Button(root, text='csc', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5,
                                command=lambda x='csc': buttonClick(x))
btncsc.place(x=120, y=150, width=60, height=45)

btnxsec = tkinter.Button(root, text='sec', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5,
                                 command=lambda x='sec': buttonClick(x))
btnxsec.place(x=180, y=150, width=60, height=45)

btnmul1 = tkinter.Button(root, text='+', font=('微软雅黑', 20), fg="#4F4F4F", bd=0.5, command=lambda \
                x='+': buttonClick(x))
btnmul1.place(x=240, y=150, width=60, height=45)

#第二行
btnleft = tkinter.Button(root, text='(', font=('微软雅黑', 20),  fg=('#4F4F4F'), bd=0.5,
                         command=lambda x='(': buttonClick(x))
btnleft.place(x=0, y=195, width=60, height=45)

btnac1 = tkinter.Button(root, text='AC',  font=('黑体', 20),fg='orange',bd=0.5,
                        command=lambda x='AC': buttonClick(x))
btnac1.place(x=60, y=195, width=60, height=45)

btnsin = tkinter.Button(root, text='sin', font=('微软雅黑', 20),  fg=('#4F4F4F'), bd=0.5,
                                command=lambda x='sin': buttonClick(x))
btnsin.place(x=120, y=195, width=60, height=45)

btncos = tkinter.Button(root, text='cos', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5,
                                command=lambda x='cos': buttonClick(x))
btncos.place(x=180, y=195, width=60, height=45)

btnsub1 = tkinter.Button(root, text='-', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='-': buttonClick(x))
btnsub1.place(x=240, y=195, width=60, height=45)

#第三行
btnrigh = tkinter.Button(root, text=')', font=('微软雅黑', 20),fg=('#4F4F4F'), bd=0.5,
                                 command=lambda x=')': buttonClick(x))
btnrigh.place(x=0, y=240, width=60, height=45)

btn71 = tkinter.Button(root, text='7', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='7': buttonClick(x))
btn71.place(x=60, y=240, width=60, height=45)

btn81 = tkinter.Button(root, text='8', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='8': buttonClick(x))
btn81.place(x=120, y=240, width=60, height=45)

btn91 = tkinter.Button(root, text='9', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='9': buttonClick(x))
btn91.place(x=180, y=240, width=60, height=45)

btnadd1 = tkinter.Button(root, text='×', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='×': buttonClick(x))
btnadd1.place(x=240, y=240, width=60, height=45)

#第四行
btnpoint1 = tkinter.Button(root, text='.', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='.': buttonClick(x))
btnpoint1.place(x=0, y=285, width=60, height=45)

btn41 = tkinter.Button(root, text='4', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='4': buttonClick(x))
btn41.place(x=60, y=285, width=60, height=45)

btn51 = tkinter.Button(root, text='5', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='5': buttonClick(x))
btn51.place(x=120, y=285, width=60, height=45)

btn61 = tkinter.Button(root, text='6', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='6': buttonClick(x))
btn61.place(x=180, y=285, width=60, height=45)

btnechu1 = tkinter.Button(root, text='÷', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='÷': buttonClick(x))
btnechu1.place(x=240, y=285, width=60, height=45)

#第五行
btn01 = tkinter.Button(root, text='0', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='0': buttonClick(x))
btn01.place(x=0, y=330, width=60, height=45)

btn11 = tkinter.Button(root, text='1', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='1': buttonClick(x))
btn11.place(x=60, y=330, width=60, height=45)

btn21 = tkinter.Button(root, text='2', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='2': buttonClick(x))
btn21.place(x=120, y=330, width=60, height=45)

btn31 = tkinter.Button(root, text='3', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda \
                x='3': buttonClick(x))
btn31.place(x=180, y=330, width=60, height=45)

btnequ1 = tkinter.Button(root, text='=', bg='orange', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5,
                                command=lambda x='=': buttonClick(x))
btnequ1.place(x=240, y=330, width=60, height=45)





def buttonClick(btn):
    pass

root.mainloop()



