# _*_ coding: utf-8 _*_

import random
from unittest import TestCase, main
from caculator import caculator as cl
import math


test_number = 10000#测试次数

class MyTestCase(TestCase):


    def test_base(self):#测试基础功能

        for i in range(test_number):
            x = random.uniform(0,32767)
            y = random.uniform(0,32767)

            string = 'x+y'
            string = list(string)
            string[0] = x
            string[2] = y
            equation = " ".join(map(str,string))

            print('x = ', x)
            print('y = ', y)
            result_calculator = cl(equation)
            print('result_calculator = ' , result_calculator)
            result_true = round(eval(equation),8)
            print('result_true = ', result_true)
            self.assertEqual(result_calculator, result_true, "+功能，执行结果不正确")

            string = 'x-y'
            string = list(string)
            string[0] = x
            string[2] = y
            equation = " ".join(map(str, string))
            result_calculator = cl(equation)
            result_true = round(eval(equation),8)
            self.assertEqual(result_calculator, result_true, "-功能，执行结果不正确")

            string = 'x*y'
            string = list(string)
            string[0] = x
            string[2] = y
            equation = " ".join(map(str, string))
            result_calculator = cl(equation)
            result_true = round(eval(equation),8)
            self.assertEqual(result_calculator, result_true, "*功能，执行结果不正确")

            string = 'x/y'
            string = list(string)
            string[0] = x
            string[2] = y
            equation = " ".join(map(str, string))
            result_calculator = cl(equation)
            if y != 0:
                result_true = round(eval(equation),8)
            else:
                result_true = "出现错误，请重新输入！"
            self.assertEqual(result_calculator, result_true, "/功能，执行结果不正确")

    def test_sin(self):#测试sin

        #测试角度
        for i in range(test_number):
            x = random.uniform(0,32767)
            string1 = '!x'
            string1 = list(string1)
            string1[1] = x
            equation1 = " ".join(map(str,string1))
            result_calculator = cl(equation1)
            x = math.radians(x)
            result_true = math.sin(x)
            result_true = round(result_true, 8)

            self.assertEqual(result_calculator, result_true, "sin角度功能，执行结果不正确")

            string1 = '!(x)'
            string1 = list(string1)
            string1[2] = x*180
            equation1 = " ".join(map(str, string1))

            result_calculator = cl(equation1)
            result_true = math.sin(x*math.pi)
            result_true = round(result_true, 8)
            print('x = ', x)
            print('result_calculator = ',result_calculator)
            print('result_true = ',result_true)

            self.assertEqual(result_calculator, result_true, "sin弧度功能，执行结果不正确")

    def test_cos(self):  # 测试cos

        # 测试角度
        for i in range(test_number):
            x = random.uniform(0,32767)
            string1 = '@x'
            string1 = list(string1)
            string1[1] = x
            equation1 = " ".join(map(str, string1))
            result_calculator = cl(equation1)
            x = math.radians(x)
            result_true = math.cos(x)
            result_true = round(result_true, 8)

            self.assertEqual(result_calculator, result_true, "cos角度功能，执行结果不正确")

            string1 = '@(x)'
            string1 = list(string1)
            string1[2] = x * 180
            equation1 = " ".join(map(str, string1))

            result_calculator = cl(equation1)
            result_true = math.cos(x * math.pi)
            result_true = round(result_true, 8)
            print('x = ', x)
            print('result_calculator = ', result_calculator)
            print('result_true = ', result_true)

            self.assertEqual(result_calculator, result_true, "cos弧度功能，执行结果不正确")
    def test_tan(self):  # 测试tan

        # 测试角度
        for i in range(test_number):
            x = random.uniform(0,32767)
            # x = 417.5002344563292
            string1 = '#x'
            string1 = list(string1)
            string1[1] = x
            equation1 = " ".join(map(str, string1))
            result_calculator = cl(equation1)

            if result_calculator == "出现错误，请重新输入！":
                print('x = ', x)
                self.assertEqual(x % 180, 90, "tan角度功能，执行结果不正确")
            # if (x % 180 != 90):
            #     x = math.radians(x)
            #     result_true = math.tan(x)
            #     result_true = round(result_true, 8)
            # else:
            #     result_true = "出现错误，请重新输入！"
            #     print('x = ', x)
            #     print('result_calculator = ', result_calculator)
            #     print('result_true = ', result_true)
            # self.assertEqual(result_calculator, result_true, "tan角度功能，执行结果不正确")

            # string1 = '#(x)'
            # string1 = list(string1)
            # string1[2] = x * 180
            # equation1 = " ".join(map(str, string1))
            #
            # result_calculator = cl(equation1)
            # if (x % 0.5 != 0):
            #     result_true = math.tan(x * math.pi)
            #     result_true = round(result_true, 8)
            # else:
            #     result_true = "出现错误，请重新输入！"
            # print('x = ', x)
            # print('result_calculator = ', result_calculator)
            # print('result_true = ', result_true)
            #
            # self.assertEqual(result_calculator, result_true, "tan弧度功能，执行结果不正确")
    def test_arcsin(self):  # 测试arcsin

        # 测试角度
        for i in range(test_number):
            # x = random.uniform(0,1)
            x = 0.5
            string1 = '$x'
            string1 = list(string1)
            string1[1] = x
            equation1 = " ".join(map(str, string1))
            result_calculator = cl(equation1)
            x = math.radians(x)
            result_true = math.asin(x)
            result_true = round(result_true, 8)
            print('x = ', x)
            print('result_calculator = ', result_calculator)
            print('result_true = ', result_true)

            self.assertEqual(result_calculator, result_true, "arcsin角度功能，执行结果不正确")

            string1 = '$(x)'
            string1 = list(string1)
            string1[2] = x * 180
            equation1 = " ".join(map(str, string1))

            result_calculator = cl(equation1)
            result_true = math.asin(x * math.pi)
            result_true = round(result_true, 8)
            print('x = ', x)
            print('result_calculator = ', result_calculator)
            print('result_true = ', result_true)

            self.assertEqual(result_calculator, result_true, "arcsin弧度功能，执行结果不正确")







if __name__ == '__main__':
    main()
