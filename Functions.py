def add(a,b):
    return a + b

def ckprime(num):
    for i in range(2,num):
        if num % i == 0 :
            return False
        
    return True
        
def revstr(rev):
    wd = ""
    for ch in rev :
        wd = ch + wd
    return wd

print("1.Addition.")
print("2.Check number is Prime or Not.")
print("3.To Reverse a String.")

num = int(input("Enter choice : "))

if num==1 :
    a=int(input("Enter Int1 : "))
    b=int(input("Enter Int2 : "))
    c = add(a,b)
    print(c)
elif num == 2 :
    x=int(input("Enter an Int : "))
    y = ckprime(x)
    if y:
        print("Prime")
    else:
        print("Not Prime")
elif num == 3 :
    rev = input("Enert string : ")
    z = revstr(rev)
    print(z)
else:
    print("Invalid Choice.")

