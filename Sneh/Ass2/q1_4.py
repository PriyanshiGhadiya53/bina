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
    i=j=0
    result=[]
    while(i<len(left) and j<len(right)):
        if(left[i]["Salary"]<right[j]["Salary"]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

list=[
    {"EmployeeID": 101, "Name": "Amit", "Salary": 45000},
    {"EmployeeID": 102, "Name": "Priya", "Salary": 30000},
    {"EmployeeID": 103, "Name": "Rahul", "Salary": 55000},
    {"EmployeeID": 104, "Name": "Neha", "Salary": 40000},
    {"EmployeeID": 105, "Name": "Riya", "Salary": 35000}
]
sortedMerge=merge_sort(list)
print("sorted by Employee salary:\n")
for emp in sortedMerge:
    print(
    emp["EmployeeID"],
    emp["Name"],
    emp["Salary"]
    )

