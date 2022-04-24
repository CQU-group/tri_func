import tkinter as TK
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

import caculate   #  测试计算


i=1    # 全局参数

# 主窗口
root = TK.Tk( )   #创建TK事例
root.title("CQU's Caculator")   #名称
root.resizable(0,0) #设置主窗口是否可以通过鼠标拉伸改变大小。此处设置为不能
root.geometry('460x370')   #主窗口初试尺寸大小
# root.geometry('400x370')

result = TK.StringVar( )   #用来显示结果的可变文本
equation = TK.StringVar( )   #用来显示算式的可变文本
change = TK.StringVar( )   # 用来显示计算弧度/角度
result.set(' ')   #赋初值
equation.set('0')   #赋初值
change.set('角度')  #赋初值

# 获得按下的数字或者符号
def getnum(num):
    temp = equation.get( )
    temp2 = result.get( )
    print(temp)
    print(temp2)
    if temp2 != ' ' :
        temp = '0'
        temp2 = ' '
        result.set(temp2)
    if (temp=='0'):
        temp = ''
    temp = temp + num
    equation.set( temp )
    print(equation)
# 按下退格键时，去除最后一个字符
def back( ):
    temp = equation.get( )
    equation.set(temp[:-1])

# 按下AC时，清空算式行与结果行
def clear( ):
    equation.set('0')
    result.set(' ')

# i=1   # 全局变量
# 实现三角函数计算 角度/弧度制 的转换
def Change():
    global i
    i += 1
    if i % 2 == 0:
        temp = change.set("弧度")
        temp11='弧度'
    else:
        temp = change.set("角度")
        temp11 = '角度'
    print("i=",i,"三角函数进行",temp11,"计算")  # 通过run窗口观察计算运行情况

def run( ):
    temp = equation.get( )
    # temp = temp.replace('×','*')  #为了方便调用caculator函数
    # temp = temp.replace('÷','/')
    temp = temp.replace('sin', '!')
    temp = temp.replace('cos', '@')
    # temp = temp.replace('tan', '#')
    temp = temp.replace('arcs', '$')
    # temp = temp.replace('arcc', '%')
    temp = temp.replace('arct', '^')
    # temp = temp.replace('Π', '180')   Tag2.0 提供的计算模块没有实现这些功能

    # 写一个小彩蛋，可以用于表白哦
    if temp == '王云;冯雪;苏舣;秦弦;袁慧敏':               # 暗号
        result.set('现代软件工程，我爱你!')               # 彩蛋或者表白语
        return 0
    print(temp)

    # i += 1
    if i % 2 == 0:   # 这里调用的i 不是全局变量i，而是通过Change()函数执行后的i
        temp2 = "弧度"
    else:
        temp2 = "角度"

    print("i=", i, '正在执行',temp2,'计算！')  # 通过run窗口观察计算运行情况

    if temp2 == "角度":
        answer = caculate.caculator(temp)  # 计算角度
    else:
        answer = caculate.caculator_2(temp)  # 计算弧度

    #answer = '%.8f'%answer  # 保留小数位数
    result.set(str(answer))

# 结果显示框
show_change = TK.Label(root,bg='white',fg = 'green',font = ('Arail','12'),bd='0',textvariable = change,anchor='se')  # 显示计算角度/弧度
show_uresult = TK.Label(root,bg='white',fg = 'black',font = ('Arail','15'),bd='0',textvariable = equation,anchor='se')  # 显示输入
show_dresult = TK.Label(root,bg='white',fg = 'black',font = ('Arail','25'),bd='0',textvariable=result,anchor='se')  # 显示结果

show_change.place(x='10',y='10',width='40',height='50')
show_uresult.place(x='50',y='10',width='400',height='50')
show_dresult.place(x='10',y='60',width='440',height='50')


# 按钮

