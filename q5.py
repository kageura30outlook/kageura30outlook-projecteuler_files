repeater = 1
i = 0
while repeater == 1:
    i = 1 + i
    counter = 0
    for r in range (1,5):
        num = i%r
        if num == 0:
            counter = counter + 1
    if counter == 3:
        repeater = 2
print(i)