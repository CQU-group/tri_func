import re
import process

def eq_format(eq):
    '''
    :param eq: 输入的算式字符串
    :return: 格式化以后的列表，如['60','+','7','*','8']
    '''
    # [\d\.]+    (    +    -     *     /
    # !:sin   @:cos   #:tan    $:arcsin     %:arccos      ^:arctan   (运算符)
    format_list = re.findall('[\d\.]+|\(|\+|\-|\*|\/|\!|\@|\#|\$|\%|\^|\)',eq)#
    print("list",format_list)
    return format_list


def trigonometric(eq):        #弧度制三角函数
    order=8
    eq[1] = float(eq[1])
    print(eq[1])
    if eq[0] == '!':
         eq[0] = process.taylor_sin((eq[1]),order)
         del eq[1]
         print('sin',eq)
    elif eq[0] == '@':
         eq[0] = process.taylor_cos((eq[1]), order)
         del eq[1]
         print('cos', eq)
    elif eq[0] == '$':
         eq[0]= process.taylor_arcsin((eq[1]), order)
         del eq[1]
         print('arcsin', eq)
    elif eq[0] == '^':
        eq[0] = process.taylor_arctan((eq[1]), order)
        del eq[1]
        print('arctan', eq)
    return eq


def caculator(eq):        #角度
        pi = 3.141592653589793
        format_list = eq_format(eq)  # 格式化列表
        format_list[1] = (float(format_list[1]) * pi) / 180
        if format_list[0]=='$' and format_list[1]>1:
            ans=("输入绝对值不应大于180")
            return ans
        ans = trigonometric(format_list)  # 执行三角函数计算
        if len(ans) == 2:
            ans = -float(ans[1])
        else:
            ans = float(ans[0])
        ans = round(ans, 8)
        return ans




def caculator_2(eq):      #弧度
        format_list = eq_format(eq)  # 格式化列表
        if format_list[0]=='$' and float(format_list[1])>float(1):
            ans=("输入绝对值不应大于1")
            return ans
        ans = trigonometric(format_list)  # 执行三角函数计算
        if len(ans) == 2:
            ans = -float(ans[1])
        else:
            ans = float(ans[0])
        ans=round(ans,8)
        return ans
