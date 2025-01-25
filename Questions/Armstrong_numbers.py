import math

def count_dig(num):
    return int(math.log10(num)+1)
num = 1634

def armstr_num(num):
    count = count_dig(num)
    act_num = num
    print(count)
    sum = 0 
    while num > 0 :
       # print(num%10**count) #issue error
        sum = sum + (num%10)**count 
        num = num // 10 
    print(sum == act_num)

armstr_num(num)