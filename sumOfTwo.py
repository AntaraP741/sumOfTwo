L=[1,3,5,6,7,8,10]
target=11
for i in range(len(L)):
            for j in range(i+1,len(L)):
                if L[j]+L[i] == target:
                    print(L[i],L[j])
        