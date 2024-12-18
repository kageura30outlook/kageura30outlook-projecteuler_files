price = 200
coin = [200,100,50,20,10,5,2,1]

for i in range (8):#Put number of coins here
    count = price / coin[i]+count
    price = price % coin[i]

print(count)
