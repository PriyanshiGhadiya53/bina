mc=[[0 for n in range(50)]for m in range(50)]
def matrix_chain(arr):
    n=len(arr)
    for length in range(2,n):
        for i in range(1,n-length+1):
            j=i+length-1
            mc[i][j]=999999

            for k in range(i,j):
                cost=(
                    mc[i][k]+
                    mc[k+1][j]+
                    arr[i-1]*arr[k]*arr[j]
             )
                mc[i][j]=min(mc[i][j],cost)

        print("After iteration",length-1)
        for i in range(1,n):
            print(mc[i][1:n])

        print()
            

arr=[5,10,15,20,25]
matrix_chain(arr)
print("Minimum number of matrix multiplication:",mc[1][len(arr)-1])