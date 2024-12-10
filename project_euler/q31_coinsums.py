price = 200
num = 0
count = 0

while price != 0:
    if 100 <= price:
        price = price-100
        count = count + 1
    elif 50 <= price:
        price = price-50
        count = count + 1
    elif 10 <= price:
        price = price-10
        count = count + 1
    elif 5 <= price:
        price = price-5
        count = count + 1
    elif 1 <= price:
        price = price-1
        count = count + 1

print(count)
