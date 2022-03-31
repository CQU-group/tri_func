import re
import math
import numpy as np
from math import fabs
from math import pi

def eq_format(eq):
    '''
    :param eq: 输入的算式字符串
    :return: 格式化以后的列表，如['60','+','7','*','8']
    '''
    # [\d\.]+    (    +    -     *     /
    # !:sin   @:cos   #:tan    $:arcsin     %:arccos      ^:arctan   (运算符)
    format_list = re.findall('[\d\.]+|\(|\+|\-|\*|\/|\!|\@|\#|\$|\%|\^|\)',eq)#
    print("1",format_list)
    return format_list

def change(eq,count):
    '''
    :param eq: 刚去完括号或者乘除后的格式化列表
    :param count: 发生变化的元素的索引
    :return: 返回一个不存在 '+-' ,'--'类的格式化列表
    '''
    if eq[count] == '-':
        if eq[count-1] == '-':
            eq[count-1] = '+'
            del eq[count]
        elif eq[count-1] == '+':
            eq[count-1] = '-'
            del eq[count]
    return eq
#先括号，再三角函数，再乘除，最后加减
#————————————————————自己瞎写————————————————————
def remove_trigonometric(eq):  #去掉三角函数
    count = 0
    for i in eq:
        if i == '!':
            if eq[count + 1] != '-':
                eq[count] = math.sin(math.radians(float(eq[count+1])))
                del (eq[count+1])  #删除变量
                # del (eq[count])
                print('sin',eq)
            elif eq[count + 1] == '-':
                eq[count] = math.sin(math.radians(-float(eq[count + 2])))
                del (eq[count + 1])
                del (eq[count + 1])
                print('sin(-)', eq)
            eq = change(eq, count - 1)
            return remove_trigonometric(eq)
        elif i == '@':
            if eq[count + 1] != '-':
                eq[count] = math.cos(math.radians(float(eq[count+1])))
                del (eq[count+1])
                # del (eq[count])
            elif eq[count + 1] == '-':
                eq[count] = math.cos(math.radians(-float(eq[count+2])))
                del (eq[count + 1])
                del (eq[count + 1])
            eq = change(eq, count - 1)
            return remove_trigonometric(eq)
        elif i == '#':
          # try:
           if eq[count + 1] != '-':
             if (int(float(eq[count+1] )+ 90) % 180 != 0):
                eq[count] = math.tan(math.radians(float(eq[count + 1])))
                del (eq[count + 1])
                eq = change(eq, count - 1)
                # del (eq[count])
             else:
                 return remove_trigonometric(eq)
           elif eq[count + 1] == '-':
             if (int(float(eq[count+2])+ 90) % 180 != 0):
                eq[count] = math.tan(math.radians(-float(eq[count + 2])))
                del (eq[count + 1])
                del (eq[count + 1])
                eq = change(eq, count - 1)
             else:
                 return remove_trigonometric(eq)
           return remove_trigonometric(eq)
          # except:
          #    eq=None
          #    print('error')
        elif i == '$':
            if eq[count + 1] != '-':
                eq[count] = np.degrees(np.arcsin(float(eq[count + 1])))
                del (eq[count+1])
                # del (eq[count])
            elif eq[count + 1] == '-':
                eq[count] = np.degrees(np.arcsin(-float(eq[count + 2])))
                del (eq[count + 1])
                del (eq[count + 1])
            eq = change(eq, count - 1)
            return remove_trigonometric(eq)
        elif i == '%':
            if eq[count + 1] != '-':
                eq[count] = np.degrees(np.arccos(float(eq[count + 1])))
                del (eq[count+1])
                # del (eq[count])
            elif eq[count + 1] == '-':
                eq[count] = np.degrees(np.arccos(-float(eq[count + 2])))
                del (eq[count + 1])
                del (eq[count + 1])
            eq = change(eq, count - 1)
            return remove_trigonometric(eq)
        elif i == '^':
            if eq[count + 1] != '-':
                eq[count] = np.degrees(np.arctan(float(eq[count + 1])))
                del (eq[count+1])
                # del (eq[count])
            elif eq[count + 1] == '-':
                eq[count] = np.degrees(np.arctan(-float(eq[count + 2])))
                del (eq[count + 1])
                del (eq[count + 1])
            eq = change(eq, count - 1)
            return remove_trigonometric(eq)

        count = count + 1
    print('三角函数计算eq',eq)
    return eq
