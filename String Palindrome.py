text = input("Enter a String : ")
rev = ""

for ch in text:
    rev = ch + rev

if str(text) == rev :
    print("Palindrome.")
else :
    print("Not a Plaindrome.")