owari = 1
i = 0
while owari == 1:
    i = 1 + i
    counter = 0
    for r in range (1,5):
        rem = i%r
        if rem == 0:
            counter = counter + 1
    if counter == 3:
        owari = 2
print(i)