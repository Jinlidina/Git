#PythonDraw.py

#导入turtle绘图库
import turtle
#设置窗体左上坐标(200,200),宽650,高350
turtle.setup(650,350,200,200)

turtle.penup()
turtle.fd(-250)
turtle .pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()
