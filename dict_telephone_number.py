使用字典来创建程序，提示用户输入电话号码，并用英文单词形式显示数字。例如：输入138则显示“one three eight”。

最终输出会在同一行显示

numWord=["zero","one","two","three","four","five","six","seven","eight","nine"]
phoneNum=str(input("输入电话号码："))
for i in range(len(phoneNum)):
    getNum=ord(phoneNum[i])-ord('0')
    print(numWord[getNum],end=" ")
