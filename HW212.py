sum = 0
while True:  
    num = int(input("Enter integer (0 for output): "))
    if num == 0:
        print("The End")
        break
    for j in range(num):
        if j % 2 == 1:
            continue
        else:
            for j in range(num + 1):
                if j % 2 == 0:
                    sum += j
        print(f"The sum of numbers from null, {num},inclusive is equal to, {j}")
        break