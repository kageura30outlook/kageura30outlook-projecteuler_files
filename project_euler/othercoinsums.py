price = 200
coin = [200,100,50,20,10,5,2,1]

for i in range (8):#coin no kazu wo kokoni ireru (koko)
    count = price / coin[i]+count
    price = price % coin[i]

print(count)