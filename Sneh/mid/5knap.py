def knap(c,val,wt,n):
    if n==0 or c==0:
        return 0

    if wt[n-1]>c:
        return knap(c,val,wt,n-1)

    pick=val[n-1]+knap(c-wt[n-1],val,wt,n-1)
    notpick=knap(c,val,wt,n-1)
    return max(pick,notpick)


val=[1,7,11]
wt=[1,2,3]
c=5

result=knap(c,val,wt,len(val))
print("Maximum Value:",result)