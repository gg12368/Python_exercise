设有三个变量a,b,c,分别对三个变量赋值，并对三个变量进行排序。如a=5,b=7,c=6,则排序结果为b>c>a。
a)源代码如下：
a=float(input("Please input a:"))
b=float(input("Please input b:"))
c=float(input("Please input c:"))
if a>b:
    if b>c:
        print("a>b>c")
    elif c>b:
        if a>c:
            print("a>c>b")
        else :
            print("c>a>b")
elif b>a:
    if a>c:
        print("b>a>c")
    elif c>a:
        if b>c:
            print("b>c>a")
        else :
            print("c>b>a")
