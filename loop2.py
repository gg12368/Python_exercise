2.	我国有13 亿人口，如果按人口年增长0.8%计算，多少年后将达到26 亿？

popu = 13.0
year = 0
while True:
    if popu>=26.0:
        print("%d年后人口将达到26亿"%year)
        break
    else:
        popu*=1.008
        year+=1
