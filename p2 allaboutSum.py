# ===題目1：計算一個等差級數1+2+3+4+...+N的總和是多少 ===
#思路1 使用迴圈硬幹
str1 = [1,3,5,7,9]
sum1 = 0
target1 = int(input('您好，請輸入要加總到的值: '))
for i in range(1,target1+1): #i為循環變量，target1用來參考，在此+1是因為左閉右開
    sum1 += i

print(sum1)

#思路2 公式解 Arithmetic series 等差級數，演算法速度較快
sum1 = 0
sum1 = (1/2) * target1 * (target1 + 1)
print(sum1)


# ===題目2：給一長度為n的陣列，求出每一元素的總和 ===
def printSumofN(arr,n):
    sum1 = 0
    for i in arr:
        sum1+=i

#用for迴圈直接遍歷數據或使用range，直接遍歷則i會變成每個元素1次，所以不可用str1[i]。 

# ===題目3：輪流打印每一個陣列元素 ===
def printAl(arr,n):
    # your code here
    for i in range(0,n,2):
        print('%d'%(arr[i]),end=' ')
