# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

time = 0

for first in range(1,5):
    for second in range(1,5):
        for third in range(1,5):
            if((first != second) and (second != third) and (first != third)):
                print(first,second,third)
                time += 1

print("總共有%d個" %(time))
















