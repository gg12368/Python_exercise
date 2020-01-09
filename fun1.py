编写函数，判断一个整数是否为素数，并编写主程序调用该函数。
(1)源代码如下：
#判断是否为素数
def judge(number):
    #素数大于1
    if number > 1:
        for i in range(2,number):
            if number%i==0:
                 print(number,"不是素数")
                 break
        else:
           print(number,"是素数")
    else:
        print(number,"不是素数")

number = int(input("Please input a number:"))
judge(number)
