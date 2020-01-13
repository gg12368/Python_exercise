通过Input（）函数任意输入三条边长，经过简单的计算后，判断三条边长能否构成三角形，并确定是类型的三角形，如（等边，等腰，一般三角形）。
源代码如下：
a=float(input("Please input a:"))
b=float(input("Please input b:"))
c=float(input("Please input c:"))
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("等边三角形。")
    elif a==b or a==c or b==c:
        print("等腰三角形。")
    elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
        print("直角三角形。")
    else: print("一般三角形。")
else: print("三条边不能构成三角形。")
