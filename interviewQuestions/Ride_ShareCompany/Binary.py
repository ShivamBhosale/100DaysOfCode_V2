def binarySearch(arr,ele):
    first = 0
    last = len(arr)-1
    found =  False
    
    while first <= last and not found:
        mid = int((first+last)/2)
        if arr[mid] == ele:
            found = True
        else:
            if ele < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

print(binarySearch([1,2,3,4,5,6,7,8,9,10],5))


def binarySearchRe(arr2,ele2):
    if len(arr2) == 0:
        return False
    else:
        mid = int(len(arr2)/2)
        if(arr2[mid] == ele2):
            return True
        else:
            if (arr2 < mid):
                return binarySearchRe(arr2[:mid],ele2)
            else:
                return binarySearchRe(arr2[mid+1:],ele2)
print(binarySearchRe([1,2,3,4,5,6,7,8,9,10],6))
        