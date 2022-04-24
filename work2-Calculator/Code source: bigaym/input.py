# -*- coding: utf-8 -*-
"""
@function： 判断str类型数据是否可以转为float
@author: 敖钰民
@last_time： 2022年3月27日19:42:11
"""


def isFloat(input: str):
    """
    检测输入是否为float
    :param input:字符串
    :return:True 是； False 否
    """
    try:
        float(input)
    except:
        return False
    else:
        return True
