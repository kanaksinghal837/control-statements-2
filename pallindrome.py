n =  int(input("Enter a value: "))

rev = 0
while n >0 :
    digit = n % 10 
    rev = rev *10 + digit
    num = num //10

if n == rev:
    print("Palindrome")
else:
    print("Not a palindrome")

