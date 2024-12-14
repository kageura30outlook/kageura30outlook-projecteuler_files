num = 1
yousei = 0
answer1 = 0
answer2 =0
answer3 = 0
check1 = [285]
check2 = [165]
check3 = [143]
num1 = 285
num2 = 165
num3 = 143
def tri(num1):
    answer = num1 + 1
    answer = answer * num1
    answer1 = answer/2
    return(answer1)
def pent(num2):
    answer = num2 * 3 - 1
    answer = answer * num2
    answer2 = answer/2
    return(answer2)
def hex(num3):
    answer = num3 * 2
    answer = answer - 1
    answer3 = num3 * answer
    return(answer3)
for i in range (1, 100000):
    num = num + 1
    num1 = num1 + 1
    num2 = num2 + 1
    num3 = num3 + 1
    check1.append(tri(num1))
    check2.append(pent(num2))
    check3.append(hex(num3))
for r in range (1,100000):
    print(r)
    if check1[r] in check2:
        print("Rinn")
        if check1[r] in check3:
            print(check1[r])
            break
