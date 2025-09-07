L = [1, 3, 5, 6, 7, 8, 10]
target = int(input("Enter target sum: "))

for i in range(len(L)):
    for j in range(i + 1, len(L)):
        if L[i] + L[j] == target:
            print(L[i], L[j])

        