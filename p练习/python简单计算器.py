import re
#匹配整数或小数的乘除法，包括了开头存在减号的情况
mul_div=re.compile("(-?\d+)(\.\d+)?(\*|/)(-?\d+)(\.\d+)?")
#匹配整数或小数的加减法，包括了开头存在减号的情况
plus_minus = re.compile("(-?\d+)(\.\d+)?(-|\+)(-?\d+)(\.\d+)?")
#匹配括号
bracket=re.compile("\([^()]*\)")
#匹配乘法的时候出现乘以负数的情况，包括了开头存在减号的情况
mul_minus_minus = re.compile("(-?\d+)(\.\d+)?(\*-)(\d+)(\.\d+)?")
#匹配除法的时候出现乘以负数的情况，包括了开头存在减号的情况
div_minus_minus = re.compile("(-?\d+)(\.\d+)?(/-)(\d+)(\.\d+)?")


#定义一个两位数的加减乘除法的运算，匹配左边的右边的数字和左边的数字，然后进行计算
def touble_cale(str_expire):
    if str_expire.count("+") == 1:
        right_num = float(str_expire[(str_expire.find("+")+1):])
        left_num = float(str_expire[:str_expire.find("+")])
        return str(right_num+left_num)
    elif str_expire[1:].count("-") == 1:
        right_num = float(str_expire[:str_expire.find("-",1)])
        left_num = float(str_expire[(str_expire.find("-", 1) + 1):])
        return str(right_num - left_num)
    elif str_expire.count("*") == 1:
        right_num = float(str_expire[:str_expire.find("*")])
        left_num = float(str_expire[(str_expire.find("*")+1):])
        return str(right_num * left_num)
    elif str_expire.count("/") == 1:
        right_num = float(str_expire[:str_expire.find("/")])
        left_num = float(str_expire[(str_expire.find("/") + 1):])
        return str(right_num / left_num)


#定义一个方法用于判断是否存在乘以负数和除以负数的情况
def judge_mul_minus(str_expire):
    #判断公式中乘以负数的部分
    if len(re.findall("(\*-)", str_expire)) != 0:
        #调用上面的正则取得*-的公式
        temp_mul_minus = mul_minus_minus.search(str_expire).group()
        #将匹配的部分的*-换成*并将-放到前面
        temp_mul_minus_2 = temp_mul_minus.replace(temp_mul_minus,"-" + temp_mul_minus.replace("*-","*"))
        #经更改的的部分与原来的部分进行替换
        str_expire=str_expire.replace(temp_mul_minus,temp_mul_minus_2)
        return judge_mul_minus(str_expire)
        #return str_expire
    # 判断公式中除以负数的部分
    elif len(re.findall(r"(/-)", str_expire)) != 0:
        # 调用上面的正则取得/-的公式
        temp_dev_minus = div_minus_minus.search(str_expire).group()
        # 将匹配的部分的/-换成/并将-放到前面
        temp_dev_minus_2 = temp_dev_minus.replace(temp_dev_minus,"-" + temp_dev_minus.replace("/-","/"))
        # 经更改的的部分与原来的部分进行替换
        str_expire = str_expire.replace(temp_dev_minus,temp_dev_minus_2)
        return judge_mul_minus(str_expire)
    #调用change_sign将公式中的++换成= +-换成-
    return change_sign(str_expire)

#定义一个方法取将--更改为+ +-改为-
def change_sign(str_expire):
    if len(re.findall(r"(\+-)", str_expire)) != 0:
        str_expire = str_expire.replace("+-", "-")
        return change_sign(str_expire)
    elif len(re.findall(r"(--)", str_expire)) != 0:
        str_expire = str_expire.replace("--", "+")
        return change_sign(str_expire)
    return str_expire


#定义一个方法用于计算只有加减乘除的公式，优先处理乘法
def cale_mix(str_expire):
    #如果公式中出现符号数字的情况即+5  -6 *8  /8的这种情况直接放回数字否则则先计算乘除在处理加减
    while len(re.findall("[-+*/]",str_expire[1:])) != 0:
        if len(re.findall("(\*|/)",str_expire)) != 0:
            str_expire = str_expire.replace(mul_div.search(str_expire).group(),touble_cale(mul_div.search(str_expire).group()))
        elif len(re.findall("(\+|-)",str_expire)) !=0:
            str_expire = str_expire.replace(plus_minus.search(str_expire).group(),touble_cale(plus_minus.search(str_expire).group()))
    return str_expire

#定义一个方法用于去括号,并调用上述的方法进行计算
def remove_bracket(str_expire):
    #判断公式中是否有括号
    if len(bracket.findall(str_expire)) == 0:
        return cale_mix(judge_mul_minus(str_expire))
    elif len(bracket.findall(str_expire))!=0:
        while len(bracket.findall(str_expire)) !=0:
            #print(bracket.search(str_expire).group())
            #只有存在括号优先处理括号中的内容并对内容进行替换，直到没有括号位置
            str_expire = str_expire.replace(bracket.search(str_expire).group(),cale_mix(judge_mul_minus(bracket.search(str_expire).group()[1:-1])))
        str_expire = cale_mix(judge_mul_minus(str_expire))
        return str_expire


if __name__ == "__main__":
    while True:
        user_input_expire = input("请输入你的公式:(不要带空格,q表示退出):")
        print("%s=%s" %(user_input_expire,remove_bracket(user_input_expire)))
        continue