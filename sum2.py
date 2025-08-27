n = input("Enter a value: ")
sum = 0

for i in n:
    if i.isdigit():
        sum += int(i)

print("Sum of digits:", sum)
