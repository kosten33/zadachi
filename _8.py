n = int(input())
m = int(input())


for i in range(n,m):
    for j in range(i,m):
        for k in range(j,m):
            if (i**2 + j**2 == k**2):
                print(i,j,k)
        
        

