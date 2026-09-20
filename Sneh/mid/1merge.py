def mergeshort(arr):
    if len(arr)<=1:
        return arr

    mid=len(arr)//2
    leftside=arr[:mid]
    rightside=arr[mid:]

    shortedleft=mergeshort(leftside)
    shortedright=mergeshort(rightside)

    return merge(shortedleft,shortedright)

def merge(left,right):
    result=[]
    i=j=0

    while(i<len(left) and j<len(right)):
        if (left[i]<right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr=[34,11,23,98,-5,9,-9,0]
arraylist=mergeshort(arr)
print("shorted array:",arraylist)