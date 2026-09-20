

mc=[[-1 for n in range(50)]for m in range(50)]
def matrix_chain(arr,i,j):
    if(i==j):
        return 0

    if(mc[i][j]!=-1):
        return mc[i][j]

    minimum=999999
    for k in range(i,j):
        cost=(
            matrix_chain(arr,i,k)+
            matrix_chain(arr,k+1,j)+
            arr[i-1]*arr[k]*arr[j]
        )
        minimum=min(minimum,cost)

    mc[i][j]=minimum
    return minimum

arr=list(map(int,input("Enter Number").split()))
result=matrix_chain(arr,1,len(arr)-1)
print("Minimum number of multiplications: ",result)