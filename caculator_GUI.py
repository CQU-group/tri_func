import tkinter as TK
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

from caculate import caculator   #导入计算模块（包含三角函数+四则运算功能）

# 主窗口
root = TK.Tk( )   #创建TK事例
root.title("CQU's Caculator")   #名称
root.resizable(0,0) #设置主窗口是否可以通过鼠标拉伸改变大小。此处设置为不能
root.geometry('580x370')   #主窗口初试尺寸大小
# root.geometry('400x370')

result = TK.StringVar( )   #用来显示结果的可变文本
equation = TK.StringVar( )   #用来显示算式的可变文本
result.set(' ')   #赋初值
equation.set('0')   #赋初值

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
# 按下MC时，清空算式行与结果行
def clear( ):
    equation.set('0')
    result.set(' ')
# 按下CQU时，显示组员信息
# def CQU( ):
#     equation.set('0')
#     result.set('王云;冯雪;苏舣;秦弦;袁慧敏')   #后面把大家的信息补充完整
# 按下等于号时计算结果
def run( ):
    temp = equation.get( )
    temp = temp.replace('×','*')  #为了方便调用caculator函数
    temp = temp.replace('÷','/')
    temp = temp.replace('sin', '!')
    temp = temp.replace('cos', '@')
    temp = temp.replace('tan', '#')
    temp = temp.replace('arcs', '$')
    temp = temp.replace('arcc', '%')
    temp = temp.replace('arct', '^')
    temp = temp.replace('Π', '180')

    # 写一个小彩蛋，CQUer！
    if temp == '王云;冯雪;苏舣;秦弦;袁慧敏':               # 暗号
        result.set('现代软件工程，我爱你!')               # 彩蛋
        return 0
    print(temp)
    answer = caculator.caculator(temp)
    #answer = '%.2f'%answer
    result.set(str(answer))


# 结果显示框
show_uresult = TK.Label(root,bg='white',fg = 'black',font = ('Arail','15'),bd='0',textvariable =equation,anchor='se')
show_dresult = TK.Label(root,bg='white',fg = 'black',font = ('Arail','30'),bd='0',textvariable=result,anchor='se')
show_uresult.place(x='10',y='10',width='560',height='50')
show_dresult.place(x='10',y='60',width='560',height='50')

# 按钮
# 第一行按钮
button_7 =TK.Button(root,text='7',bd=8,font=16,bg='dark gray', fg='black',command= lambda : getnum('7'))
button_7.place(x = '10',y='150',width = '60',height='40')
button_8 =TK.Button(root,text='8',bd=8,font=16,bg='dark gray', fg='black',command= lambda : getnum('8'))
button_8.place(x = '90',y='150',width = '60',height='40')
button_9 =TK.Button(root,text='9',bd=8,font=16,bg='dark gray', fg='black',command= lambda : getnum('9'))
button_9.place(x = '170',y='150',width = '60',height='40')
button_lbracket=TK.Button(root,text='(',bd=8,font=16,bg='gray',fg='White',command= lambda : getnum('('))
button_lbracket.place(x = '250',y='150',width = '60',height='40')
button_rbracket=TK.Button(root,text=')',bd=8,font=16,bg='gray',fg='White',command= lambda : getnum(')'))
button_rbracket.place(x = '330',y='150',width = '60',height='40')
button_sin =TK.Button(root,text='sin',bd=8,font=16,bg='gray',fg='White',command= lambda : getnum('sin'))
button_sin.place(x = '410',y='150',width = '60',height='40')
button_arcsin =TK.Button(root,text='arcsin',bd=8,font=16,bg='gray',fg='White',command= lambda : getnum('arcs'))
button_arcsin.place(x = '490',y='150',width = '80',height='40')