#__________________________自己瞎写______________________________


def remove_multiplication_division(eq):   #去掉乘除号
    '''
    :param eq: 带有乘除号的格式化列表
    :return: 去除了乘除号的格式化列表
    '''
    count = 0
    for i in eq:
      try:
        if i == '*':
            if eq[count+1] != '-':
                eq[count-1] = float(eq[count-1]) * float(eq[count+1])
                del(eq[count])
                del(eq[count])
                print('3', eq)
            elif eq[count+1] == '-':
                eq[count] = float(eq[count-1]) * float(eq[count+2])
                eq[count-1] = '-'
                del(eq[count+1])
                del(eq[count+1])
                print('-3', eq)
            eq = change(eq,count-1)
            return remove_multiplication_division(eq)
        elif i == '/':
            if eq[count+1] != '-':
                eq[count-1] = float(eq[count-1]) / float(eq[count+1])
                del(eq[count])
                del(eq[count])
            elif eq[count+1] == '-':
                eq[count] = float(eq[count-1]) / float(eq[count+2])
                eq[count-1] = '-'
                del(eq[count+1])
                del(eq[count+1])
            eq = change(eq,count-1)
            return remove_multiplication_division(eq)
        count = count + 1
      except:
        eq = ("error")
    print('乘除计算eq', eq)
    return eq


def remove_plus_minus(eq):   #去掉加减号
    '''
    :param eq: 只带有加减号的格式化列表
    :return: 计算出整个列表的结果
    '''
    count = 0
    if eq[0] != '-':
        sum = float(eq[0])
    else:
        sum = 0.0
    for i in eq:
        if i == '-':
            sum = sum - float(eq[count+1])
        elif i == '+':
            sum = sum + float(eq[count+1])
        count = count + 1
    if sum >= 0:
        eq = [str(sum)]
    else:
        eq = ['-',str(-sum)]
    print('加减计算eq', eq)
    return eq

def calculate(s_eq): #输入不带括号的格式化列表
    '''
    :param s_eq: 不带括号的格式化列表
    :return: 计算结果
    '''
    # if '!' or '@'or '#'or '$'or '%'or '^' in s_eq:
    if '!' or'@' in s_eq:
        s_eq =remove_trigonometric(s_eq)
    if '%'or '^' in s_eq:
        s_eq = remove_trigonometric(s_eq)
    if '#'or '$' in s_eq:
        s_eq = remove_trigonometric(s_eq)

    if '*' or '/' in s_eq:
        s_eq = remove_multiplication_division(s_eq)

    if '+' or '-' in s_eq:
        s_eq = remove_plus_minus(s_eq)
    return s_eq



def simplify(format_list):
    '''
    :param format_list: 输入的算式格式化列表如['60','+','7','*','8']
    :return: 通过递归去括号，返回简化后的列表
    '''

    bracket = 0     # 用于存放左括号在格式化列表中的索引
    count = 0
    for i in format_list:
        if i == '(':
            bracket = count
        elif i == ')':
            temp = format_list[bracket + 1 : count]
            # print(temp)
            new_temp = calculate(temp)
            format_list = format_list[:bracket] + new_temp + format_list[count+1:]
            format_list = change(format_list,bracket)     # 解决去括号后会出现的--  +- 问题
            return simplify(format_list)            # 递归去括号
        count = count + 1
    return format_list                     # 当递归到最后一层的时候，不再有括号，因此返回列表


def caculator(eq):
 try:
    format_list = eq_format(eq)    # 格式化列表
    s_eq = simplify(format_list)   #执行去括号操作
    ans = calculate(s_eq)   # 执行三角函数、乘除、加减 计算
    if len(ans) == 2:
        ans = -float(ans[1])
    else:
        ans = float(ans[0])
    # return '%.2f'%ans
    return round(ans,8)
 except:
    ans= ("出现错误，请重新输入！")
    return ans



'''    
#测试
if __name__ == '__main__':
    equation = '1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
    ans = caculator(equation)
    print('eval运算结果：',eval(equation))
    print('程序运算结果：',ans)
'''
