def fknap(c,wt,v):
    n=len(v)
    item=[]

    for i in range(n):
        ratio=v[i]/wt[i]
        item.append((ratio,v[i],wt[i]))

    item.sort(reverse=True)
    total=0

    for ratio,v,wt in item:
        print("value:",v,"Weight:",wt,"Ratio:",round(ratio,2))

        if c>=wt:
            c-=wt
            total+=v
            print("Full item selected")
        else:
            total+=ratio*c
            print("Fraction selected:", c)
            break

    return total
    


v=[100,60,120]
wt=[20,10,30]
c=50

result=fknap(c,wt,v)
print("Maximum value=",round(result,2))