n = input("Enter a value: ")

rev = ''
for i in n:
    if i.isdigit():
        rev = i + rev  # Prepend digit to reverse the number

if n == rev:
    print("Palindrome")
else:
    print("Not a palindrome")
