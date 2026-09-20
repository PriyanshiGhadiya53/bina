def activity_sort(start,finish):
    activitist=list(zip(start,finish))
    activitist.sort(key=lambda x:x[1])
    select=[]
    last_end=0

    for s,f in activitist:
        if s>=last_end:
            select.append((s,f))
            last_end=f

    return select


start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
result=activity_sort(start,finish)
print("selected pairs:",result)
print("len of the result",len(result))