# _*_ coding: utf-8 _*_

import random
from unittest import TestCase, main
from caculate import caculator as cl1
from caculate import caculator_2 as cl2
import math
import numpy as np


test_number = 1000#测试次数

list = []#随机输入

for i in range(10):
    list.append(i)
list.append('+')
list.append('-')
list.append('*')
list.append('/')
list.append('!')
list.append('@')
list.append('#')
list.append('$')
list.append('%')
list.append('^')

class MyTestCase(TestCase):

    '''
    以下包括精度测试与误差测试，若需要测试精度请取消注释
    '''
    def test_sin(self):#测试sin

        # 测试角度
        for i in range(test_number):
            x = random.uniform(0, 32767)
            print('测试用例',x)

            equation1 = '!%d' % x
            result_calculator = round(cl1(equation1), 8)

            result_true = math.sin(x / 180 * math.pi)
            result_true = round(result_true, 8)

            # self.assertEqual(result_calculator, result_true, "sin角度功能，测试用例x = %d，执行结果不正确" % x)

            equation1 = '!%d' % (x)
            result_calculator = round(cl2(equation1), 8)
            result_true = math.sin(x)
            result_true = round(result_true, 8)
            print('x = ', x)
            print('result_calculator = ', result_calculator)
            print('result_true = ', result_true)

            self.assertEqual(result_calculator, result_true, "sin弧度功能，测试用例x = %d，执行结果不正确" % x)

    def test_cos(self):  # 测试cos

        for i in range(test_number):
            x = random.uniform(0, 32767)
            print('测试用例', x)

            equation1 = '@%d' % x
            result_calculator = round(cl1(equation1), 8)

            result_true = math.cos(x / 180 * math.pi)
            result_true = round(result_true, 8)

            self.assertEqual(result_calculator, result_true, "cos角度功能，测试用例x = %d，执行结果不正确" % x)

            result_calculator = round(cl2(equation1), 8)
            result_true = math.cos(x)
            result_true = round(result_true, 8)
            print('x = ', x)
            print('result_calculator = ', result_calculator)
            print('result_true = ', result_true)

            self.assertEqual(result_calculator, result_true, "cos弧度功能，测试用例x = %d，执行结果不正确" % x)

    def test_tan(self):  # 测试tan

        for i in range(test_number):
            x = random.uniform(0, 1)
            print('测试用例', x)

            equation1 = '#%d' % x
            result_calculator = round(cl1(equation1), 8)

            result_true = math.tan(x / 180 * math.pi)
            result_true = round(result_true, 8)

            self.assertEqual(result_calculator, result_true, "tan角度功能，测试用例x = %d，执行结果不正确" % x)

            result_calculator = round(cl2(equation1), 8)
            result_true = math.tan(x)
            result_true = round(result_true, 8)
            print('x = ', x)
            print('result_calculator = ', result_calculator)
            print('result_true = ', result_true)

            self.assertEqual(result_calculator, result_true, "tan弧度功能，测试用例x = %d，执行结果不正确" % x)
    def test_arcsin(self):  # 测试arcsin

        for i in range(test_number):
            x = random.uniform(0, 32767)
            print('测试用例', x)

            equation1 = '#%d' % x
            result_calculator = round(cl1(equation1), 8)

            result_true = math.asin(x / 180 * math.pi)
            result_true = round(result_true, 8)

            self.assertEqual(result_calculator, result_true, "arcsin角度功能，测试用例x = %d，执行结果不正确" % x)

            result_calculator = round(cl2(equation1), 8)
            result_true = math.asin(x)
            result_true = round(result_true, 8)
            print('x = ', x)
            print('result_calculator = ', result_calculator)
            print('result_true = ', result_true)

            self.assertEqual(result_calculator, result_true, "arcsin弧度功能，测试用例x = %d，执行结果不正确" % x)

    def test_arctan(self):  # 测试arccos

        for i in range(test_number):
            x = random.uniform(0, 32767)
            print('测试用例', x)

            equation1 = '#%d' % x
            result_calculator = round(cl1(equation1), 8)

            result_true = math.atan(x / 180 * math.pi)
            result_true = round(result_true, 8)

            self.assertEqual(result_calculator, result_true, "arctan角度功能，测试用例x = %d，执行结果不正确" % x)

            result_calculator = round(cl2(equation1), 8)
            result_true = math.atan(x)
            result_true = round(result_true, 8)
            print('x = ', x)
            print('result_calculator = ', result_calculator)
            print('result_true = ', result_true)

            self.assertEqual(result_calculator, result_true, "arctan弧度功能，测试用例x = %d，执行结果不正确" % x)


if __name__ == '__main__':
    main()