# 第二行按钮
button_4 =TK.Button(root,text='4',bd=8,font=16,bg='dark gray', fg='black',command= lambda : getnum('4'))
button_4.place(x = '10',y='205',width = '60',height='40')
button_5 =TK.Button(root,text='5',bd=8,font=16,bg='dark gray', fg='black',command= lambda : getnum('5'))
button_5.place(x = '90',y='205',width = '60',height='40')
button_6 =TK.Button(root,text='6',bd=8,font=16,bg='dark gray', fg='black',command= lambda : getnum('6'))
button_6.place(x = '170',y='205',width = '60',height='40')
button_plus =TK.Button(root,text='+',bd=8,font=16,bg='gray',fg='White',command= lambda : getnum('+'))
button_plus.place(x = '250',y='205',width = '60',height='40')
button_minus =TK.Button(root,text='—',bd=8,font=16,bg='gray',fg='White',command= lambda : getnum('-'))
button_minus.place(x = '330',y='205',width = '60',height='40')
button_cos =TK.Button(root,text='cos',bd=8,font=16,bg='gray',fg='White',command= lambda : getnum('cos'))
button_cos.place(x = '410',y='205',width = '60',height='40')
button_arccos=TK.Button(root,text='arccos',bd=8,font=16,bg='gray',fg='White',command= lambda : getnum('arcc'))
button_arccos.place(x = '490',y='205',width = '80',height='40')
# 第三行按钮
button_1 =TK.Button(root,text='1',bd=8,font=16,bg='dark gray', fg='black',command= lambda :getnum('1'))
button_1.place(x = '10',y='260',width = '60',height='40')
button_2 =TK.Button(root,text='2',bd=8,font=16,bg='dark gray', fg='black',command= lambda : getnum('2'))
button_2.place(x = '90',y='260',width = '60',height='40')
button_3 =TK.Button(root,text='3',bd=8,font=16,bg='dark gray', fg='black',command= lambda : getnum('3'))
button_3.place(x = '170',y='260',width = '60',height='40')
button_multiplication =TK.Button(root,text='×',bd=8,font=16,bg='gray',fg='White',command= lambda : getnum('×'))
button_multiplication.place(x = '250',y='260',width = '60',height='40')
button_division =TK.Button(root,text='÷',bd=8,font=16,bg='gray',fg='White',command= lambda : getnum('÷'))
button_division.place(x = '330',y='260',width = '60',height='40')
button_tan =TK.Button(root,text='tan',bd=8,font=16,bg='gray',fg='White',command= lambda : getnum('tan'))
button_tan.place(x = '410',y='260',width = '60',height='40')
button_arctan =TK.Button(root,text='arctan',bd=8,font=16,bg='gray',fg='White',command= lambda : getnum('arct'))
button_arctan.place(x = '490',y='260',width = '80',height='40')
# 第四行按钮
button_point =TK.Button(root,text='.',bd=8,font=16,bg='dark gray', fg='black',command= lambda : getnum('.'))
button_point.place(x = '10',y='315',width = '60',height='40')
button_0 =TK.Button(root,text='0',bd=8,font=16,bg='dark gray', fg='black',command= lambda : getnum('0'))
button_0.place(x = '90',y='315',width = '60',height='40')
button_equal=TK.Button(root,text='=',bd=8,font=16,bg='gray',fg='White',command= run)
button_equal.place(x = '170',y='315',width = '60',height='40')
button_back =TK.Button(root,text='←',bd=8,font=16,bg='gray',fg='White',command=back)
button_back.place(x = '250',y='315',width = '60',height='40')
button_MC =TK.Button(root,text='AC',bd=8,font=16,bg='maroon',fg='White',command = clear)
button_MC.place(x = '330',y='315',width = '60',height='40')
button_pi =TK.Button(root,text='Π',bd=8,font=16,bg='gray',fg='White',command = lambda : getnum('Π'))
button_pi.place(x = '410',y='315',width = '60',height='40')
button_FX =TK.Button(root,text='CQU',bd=8,font=16,bg='gray',fg='White',command = lambda : getnum('王云;冯雪;苏舣;秦弦;袁慧敏'))
button_FX.place(x = '490',y='315',width = '80',height='40')


root.mainloop( )