# 第一行按钮
button_7 =TK.Button(root,text='7',bd=8,font=16,bg='dark gray', fg='black',command= lambda : getnum('7'))
button_7.place(x = '10',y='150',width = '60',height='40')
button_8 =TK.Button(root,text='8',bd=8,font=16,bg='dark gray', fg='black',command= lambda : getnum('8'))
button_8.place(x = '90',y='150',width = '60',height='40')
button_9 =TK.Button(root,text='9',bd=8,font=16,bg='dark gray', fg='black',command= lambda : getnum('9'))
button_9.place(x = '170',y='150',width = '60',height='40')
button_sin =TK.Button(root,text='sin',bd=8,font=16,bg='gray',fg='White',command= lambda : getnum('sin'))
button_sin.place(x = '250',y='150',width = '90',height='40')
button_cos =TK.Button(root,text='cos',bd=8,font=16,bg='gray',fg='White',command= lambda : getnum('cos'))
button_cos.place(x = '360',y='150',width = '90',height='40')


# 第二行按钮
button_4 =TK.Button(root,text='4',bd=8,font=16,bg='dark gray', fg='black',command= lambda : getnum('4'))
button_4.place(x = '10',y='205',width = '60',height='40')
button_5 =TK.Button(root,text='5',bd=8,font=16,bg='dark gray', fg='black',command= lambda : getnum('5'))
button_5.place(x = '90',y='205',width = '60',height='40')
button_6 =TK.Button(root,text='6',bd=8,font=16,bg='dark gray', fg='black',command= lambda : getnum('6'))
button_6.place(x = '170',y='205',width = '60',height='40')
button_arcsin =TK.Button(root,text='arcsin',bd=8,font=16,bg='gray',fg='White',command= lambda : getnum('arcs'))
button_arcsin.place(x = '250',y='205',width = '90',height='40')
button_arctan =TK.Button(root,text='arctan',bd=8,font=16,bg='gray',fg='White',command= lambda : getnum('arct'))
button_arctan.place(x = '360',y='205',width = '90',height='40')


# 第三行按钮
button_1 =TK.Button(root,text='1',bd=8,font=16,bg='dark gray', fg='black',command= lambda :getnum('1'))
button_1.place(x = '10',y='260',width = '60',height='40')
button_2 =TK.Button(root,text='2',bd=8,font=16,bg='dark gray', fg='black',command= lambda : getnum('2'))
button_2.place(x = '90',y='260',width = '60',height='40')
button_3 =TK.Button(root,text='3',bd=8,font=16,bg='dark gray', fg='black',command= lambda : getnum('3'))
button_3.place(x = '170',y='260',width = '60',height='40')
button_back =TK.Button(root,text='←',bd=8,font=16,bg='gray',fg='White',command=back)
button_back.place(x = '250',y='260',width = '90',height='40')
button_Change =TK.Button(root,text='角度/弧度',bd=8,font=12,bg='gray',fg='White',command=Change)
button_Change.place(x = '360',y='260',width = '90',height='40')


# 第四行按钮
button_point =TK.Button(root,text='.',bd=8,font=16,bg='dark gray', fg='black',command= lambda : getnum('.'))
button_point.place(x = '10',y='315',width = '60',height='40')
button_0 =TK.Button(root,text='0',bd=8,font=16,bg='dark gray', fg='black',command= lambda : getnum('0'))
button_0.place(x = '90',y='315',width = '60',height='40')
button_equal=TK.Button(root,text='=',bd=8,font=16,bg='gray',fg='White',command= run)
button_equal.place(x = '170',y='315',width = '60',height='40')
button_AC =TK.Button(root,text='AC',bd=8,font=16,bg='maroon',fg='White',command = clear)
button_AC.place(x = '250',y='315',width = '90',height='40')
button_FX =TK.Button(root,text='Tag2.0',bd=8,font=16,bg='gray',fg='White',command = lambda : getnum('王云;冯雪;苏舣;秦弦;袁慧敏'))
button_FX.place(x = '360',y='315',width = '90',height='40')






root.mainloop( )