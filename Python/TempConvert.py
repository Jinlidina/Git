#TempConvert.py

#从控制台赋值并保存在变量TempStr中
TempStr = input("请输入带有符号的温度值:")
#判断字符串变量TempStr的最后一个字符是否在F和f中
if TempStr[-1] in ['F','f']:
    #将除最后一个字符外的字符串转换为数字并运算,赋值给C
    C=(eval(TempStr[0:-1]) - 32)/1.8
    #输出精度为两位小数的C"C"
    print("转换后的温度是{:.2f}C".format(C))
#判断字符串变量TempStr的最后一个字符是否在C和c中
elif TempStr[-1] in ['C','c']:
    #将除最后一个字符外的字符串转换为数字并运算,赋值给F
    F = 1.8*eval(TempStr[0:-1]) +32
    #输出精度为两位小数的F"F"
    print("转换后的温度是{:.2f}F".format(F))
else:
    #判断失败,输出错误
    print("输入格式错误")
