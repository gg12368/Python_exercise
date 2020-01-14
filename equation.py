计算一元二次方程ax2+bx+c 的根是公式。因为负数的平方根是虚的，所以可以使用平方根里面的表达式（称为差别式）先进地判别，检查根型。如果判别式是负数，根是虚的。如果判别式是零，只有一个根；如果判别式是正的，有两个根。写一个程序，使用二次方根式得到实根，即忽略虚根。使用判别式确定有一个根或两个根，然后显示出答案。
a)源代码如下：
import math
a=float(input("Please input a:"))
b=float(input("Please input b:"))
c=float(input("Please input c:"))
disc = b*b-4*a*c #判别式
if disc<0:
    print("方程有虚根。")
else:
    result1=(-b+math.sqrt(disc))/(2*a)
    result2=(-b-math.sqrt(disc))/(2*a)
    if disc==0:
        print ("result:{}".format(result1))
    else:
        print("result1={},result2={}".format(result1,result2))
