num:int = 1234
res:int = 0
r: int = num
while r > 0:
    res = res * 10 + r % 10  # Add the last digit of r to s
    r = r // 10  # Remove the last digit from r

print(res == num)  # Output: 4321
