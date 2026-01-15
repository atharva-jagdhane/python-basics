text = input("Enter a string : ")
count = 0
for ch in text:
    if ch in  "AEIOUaeiou" :
        count += 1
print(count)