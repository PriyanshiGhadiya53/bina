mc=[[-1 for n in range(50)]for m in range(50)]
brackt=[["" for n in range(50)]for m in range(50)]
def matrix_chain(arr,i,j):
    if i==j:
        brackt[i][j] = "A" + str(i)
        return 0
    if mc[i][j]!=-1:
        return mc[i][j]

    minimum=999999
    for k in range(i,j):
        cost=(
            matrix_chain(arr,i,k)+
            matrix_chain(arr,k+1,j)+
            arr[i-1]*arr[k]*arr[j]
        )
        if cost<minimum:
            minimum=cost

            brackt[i][j] = "(" + brackt[i][k] + "x" + brackt[k+1][j] + ")"

    mc[i][j]=minimum
    return minimum

arr=[5,10,15,20,25]
result=matrix_chain(arr,1,len(arr)-1)
print("Minimum Number of multiplication",result)
print("Optimal Parenthesization:",brackt[1][len(arr)-1])