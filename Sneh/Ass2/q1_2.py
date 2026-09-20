def merge_sort(arr):
    if len(arr)<=1:
        return arr

    mid=len(arr)//2
    leftside=arr[:mid]
    rightside=arr[mid:]

    sortedleft=merge_sort(leftside)
    sortedright=merge_sort(rightside)

    return merge(sortedleft,sortedright)
def merge(left,right):
    result=[]
    i=j=0

    while(i<len(left) and j<len(right)):
        if(left[i].lower()<right[j].lower()):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

list=["priya","amit","rahul","Nisha","Jiyansh","Rutvik"]
shortedmerge=merge_sort(list)
print("Merge sort:",shortedmerge)