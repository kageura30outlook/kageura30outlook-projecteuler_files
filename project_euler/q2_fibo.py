fibo = [0] * 10

fibo[0] = 1
fibo[1] = 2
for i in range(2,10):
    fibo[i] = fibo[i-2] + fibo[i-1]

print(fibo)
