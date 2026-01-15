num = int(input("enter a number : "))
temp = num
pld = 0
while temp > 0 :
    pld = pld * 10 + (temp % 10)
    temp = temp // 10
if pld == num:
    print("Palindrome.")
else:
    print("Not a palindrome.")