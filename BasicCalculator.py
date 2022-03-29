import re
from decimal import *

a =r'1 - 2 * ((2+52-31 +(-22/5) * (6-5*5/3))- (-4*3)/(26-3*2))'
# ＊／运算函数
def shengchu(str):
  calc = re.split("[*/]",str)   #用＊/分割公式
  OP = re.findall("[*/]",str)  #找出所有＊和／号
  ret = None
  for index,i in enumerate(calc):
    if ret:
      if OP[index-1] == "*":
        ret *= float(i)
      elif OP[index-1] == "/":
        ret /= float(i)
    else:
      ret = float(i)
  return ret
# 去掉重复运算,和处理特列+－符号
def del_double(str):
  str = str.replace("++", "+")
  str = str.replace("--", "-")
  str = str.replace("+-","-")
  str = str.replace("- -","-")
  str = str.replace("+ +","+")
  return str
# 计算主控制函数
def calc_contrl(str):
  tag = False
  str = str.strip("()") # 去掉最外面的括号
  str = del_double(str) # 调用函数处理重复运算
  find_ = re.findall("[+-]",str) # 获取所有+－ 操作符
  split_ = re.split("[+-]",str) #正则处理 以+－操作符进行分割，分割后 只剩*/运算符
  if len(split_[0].strip()) == 0: # 特殊处理
    split_[1] = find_[0] + split_[1] # 处理第一个数字前有“－”的情况，得到新的带符号的数字
    # 处理第一个数字前为负数“-"，时的情况，可能后面的操作符为“－”则进行标记
    if len(split_) == 3 and len(find_) ==2:
      tag =True
      del split_[0] # 删除原分割数字
      del find_[0]
    else:
      del split_[0] # 删除原分割数字
      del find_[0] # 删除原分割运算符
  for index, i in enumerate(split_):
    # 去除以*或/结尾的运算数字
    if i.endswith("* ") or i.endswith("/ "):
      split_[index] = split_[index] + find_[index] + split_[index+1]
      del split_[index+1]
      del find_[index]
  for index, i in enumerate(split_):
    if re.search("[*/]",i): # 先计算含*/的公式
      sub_res = shengchu(i) #调用剩除函数
      split_[index] = sub_res
  # 再计算加减
  res = None
  for index, i in enumerate(split_):
    if res:
      if find_[index-1] == "+":
        res += float(i)
      elif find_[index-1] == "-":
        # 如果是两个负数相减则将其相加，否则相减
        if tag == True:
          res += float(i)
        else:
          res -= float(i)
    else:
      # 处理没有括号时会出现i 为空的情况
      if i != "":
        res = float(i)
  return res
if __name__ == '__main__':
  calc_input = input("请输入计算式：" ).strip()
  try:
    if len(calc_input) ==0:
      calc_input = a
    calc_input = r'%s'%calc_input # 做特殊处理，保持字符原形
    flag = True  # 初始化标志位
    result = None  # 初始化计算结果
    # 循环处理去括号
    while flag:
      inner = re.search("\([^()]*\)", calc_input)# 先获取最里层括号内的单一内容
      #print(inner.group())
      # 有括号时计算
      if inner:
        ret = calc_contrl(inner.group()) # 调用计算控制函数
        calc_input = calc_input.replace(inner.group(), str(ret)) # 将运算结果，替换原处理索引值处对应的字符串
        #flag = True
      # 没有括号时计算
      else:
        ret = calc_contrl(calc_input)
        print("计算结果为：%s"% round(ret,8))
        #结束计算标志
        flag = False
  except:
    print("你输入的公式有误请重新输入！")

