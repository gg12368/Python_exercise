密码登录程序。要求：建立一个登录窗口,要求输入帐号和密码。设定用户名为”zhangshan”，密码为“Python123”若;用户名正确，密码正确，则显示 “Zhangshan先生，欢迎你 !”如;果用户名错误，则显示“用户名错误，请重新输入! ”;
若密码不正确,显示“对不起,密码错误,无法登录! ”。
源代码如下：
username = input("请输入用户名：")
code = input("请输入密码：")
if username == "zhangshan" and code =="Python123":
    print("Zhangshan先生，欢迎你！")
elif username != "zhangshan":
    print ("用户名错误，请重新输入！")
else :
print("对不起，密码错误，无法登录！")
