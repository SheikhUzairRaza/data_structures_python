num = 5783 
n = num 
count = 0 
while num > 0 :
    count += 1
    num = num//10
print(count)

#OR

num = 5783 
import math
def num_count(num):
    return int(math.log10(num)+1)
num_count(num)
