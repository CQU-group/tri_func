# _*_ coding: utf-8 _*_

import random
from unittest import TestCase, main
from caculator import caculator as cl

test_number = 10000#测试次数

class MyTestCase(TestCase):


    # def test_base(self):#测试基础功能
    #
    #     for i in range(test_number):
    #         x = random.uniform(0,32767)
    #         y = random.uniform(0,32767)
    #
    #         string = 'x+y'
    #         string = list(string)
    #         string[0] = x
    #         string[2] = y
    #         equation = " ".join(map(str,string))
    #
    #         print('x = ', x)
    #         print('y = ', y)
    #         result_calculator = cl(equation)
    #         print('result_calculator = ' , result_calculator)
    #         result_true = round(eval(equation),8)
    #         print('result_true = ', result_true)
    #         self.assertEqual(result_calculator, result_true, "+功能，执行结果不正确")
    #
    #         string = 'x-y'
    #         string = list(string)
    #         string[0] = x
    #         string[2] = y
    #         equation = " ".join(map(str, string))
    #         result_calculator = cl(equation)
    #         result_true = round(eval(equation),8)
    #         self.assertEqual(result_calculator, result_true, "-功能，执行结果不正确")
    #
    #         string = 'x*y'
    #         string = list(string)
    #         string[0] = x
    #         string[2] = y
    #         equation = " ".join(map(str, string))
    #         result_calculator = cl(equation)
    #         result_true = round(eval(equation),8)
    #         self.assertEqual(result_calculator, result_true, "*功能，执行结果不正确")
    #
    #         string = 'x/y'
    #         string = list(string)
    #         string[0] = x
    #         string[2] = y
    #         equation = " ".join(map(str, string))
    #         result_calculator = cl(equation)
    #         if y != 0:
    #             result_true = round(eval(equation),8)
    #         else:
    #             result_true = "出现错误，请重新输入！"
    #         self.assertEqual(result_calculator, result_true, "/功能，执行结果不正确")

    def test_sin(self):#测试sin

        for i in range(test_number):
            x = random.uniform(-32768, 32767)
            string = 'sin(x)'
            string = list(string)
            if x <= 0:
                string[4] = '-'
                string[5] = x
            else:
                string[4] = x
            equation = " ".join(map(str,string))


            result_calculator = cl(equation)
            result_true = round(eval(equation),8)
            self.assertEqual(result_calculator, result_true, "sin功能，执行结果不正确")






if __name__ == '__main__':
    main()