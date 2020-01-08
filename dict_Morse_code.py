莫尔斯电码采用了短脉冲和长脉冲（分别为点和点划线） 来编码字母和数字。例如，字母“A”是点划线，“B”是点划线点点。

如文件Mos.txt 文件所示：

A .- B ... C -.-. D -.. E . F ..-. G --. H .... I ..

J .--- K -.- L .-.. M -- N -. O --- P .--.

Q --.- R .-. S ... T - U ..- V ...- W .—

X -..- Y -.-- Z --..

keys = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
values = ['.-','...','-.-','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']
mydict = dict(zip(keys, values))
str = input("请输入一段英文：")
for s in str:
    print(mydict[s], end=' ')
print()