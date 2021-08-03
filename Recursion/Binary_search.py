def binarySearch(arr,ele):
    if len(arr)==0:
        return False
    else:
        mid = int(len(arr)/2)
        if arr[mid] == ele:
            return True
        elif ele < arr[mid]:
            return binarySearch(arr[:mid],ele)
        elif ele > arr[mid]:
            return binarySearch(arr[mid:],ele)
        
print(binarySearch([1,2,3,4,5,6],6))         
            
        
        
    