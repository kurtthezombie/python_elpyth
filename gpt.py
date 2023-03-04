n = int(input("Enter a positive integer not greater than 11: "))
for i in range(1, n+1):
    for j in range(i, i+n):
        if j <= n:
            print(j, end=" ")
        else:
            print(j-n, end=" ")
    print()