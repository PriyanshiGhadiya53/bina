count=0
def merge_sort(arr):
    if(len(arr)<=1):
        return arr

    mid=len(arr)//2
    leftside=arr[:mid]
    rightside=arr[mid:]

    sortedleft=merge_sort(leftside)
    sortedright=merge_sort(rightside)

    return merge(sortedleft,sortedright)
def merge(left,right):
    global count
    i=j=0
    result=[]


    while(i<len(left) and j<len(right)):
        count+=1
        if(left[i] <right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


list=[ 12.5, 3.2, 8.7, 1.5, 15.6, 7.4, 10.1, 2.8, 6.3, 14.9,4.6, 9.8, 11.2, 5.5, 13.7]
sortedMerge=merge_sort(list)
print("Merge Sort:",sortedMerge)
print("Number of comparisons:", count)