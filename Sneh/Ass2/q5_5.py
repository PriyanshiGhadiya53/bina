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

    return dp[n][c]

def greedy(c,v,wt):
    item=[]
    n=len(v)

    for i in range(n):
        ratio=v[i]/wt[i]
        item.append((ratio,v[i],wt[i]))

    item.sort(reverse=True)
    total=0

    for ratio,v,wt in item:
        if c>=wt:
            c-=wt
            total+=v

    return total

n=int(input("enter value item:"))
v=[]
wt=[]

for i in range(n):
    value=int(input("enter the value:"))
    weight=int(input("enter the weight:"))

    v.append(value)
    wt.append(weight)

c=int(input("enter capacity:"))
result=knap(c,v,wt,n)
gredyresult=greedy(c,v,wt)
print("Maximum value of knap: ",result)
print("Maximum value of greedy: ",gredyresult)
