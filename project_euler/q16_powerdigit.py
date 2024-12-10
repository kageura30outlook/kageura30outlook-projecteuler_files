import math
num = int(input("num:"))
power = int(input("power:"))
total = num**power
answer = 0
s = str(total)
l = len(s)
for i in range (l):
    answer = answer + total%10
    total = math.floor(total/10)
print(answer)
