L = [1, 3, 5, 6, 7, 8, 10]
target = int(input("Enter target sum: "))

s=set()
for i in L:
    if target-i in s:
        print(i,target-i)
    s.add(i)    