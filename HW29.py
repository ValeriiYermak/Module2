first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))

gcd = first if first > second else second

while first % gcd != 0 or second % gcd != 0: 
        gcd -= 1
print(gcd)       