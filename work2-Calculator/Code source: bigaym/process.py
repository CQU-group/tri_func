# -*- coding: utf-8 -*-
"""
@function： 判断str类型数据是否可以转为float
@author: 敖钰民
@last_time： 2022年3月27日19:42:11
"""
# PI的值
PI = 3.141592653589793

def pow(x: int, n:int):
    """
    返回x的n次方
    :param x: 求n次方的数
    :param n:n次方
    :return:
    """
    if n==1:
        return x
    m = 1
    for i in range(n-1):
        m = m*x
    return m


def taylor_sin(x: float, order: int):
    """
    使用泰勒公式近似 sin x
    :param x: x
    :param order:精度
    :return: 结果
    """
    # 调整到[-PI, PI]
    ratio = int(x/PI)
    if (ratio % 2) != 0:
        if ratio < 0:
            ratio = ratio - 1
        elif ratio > 0:
            ratio = ratio + 1
    x = x - ratio*PI


    e = x   # 迭代项
    s = x   # 初始项
    for i in range(2, 999999999):
        e = -1*e*x*x/((2*i-1)*(2*i-2))
        if abs(e) < 1/(pow(10, order+2)):
            return s
        s += e
    return s


def taylor_cos(x: float, order: int):
    """
    使用泰勒公式近似 cosx
    :param x: x
    :param order:精度
    :return: 结果
    """
    # 调整到[-PI, PI]
    ratio = int(x / PI)
    if (ratio % 2) != 0:
        if ratio < 0:
            ratio = ratio - 1
        elif ratio > 0:
            ratio = ratio + 1
    x = x - ratio * PI

    e = 1
    s = 1
    for i in range(1, 999999999):
        e = -1*e*x*x/((2*i-1)*(2*i))
        if abs(e) < 1/(pow(10, order+2)):
            return s
        s += e
    return s


def taylor_arcsin(x: float, order: int):
    """
    计算arcsin
    :param x:[-1, 1]
    :param order: 精确位数
    :return: 结果
    """
    if x == 1:
        return PI/2
    elif x == -1:
        return -PI/2
    if -1 < x < 1:
        e = x
        s = x
        i = 1
        n = 1
        cft = 1
        while True:
            e = e * x * x
            cft = cft * (2 * i - 1) / (2 * i)
            e1 = cft / (2 * n + 1)
            e1 = e * e1
            s = e1 + s
            i = i + 1
            n = n + 1

            if abs(e1) <= 1/(pow(10, order+2)):
                return s


def atan(x: float, order: int):
    """
    返回-1~1之间的arctan的值
    :param x: [-1,1]
    :param order: 精度
    :return:
    """
    e = x
    s = x
    for i in range(2, 999999999):
        e = -1 * e * x * x * (2 * i - 3) / (2 * i - 1)
        if abs(e) < 1 / (pow(10, order+1)):
            return s
        s += e
    return s

def taylor_arctan(x: float, order: int):
    """
    使用泰勒公式近似 arctan x
    :param x: x
    :param order:阶数，越高越准但越慢
    :return: 结果,输入错误是返回None
    注意：arctan(x) + arctan(1/x) = pi/2
    """
    if (x >= -1) and (x <= 1):
        return atan(x, order)
    elif x > 1:
        return PI/2 - atan(1/x, order)
    elif x < -1:
        return -(PI/2 - atan(-1/x, order))
    else:
        return None


if __name__ == '__main__':
    import math
    x = 0.6
    print(taylor_arcsin(x, 8))
    print(math.asin(x))
    import numpy as np
