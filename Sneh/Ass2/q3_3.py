def activity(start,finish):
    activities=list(zip(start,finish))
    activities.sort(key=lambda x:x[1])

    selected=[]
    last=0

    for s,f in activities:
        if s>=last:
            selected.append((s,f))
            last=f

    return selected



n=int(input("enter the number you want to pair."))
start=[]
finish=[]

for i in range(n):
    s=int(input("Starting point:"))
    f=int(input("finish point:"))

    start.append(s)
    finish.append(f)

result=activity(start,finish)
print("Selected activities:",result)
print("Total Activities:",len(result))