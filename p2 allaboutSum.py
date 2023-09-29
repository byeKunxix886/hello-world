# 計算the sum of the given series 1+2+3+ . . . . . .(N terms)
sum1 = 0
target1 = int(input('您好，請輸入要加總到的值: '))
for i in range(1,target1+1): #i為循環變量，target1用來參考，在此+1是因為左閉右開
    sum1 += i

print(sum1)

#注意關鍵字sum 不可打錯

#Solution2：公式解 Arithmetic series 等差級數，演算法速度較快
sum1 = 0
sum1 = (1/2) * target1 * (target1 + 1)
print(sum1)