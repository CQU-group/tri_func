"""
名称：example
功能：使用泰勒公式近似sinx
作者：bigaym
时间：2022年3月12日14:07:49
"""


def taylor_sin(x:float, order:int):
    """
    使用泰勒公式近似sinx
    :param x: x
    :param order:阶数，越高越准但越慢
    :return: 结果
    """
    e = x
    s = x
    for i in range(2, order):
        e = -1*e*x*x/((2*i-1)*(2*i-2))
        s += e
    return s


if __name__ == '__main__':
    import time
    import math

    startTime = time.time()
    x = 3.14
    print(taylor_sin(x, 200))
    testTime = time.time()

    print(math.sin(x))
    mathTime = time.time()
    print(testTime-startTime, mathTime-testTime)