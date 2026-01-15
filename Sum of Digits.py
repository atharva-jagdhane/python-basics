num = int(input("enter an Integer : "))
y = 0
while num > 0 :
    x = num % 10
    y = y + x
    num = num // 10
print(y)