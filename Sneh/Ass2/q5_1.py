
def knap(c,v,wt,n):
    dp=[[0 for j in range(c+1)]for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,c+1):
            if wt[i-1]<=j:
                pick=v[i-1]+dp[i-1][j-wt[i-1]]
                notpick=dp[i-1][j]
                dp[i][j]=max(pick,notpick)
            else:
                dp[i][j]=dp[i-1][j]

    print("dp table:")
    for row in dp:
        print(row)


    return dp[n][c]




v=[1,7,11]
wt=[1,2,3]
c=5
result=knap(c,v,wt,len(v))
print("Maximum value: ",result)