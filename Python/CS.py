#字符串
#'是一个字符
print("'abc'")
#"是一个字符
print('"abc"')
#r''表示内部不转义
print(r'"abc"')
#''',"""可以直接打印多行内容,没区别
print('''line1
line2
line3''')

#布尔值
#and or not 
print(True and False)
print(True or False)
print(not True)

#空值
print(None)

#取整除法
print(10//3)

#单个字符编码
#ord()函数获取字符的整数表示
print(ord('A'))
print(ord('中'))
#chr()函数把编码转换为对应的字符
print(chr(66))
print(chr(25991))
#\u Unicode编码
print('\u4e2d\u6587')
print('\u4e66')
